"""
Markdown Generator
Generates markdown files for rankings following HCI principles
"""

from typing import List, Dict
from pathlib import Path
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MarkdownGenerator:
    """Generate markdown files for rankings"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.output_dir = Path(__file__).parent.parent.parent / 'rankings'
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_header(self, title: str, description: str) -> str:
        """Generate markdown header"""
        return f"""# {title}

{description}

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

---

"""
    
    def generate_navigation(self, current_page: str) -> str:
        """Generate navigation links"""
        nav = """## Navigation

- [National Rankings](../national/README.md)
- [By Wilaya](../by-wilaya/README.md)
- [By Category](../by-category/README.md)
- [Home](../README.md)

---

"""
        return nav
    
    def generate_user_table(self, users: List[Dict], category: str) -> str:
        """
        Generate markdown table for users
        
        Args:
            users: List of ranked users
            category: Ranking category
            
        Returns:
            Markdown table string
        """
        if not users:
            return "No users found matching criteria.\n"
        
        # Table header
        table = """| Rank | User | Name | Location | Followers | Repos | Stars | Score |
|------|------|------|----------|-----------|-------|-------|-------|
"""
        
        # Table rows
        for user in users[:100]:  # Top 100
            rank = user.get('rank', '-')
            username = user.get('username', 'Unknown')
            name = user.get('name') or username
            location = user.get('location', '-')
            followers = user.get('followers', 0)
            repos = user.get('public_repos', 0)
            stars = user.get('total_stars', 0)
            score = user.get('score', 0)
            
            # Truncate long names
            if len(name) > 20:
                name = name[:17] + '...'
            if len(location) > 15:
                location = location[:12] + '...'
            
            table += f"| {rank} | [@{username}](https://github.com/{username}) | {name} | {location} | {followers} | {repos} | {stars} | {score:.0f} |\n"
        
        return table
    
    def generate_wilaya_summary(self, wilaya_rankings: Dict) -> str:
        """Generate summary table of all wilayas"""
        summary = """## Summary by Wilaya

| Code | Wilaya | Users | Top User | Followers |
|------|--------|-------|----------|-----------|
"""
        
        for wilaya in self.config['wilayas']:
            code = wilaya['code']
            name = wilaya['name_en']
            
            # Get users for this wilaya (from any category)
            users = wilaya_rankings.get(code, [])
            user_count = len(users)
            
            if users:
                top_user = users[0]
                top_username = top_user.get('username', '-')
                top_followers = top_user.get('followers', 0)
                summary += f"| {code} | {name} | {user_count} | [@{top_username}](https://github.com/{top_username}) | {top_followers} |\n"
            else:
                summary += f"| {code} | {name} | 0 | - | - |\n"
        
        return summary
    
    def generate_category_ranking(self, rankings: Dict, category: str):
        """Generate ranking file for specific category"""
        category_config = next((c for c in self.config['ranking_categories'] if c['id'] == category), None)
        if not category_config:
            logger.error(f"Category {category} not found")
            return
        
        # National ranking
        national_users = rankings['national'].get(category, [])
        
        content = self.generate_header(
            f"Algeria GitHub Rankings - {category_config['name']}",
            category_config['description']
        )
        content += self.generate_navigation(category)
        content += f"\n## Top 100 Users - {category_config['name']}\n\n"
        content += self.generate_user_table(national_users, category)
        
        # Save file
        output_path = self.output_dir / 'by-category' / f"{category}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Generated ranking for category: {category}")
    
    def generate_wilaya_ranking(self, rankings: Dict, wilaya_code: str):
        """Generate ranking file for specific wilaya"""
        wilaya = next((w for w in self.config['wilayas'] if w['code'] == wilaya_code), None)
        if not wilaya:
            logger.error(f"Wilaya {wilaya_code} not found")
            return
        
        content = self.generate_header(
            f"GitHub Rankings - {wilaya['name_en']} ({wilaya['name_ar']})",
            f"Top GitHub users from {wilaya['name_en']} wilaya"
        )
        content += self.generate_navigation(f"wilaya_{wilaya_code}")
        
        # Generate rankings for each category
        for category_config in self.config['ranking_categories']:
            category_id = category_config['id']
            users = rankings['by_wilaya'].get(category_id, {}).get(wilaya_code, [])
            
            content += f"\n## {category_config['name']}\n\n"
            content += self.generate_user_table(users, category_id)
        
        # Save file
        output_path = self.output_dir / 'by-wilaya' / f"wilaya_{wilaya_code}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Generated ranking for wilaya: {wilaya['name_en']}")
    
    def generate_all_rankings(self, rankings: Dict):
        """Generate all ranking files"""
        logger.info("Generating all ranking files...")
        
        # Generate category rankings
        for category_config in self.config['ranking_categories']:
            self.generate_category_ranking(rankings, category_config['id'])
        
        # Generate wilaya rankings
        for wilaya in self.config['wilayas']:
            self.generate_wilaya_ranking(rankings, wilaya['code'])
        
        # Generate index files
        self.generate_index_files(rankings)
        
        logger.info("All ranking files generated successfully")
    
    def generate_index_files(self, rankings: Dict):
        """Generate index/README files for navigation"""
        # Main index
        main_index = self.generate_header(
            "Algeria GitHub Rankings",
            "Comprehensive rankings of GitHub users across all 69 Algerian wilayas"
        )
        main_index += """
## Quick Links

- [National Rankings](national/README.md) - Top users across Algeria
- [By Wilaya](by-wilaya/README.md) - Rankings for each wilaya
- [By Category](by-category/README.md) - Rankings by contribution type

## Statistics

"""
        main_index += f"- Total Users Ranked: {rankings['total_users']}\n"
        main_index += f"- Wilayas Covered: 69\n"
        main_index += f"- Categories: {len(self.config['ranking_categories'])}\n"
        
        with open(self.output_dir / 'README.md', 'w', encoding='utf-8') as f:
            f.write(main_index)
        
        logger.info("Generated index files")
