"""
Collect Real GitHub Data for Algeria Rankings
Starts with major wilayas for faster results
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from collectors.github_collector import GitHubCollector
from processors.ranking_processor import RankingProcessor
from generators.markdown_generator import MarkdownGenerator
import json

# Priority wilayas (major cities with most developers)
PRIORITY_WILAYAS = [
    "16",  # Algiers
    "31",  # Oran
    "25",  # Constantine
    "19",  # Sétif
    "06",  # Béjaïa
    "15",  # Tizi Ouzou
    "09",  # Blida
    "23",  # Annaba
    "13",  # Tlemcen
    "35",  # Boumerdès
]

def load_config():
    """Load wilayas configuration"""
    config_path = Path(__file__).parent / 'config' / 'wilayas.json'
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def collect_priority_wilayas():
    """Collect data for priority wilayas first"""
    print("=" * 60)
    print("COLLECTING REAL GITHUB DATA FOR ALGERIA")
    print("=" * 60)
    print()
    
    # Check token
    token = os.getenv('GITHUB_TOKEN')
    if not token or token == 'your_token_here':
        print("❌ ERROR: GitHub token not configured!")
        print()
        print("Please follow these steps:")
        print("1. Go to: https://github.com/settings/tokens")
        print("2. Click 'Generate new token (classic)'")
        print("3. Select scopes: read:user, public_repo")
        print("4. Copy the token")
        print("5. Edit .env file and replace 'your_token_here' with your token")
        print()
        return False
    
    # Initialize collector
    try:
        collector = GitHubCollector(token)
        remaining = collector.check_rate_limit()
        print(f"✅ GitHub API connected")
        print(f"📊 Rate limit remaining: {remaining} requests")
        print()
    except Exception as e:
        print(f"❌ Error connecting to GitHub API: {e}")
        return False
    
    # Load config
    config = load_config()
    wilayas_dict = {w['code']: w for w in config['wilayas']}
    
    # Collect data for priority wilayas
    print("🎯 Collecting data for major wilayas (fastest results):")
    print()
    
    all_users = []
    
    for wilaya_code in PRIORITY_WILAYAS:
        wilaya = wilayas_dict.get(wilaya_code)
        if not wilaya:
            continue
        
        print(f"📍 Collecting: {wilaya['name_en']} ({wilaya['name_ar']})...")
        
        try:
            users = collector.collect_wilaya_data(wilaya)
            
            if users:
                # Save raw data
                output_path = Path(__file__).parent / 'data' / 'raw' / f"wilaya_{wilaya_code}.json"
                collector.save_data(users, str(output_path))
                all_users.extend(users)
                print(f"   ✅ Found {len(users)} developers")
            else:
                print(f"   ⚠️  No developers found")
        
        except Exception as e:
            print(f"   ❌ Error: {e}")
            continue
        
        print()
    
    print("=" * 60)
    print(f"✅ Data collection complete!")
    print(f"📊 Total developers collected: {len(all_users)}")
    print("=" * 60)
    print()
    
    return all_users

def generate_rankings(users):
    """Generate rankings from collected data"""
    if not users:
        print("❌ No data to generate rankings")
        return False
    
    print("🔄 Generating rankings...")
    print()
    
    # Load config
    config = load_config()
    
    # Process rankings
    processor = RankingProcessor(config)
    rankings = processor.process_rankings(users)
    
    # Generate markdown files
    generator = MarkdownGenerator(config)
    generator.generate_all_rankings(rankings)
    
    print("✅ Rankings generated successfully!")
    print(f"📁 Location: rankings/")
    print()
    print("🌐 To view:")
    print("   1. cd rankings")
    print("   2. python -m http.server 8000")
    print("   3. Open http://localhost:8000")
    print()
    
    return True

def main():
    """Main execution"""
    print()
    
    # Collect data
    users = collect_priority_wilayas()
    
    if not users:
        print("❌ No data collected. Please check your GitHub token.")
        return
    
    # Generate rankings
    success = generate_rankings(users)
    
    if success:
        print("=" * 60)
        print("🎉 SUCCESS! Your rankings are ready!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("1. View locally: cd rankings && python -m http.server 8000")
        print("2. Deploy to GitHub Pages:")
        print("   - git add rankings/")
        print("   - git commit -m 'Add real rankings data'")
        print("   - git push origin master")
        print("   - Enable GitHub Pages in repository settings")
        print()
        print("Your site will be live at:")
        print("https://samir-guenchi.github.io/algeria-github-rankings/")
        print()

if __name__ == "__main__":
    main()
