# buzzsprout-client
Python client for Buzzsprout API

## Installation

```bash
pip install buzzsprout-client
```

## Usage

```python
from buzzsprout_client import BuzzsproutClient

# Initialize client with your API key
client = BuzzsproutClient(api_key="your_api_key_here")

# Get all podcasts
podcasts = client.get_podcasts()

# Get a specific podcast
podcast = client.get_podcast(podcast_id=12345)

# Get all episodes for a podcast
episodes = client.get_episodes(podcast_id=12345)

# Get a specific episode
episode = client.get_episode(podcast_id=12345, episode_id=67890)

# Create a new episode
new_episode = client.create_episode(
    podcast_id=12345,
    title="My New Episode",
    audio_file="path/to/audio.mp3",
    description="This is my new episode",
    private=True
)

# Update an existing episode
updated_episode = client.update_episode(
    podcast_id=12345,
    episode_id=67890,
    title="Updated Episode Title",
    private=False,
    audio_url="https://example.com/new-audio.mp3"
)

# Update episode with file uploads
updated_episode = client.update_episode(
    podcast_id=12345,
    episode_id=67890,
    title="Updated Episode Title",
    private=False,
    audio_file="path/to/new-audio.mp3",
    artwork_file="path/to/new-artwork.jpg"
)
```
