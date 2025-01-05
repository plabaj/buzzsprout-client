import requests
from typing import List, Dict, Optional

class BuzzsproutClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://www.buzzsprout.com/api"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Token token={self.api_key}",
            "Accept": "application/json"
        })

    def get_podcasts(self) -> List[Dict]:
        """Get all podcasts associated with the account.
        
        Returns:
            List of podcast dictionaries containing podcast details
        """
        url = f"{self.base_url}/podcasts.json"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_podcast(self, podcast_id: int) -> Optional[Dict]:
        """Get details for a specific podcast.
        
        Args:
            podcast_id: ID of the podcast to retrieve
            
        Returns:
            Dictionary containing podcast details or None if not found
        """
        url = f"{self.base_url}/podcasts/{podcast_id}.json"
        response = self.session.get(url)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()

    def get_episodes(self, podcast_id: int) -> List[Dict]:
        """Get all episodes for a specific podcast.
        
        Args:
            podcast_id: ID of the podcast to retrieve episodes for
            
        Returns:
            List of episode dictionaries containing episode details
        """
        url = f"{self.base_url}/{podcast_id}/episodes.json"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_episode(self, podcast_id: int, episode_id: int) -> Optional[Dict]:
        """Get details for a specific episode.
        
        Args:
            podcast_id: ID of the podcast containing the episode
            episode_id: ID of the episode to retrieve
            
        Returns:
            Dictionary containing episode details or None if not found
        """
        url = f"{self.base_url}/{podcast_id}/episodes/{episode_id}.json"
        response = self.session.get(url)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()
