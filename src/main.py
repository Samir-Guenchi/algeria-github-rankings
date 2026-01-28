"""
Main entry point for Algeria GitHub Rankings
"""

import argparse
import json
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from collectors.github_collector import GitHubCollector
from processors.ranking_processor import RankingProcessor
from generators.markdown_generator import MarkdownGenerator


def load_wilayas_config():
    """Load wilayas configuration"""
    config_path = Path(__file__).parent.parent / 'config' / 'wilayas.json'
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def collect_all_data(collector: GitHubCollector, config: dict):
    """Collect data for all wilayas"""
    print("Starting data collection for all 69 wilayas...")
    
    for wilaya in config['wilayas']:
        try:
            users = collector.collect_wilaya_data(wilaya)
            
            # Save raw data
            output_path = Path(__file__).parent.parent / 'data' / 'raw' / f"wilaya_{wilaya['code']}.json"
            collector.save_data(users, str(output_path))
            
        except Exception as e:
            print(f"Error collecting data for {wilaya['name_en']}: {e}")
            continue
    
    print("Data collection completed!")


def collect_wilaya_data(collector: GitHubCollector, config: dict, wilaya_name: str):
    """Collect data for specific wilaya"""
    wilaya = next((w for w in config['wilayas'] if w['name_en'].lower() == wilaya_name.lower()), None)
    
    if not wilaya:
        print(f"Wilaya '{wilaya_name}' not found")
        return
    
    print(f"Collecting data for {wilaya['name_en']}...")
    users = collector.collect_wilaya_data(wilaya)
    
    output_path = Path(__file__).parent.parent / 'data' / 'raw' / f"wilaya_{wilaya['code']}.json"
    collector.save_data(users, str(output_path))
    
    print(f"Data collection completed for {wilaya['name_en']}")


def generate_rankings(config: dict, category: str = None):
    """Generate rankings from collected data"""
    print("Generating rankings...")
    
    processor = RankingProcessor(config)
    generator = MarkdownGenerator(config)
    
    # Load all collected data
    data_dir = Path(__file__).parent.parent / 'data' / 'raw'
    all_users = []
    
    for json_file in data_dir.glob('wilaya_*.json'):
        with open(json_file, 'r', encoding='utf-8') as f:
            users = json.load(f)
            all_users.extend(users)
    
    print(f"Loaded {len(all_users)} users from collected data")
    
    # Process rankings
    rankings = processor.process_rankings(all_users)
    
    # Generate markdown files
    if category:
        generator.generate_category_ranking(rankings, category)
    else:
        generator.generate_all_rankings(rankings)
    
    print("Rankings generated successfully!")


def main():
    parser = argparse.ArgumentParser(description='Algeria GitHub Rankings')
    parser.add_argument('--collect-all', action='store_true', help='Collect data for all wilayas')
    parser.add_argument('--collect', action='store_true', help='Collect data for specific wilaya')
    parser.add_argument('--wilaya', type=str, help='Wilaya name for collection')
    parser.add_argument('--generate-all', action='store_true', help='Generate all rankings')
    parser.add_argument('--generate', action='store_true', help='Generate specific category ranking')
    parser.add_argument('--category', type=str, help='Ranking category')
    parser.add_argument('--check-rate-limit', action='store_true', help='Check GitHub API rate limit')
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_wilayas_config()
    
    # Initialize collector
    try:
        collector = GitHubCollector()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please set GITHUB_TOKEN environment variable")
        return
    
    # Execute commands
    if args.check_rate_limit:
        remaining = collector.check_rate_limit()
        print(f"GitHub API rate limit remaining: {remaining}")
    
    elif args.collect_all:
        collect_all_data(collector, config)
    
    elif args.collect:
        if not args.wilaya:
            print("Error: --wilaya required with --collect")
            return
        collect_wilaya_data(collector, config, args.wilaya)
    
    elif args.generate_all:
        generate_rankings(config)
    
    elif args.generate:
        if not args.category:
            print("Error: --category required with --generate")
            return
        generate_rankings(config, args.category)
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
