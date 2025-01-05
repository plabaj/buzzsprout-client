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

    def update_episode(
        self,
        podcast_id: int,
        episode_id: int,
        title: Optional[str] = None,
        audio_file: Optional[str] = None,
        audio_url: Optional[str] = None,
        artwork_file: Optional[str] = None,
        artwork_url: Optional[str] = None,
        description: Optional[str] = None,
        summary: Optional[str] = None,
        artist: Optional[str] = None,
        tags: Optional[str] = None,
        published_at: Optional[str] = None,
        duration: Optional[int] = None,
        guid: Optional[str] = None,
        inactive_at: Optional[str] = None,
        episode_number: Optional[int] = None,
        season_number: Optional[int] = None,
        explicit: Optional[bool] = None,
        private: Optional[bool] = None,
        email_user_after_audio_processed: Optional[bool] = None
    ) -> Dict:
        """Update an existing episode.
        
        Args:
            podcast_id: ID of the podcast containing the episode
            episode_id: ID of the episode to update
            title: New episode title
            audio_file: Path to new audio file to upload
            audio_url: URL of new hosted audio file
            artwork_file: Path to new artwork image file to upload
            artwork_url: URL of new hosted artwork image
            description: New episode description
            summary: New episode summary
            artist: New episode artist
            tags: New comma-separated tags
            published_at: New publish date in ISO 8601 format
            duration: New episode duration in seconds
            guid: New custom GUID
            inactive_at: New date to make episode inactive
            episode_number: New episode number
            season_number: New season number
            explicit: Whether episode contains explicit content
            private: Whether episode is private
            email_user_after_audio_processed: Whether to email user after processing
            
        Returns:
            Dictionary containing updated episode details
            
        Raises:
            requests.HTTPError: If API request fails
        """
        url = f"{self.base_url}/{podcast_id}/episodes/{episode_id}.json"
        data = {
            "title": title,
            "description": description,
            "summary": summary,
            "artist": artist,
            "tags": tags,
            "published_at": published_at,
            "duration": duration,
            "guid": guid,
            "inactive_at": inactive_at,
            "episode_number": episode_number,
            "season_number": season_number,
            "explicit": explicit,
            "private": private,
            "email_user_after_audio_processed": email_user_after_audio_processed,
            "audio_url": audio_url,
            "artwork_url": artwork_url
        }
        
        # Remove None values to avoid sending nulls
        data = {k: v for k, v in data.items() if v is not None}
        
        files = {}
        if audio_file:
            files["audio_file"] = open(audio_file, "rb")
        if artwork_file:
            files["artwork_file"] = open(artwork_file, "rb")
            
        response = self.session.put(url, data=data, files=files or None)
        response.raise_for_status()
        return response.json()

    def create_episode(
        self,
        podcast_id: int,
        title: str,
        audio_file: Optional[str] = None,
        audio_url: Optional[str] = None,
        artwork_file: Optional[str] = None,
        artwork_url: Optional[str] = None,
        description: str = "",
        summary: str = "",
        artist: str = "",
        tags: str = "",
        published_at: Optional[str] = None,
        duration: Optional[int] = None,
        guid: Optional[str] = None,
        inactive_at: Optional[str] = None,
        episode_number: Optional[int] = None,
        season_number: Optional[int] = None,
        explicit: bool = False,
        private: bool = False,
        email_user_after_audio_processed: bool = True
    ) -> Dict:
        """Create a new episode.
        
        Args:
            podcast_id: ID of the podcast to add the episode to
            title: Episode title (required)
            audio_file: Path to audio file to upload
            audio_url: URL of hosted audio file
            artwork_file: Path to artwork image file to upload
            artwork_url: URL of hosted artwork image
            description: Episode description
            summary: Episode summary
            artist: Episode artist
            tags: Comma-separated tags
            published_at: Publish date in ISO 8601 format
            duration: Episode duration in seconds
            guid: Custom GUID
            inactive_at: Date to make episode inactive
            episode_number: Episode number
            season_number: Season number
            explicit: Whether episode contains explicit content
            private: Whether episode is private
            email_user_after_audio_processed: Whether to email user after processing
            
        Returns:
            Dictionary containing created episode details
            
        Raises:
            ValueError: If neither audio_file nor audio_url is provided
            requests.HTTPError: If API request fails
        """
        if not audio_file and not audio_url:
            raise ValueError("Either audio_file or audio_url must be provided")
            
        url = f"{self.base_url}/{podcast_id}/episodes.json"
        data = {
            "title": title,
            "description": description,
            "summary": summary,
            "artist": artist,
            "tags": tags,
            "published_at": published_at,
            "duration": duration,
            "guid": guid,
            "inactive_at": inactive_at,
            "episode_number": episode_number,
            "season_number": season_number,
            "explicit": explicit,
            "private": private,
            "email_user_after_audio_processed": email_user_after_audio_processed,
            "audio_url": audio_url,
            "artwork_url": artwork_url
        }
        
        files = {}
        if audio_file:
            files["audio_file"] = open(audio_file, "rb")
        if artwork_file:
            files["artwork_file"] = open(artwork_file, "rb")
            
        response = self.session.post(url, data=data, files=files or None)
        response.raise_for_status()
        return response.json()
