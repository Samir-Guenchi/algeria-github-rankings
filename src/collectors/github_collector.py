"""
GitHub Data Collector for Algeria Rankings
Collects user data from GitHub API for all 69 Algerian wilayas
"""

import os
import json
import time
import requests
from typing import List, Dict, Optional
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GitHubCollector:
    """Collects GitHub user data using GitHub API"""
    
    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv('GITHUB_TOKEN')
        if not self.token:
            raise ValueError("GitHub token required. Set GITHUB_TOKEN environment variable.")
        
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.base_url = 'https://api.github.com'
        self.rate_limit_remaining = 5000
        
    def check_rate_limit(self):
        """Check GitHub API rate limit"""
        response = requests.get(
            f'{self.base_url}/rate_limit',
            headers=self.headers
        )
        data = response.json()
        self.rate_limit_remaining = data['rate']['remaining']
        logger.info(f"Rate limit remaining: {self.rate_limit_remaining}")
        return self.rate_limit_remaining
    
    def search_users_by_location(self, location: str, min_followers: int = 5) -> List[Dict]:
        """
        Search GitHub users by location
        
        Args:
            location: Location search term
            min_followers: Minimum number of followers
            
        Returns:
            List of user data dictionaries
        """
        users = []
        page = 1
        per_page = 100
        
        while True:
            if self.rate_limit_remaining < 10:
                logger.warning("Rate limit low, waiting 60 seconds...")
                time.sleep(60)
                self.check_rate_limit()
            
            query = f'location:{location} followers:>={min_followers}'
            url = f'{self.base_url}/search/users'
            params = {
                'q': query,
                'per_page': per_page,
                'page': page,
                'sort': 'followers',
                'order': 'desc'
            }
            
            try:
                response = requests.get(url, headers=self.headers, params=params)
                response.raise_for_status()
                data = response.json()
                
                if 'items' not in data or len(data['items']) == 0:
                    break
                
                users.extend(data['items'])
                logger.info(f"Collected {len(users)} users for location: {location}")
                
                # Check if there are more pages
                if len(data['items']) < per_page:
                    break
                    
                page += 1
                time.sleep(2)  # Rate limiting
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Error fetching users for {location}: {e}")
                break
        
        return users
    
    def get_user_details(self, username: str) -> Optional[Dict]:
        """
        Get detailed information for a specific user
        
        Args:
            username: GitHub username
            
        Returns:
            User details dictionary or None
        """
        if self.rate_limit_remaining < 10:
            logger.warning("Rate limit low, waiting 60 seconds...")
            time.sleep(60)
            self.check_rate_limit()
        
        try:
            response = requests.get(
                f'{self.base_url}/users/{username}',
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching details for {username}: {e}")
            return None
    
    def get_user_repos(self, username: str) -> List[Dict]:
        """
        Get user's public repositories
        
        Args:
            username: GitHub username
            
        Returns:
            List of repository dictionaries
        """
        repos = []
        page = 1
        per_page = 100
        
        while True:
            if self.rate_limit_remaining < 10:
                time.sleep(60)
                self.check_rate_limit()
            
            try:
                response = requests.get(
                    f'{self.base_url}/users/{username}/repos',
                    headers=self.headers,
                    params={'per_page': per_page, 'page': page, 'sort': 'updated'}
                )
                response.raise_for_status()
                data = response.json()
                
                if not data:
                    break
                
                repos.extend(data)
                
                if len(data) < per_page:
                    break
                    
                page += 1
                time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Error fetching repos for {username}: {e}")
                break
        
        return repos
    
    def get_user_contributions(self, username: str) -> int:
        """
        Estimate user contributions from events
        Note: GitHub API doesn't provide total contribution count directly
        
        Args:
            username: GitHub username
            
        Returns:
            Estimated contribution count
        """
        try:
            response = requests.get(
                f'{self.base_url}/users/{username}/events/public',
                headers=self.headers,
                params={'per_page': 100}
            )
            response.raise_for_status()
            events = response.json()
            
            # Count different event types as contributions
            contribution_events = [
                'PushEvent', 'PullRequestEvent', 'IssuesEvent',
                'IssueCommentEvent', 'PullRequestReviewEvent'
            ]
            
            contributions = sum(1 for event in events if event['type'] in contribution_events)
            return contributions
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching contributions for {username}: {e}")
            return 0
    
    def collect_wilaya_data(self, wilaya: Dict) -> List[Dict]:
        """
        Collect all user data for a specific wilaya
        
        Args:
            wilaya: Wilaya configuration dictionary
            
        Returns:
            List of enriched user data
        """
        logger.info(f"Collecting data for {wilaya['name_en']} ({wilaya['code']})")
        
        all_users = []
        seen_usernames = set()
        
        # Search by all search terms
        for term in wilaya['search_terms']:
            users = self.search_users_by_location(term)
            
            for user in users:
                if user['login'] not in seen_usernames:
                    seen_usernames.add(user['login'])
                    
                    # Get detailed user info
                    details = self.get_user_details(user['login'])
                    if details:
                        # Get repositories
                        repos = self.get_user_repos(user['login'])
                        
                        # Calculate stats
                        total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
                        total_forks = sum(repo.get('forks_count', 0) for repo in repos)
                        
                        enriched_user = {
                            'username': user['login'],
                            'name': details.get('name'),
                            'avatar_url': details.get('avatar_url'),
                            'bio': details.get('bio'),
                            'company': details.get('company'),
                            'location': details.get('location'),
                            'email': details.get('email'),
                            'blog': details.get('blog'),
                            'twitter_username': details.get('twitter_username'),
                            'followers': details.get('followers', 0),
                            'following': details.get('following', 0),
                            'public_repos': details.get('public_repos', 0),
                            'public_gists': details.get('public_gists', 0),
                            'total_stars': total_stars,
                            'total_forks': total_forks,
                            'created_at': details.get('created_at'),
                            'updated_at': details.get('updated_at'),
                            'wilaya_code': wilaya['code'],
                            'wilaya_name': wilaya['name_en'],
                            'collected_at': datetime.utcnow().isoformat()
                        }
                        
                        all_users.append(enriched_user)
                        logger.info(f"Collected data for {user['login']}")
                        
                        time.sleep(1)  # Rate limiting
        
        logger.info(f"Total users collected for {wilaya['name_en']}: {len(all_users)}")
        return all_users
    
    def save_data(self, data: List[Dict], filepath: str):
        """Save collected data to JSON file"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"Data saved to {filepath}")


if __name__ == '__main__':
    # Example usage
    collector = GitHubCollector()
    collector.check_rate_limit()
