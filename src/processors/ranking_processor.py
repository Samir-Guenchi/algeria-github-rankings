"""
Ranking Processor
Processes collected GitHub data and generates rankings
"""

from typing import List, Dict
from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RankingProcessor:
    """Process and rank GitHub users"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.categories = config['ranking_categories']
        self.thresholds = config['minimum_thresholds']
    
    def filter_users(self, users: List[Dict]) -> List[Dict]:
        """
        Filter users based on minimum thresholds
        
        Args:
            users: List of user dictionaries
            
        Returns:
            Filtered list of users
        """
        filtered = []
        
        for user in users:
            if (user.get('followers', 0) >= self.thresholds['followers'] and
                user.get('public_repos', 0) >= self.thresholds['repositories']):
                filtered.append(user)
        
        logger.info(f"Filtered {len(filtered)} users from {len(users)} total")
        return filtered
    
    def calculate_score(self, user: Dict, category: str) -> float:
        """
        Calculate ranking score for a user in a specific category
        
        Args:
            user: User dictionary
            category: Ranking category ID
            
        Returns:
            Calculated score
        """
        if category == 'public_contributions':
            # Estimate from repos and activity
            return user.get('public_repos', 0) * 10 + user.get('public_gists', 0) * 5
        
        elif category == 'total_contributions':
            # Similar to public but with weight
            return user.get('public_repos', 0) * 12 + user.get('total_stars', 0)
        
        elif category == 'followers':
            return user.get('followers', 0)
        
        elif category == 'stars':
            return user.get('total_stars', 0)
        
        elif category == 'repositories':
            return user.get('public_repos', 0)
        
        return 0
    
    def rank_by_category(self, users: List[Dict], category: str) -> List[Dict]:
        """
        Rank users by specific category
        
        Args:
            users: List of user dictionaries
            category: Ranking category ID
            
        Returns:
            Sorted list of users with ranks
        """
        # Calculate scores
        for user in users:
            user['score'] = self.calculate_score(user, category)
        
        # Sort by score descending
        ranked = sorted(users, key=lambda x: x['score'], reverse=True)
        
        # Add rank numbers
        for i, user in enumerate(ranked, 1):
            user['rank'] = i
        
        return ranked
    
    def rank_by_wilaya(self, users: List[Dict], category: str) -> Dict[str, List[Dict]]:
        """
        Rank users grouped by wilaya
        
        Args:
            users: List of user dictionaries
            category: Ranking category ID
            
        Returns:
            Dictionary mapping wilaya codes to ranked user lists
        """
        # Group by wilaya
        by_wilaya = defaultdict(list)
        for user in users:
            wilaya_code = user.get('wilaya_code', '00')
            by_wilaya[wilaya_code].append(user)
        
        # Rank within each wilaya
        ranked_by_wilaya = {}
        for wilaya_code, wilaya_users in by_wilaya.items():
            ranked_by_wilaya[wilaya_code] = self.rank_by_category(wilaya_users, category)
        
        return ranked_by_wilaya
    
    def process_rankings(self, users: List[Dict]) -> Dict:
        """
        Process all rankings
        
        Args:
            users: List of all collected users
            
        Returns:
            Dictionary containing all ranking data
        """
        logger.info(f"Processing rankings for {len(users)} users")
        
        # Filter users
        filtered_users = self.filter_users(users)
        
        rankings = {
            'total_users': len(filtered_users),
            'by_category': {},
            'by_wilaya': {},
            'national': {}
        }
        
        # Generate rankings for each category
        for category_config in self.categories:
            category_id = category_config['id']
            logger.info(f"Processing category: {category_id}")
            
            # National ranking
            national_ranking = self.rank_by_category(filtered_users.copy(), category_id)
            rankings['national'][category_id] = national_ranking[:100]  # Top 100
            
            # By wilaya ranking
            wilaya_rankings = self.rank_by_wilaya(filtered_users.copy(), category_id)
            rankings['by_wilaya'][category_id] = wilaya_rankings
        
        logger.info("Rankings processing completed")
        return rankings
