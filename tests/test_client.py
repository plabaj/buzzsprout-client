import pytest
from unittest.mock import Mock, patch
from buzzsprout_client import BuzzsproutClient

@pytest.fixture
def mock_session():
    return Mock()

def test_client_initialization():
    client = BuzzsproutClient(api_key="test_key")
    assert client.api_key == "test_key"
    assert client.base_url == "https://www.buzzsprout.com/api"

def test_authentication_header(mock_session):
    test_key = "test_api_key_123"
    
    # Create client with mocked session
    with patch('buzzsprout_client.client.requests.Session', return_value=mock_session):
        client = BuzzsproutClient(api_key=test_key)
        
        # Verify headers were set correctly
        expected_headers = {
            "Authorization": f"Token token={test_key}",
            "Accept": "application/json"
        }
        mock_session.headers.update.assert_called_with(expected_headers)

def test_base_url():
    client = BuzzsproutClient(api_key="test_key")
    assert client.base_url == "https://www.buzzsprout.com/api"

def test_get_episodes(mock_session):
    test_key = "test_api_key_789"
    podcast_id = 12345
    mock_response = [
        {
            "id": 788881,
            "title": "Test Episode",
            "audio_url": "https://example.com/episode.mp3"
        }
    ]
    
    # Setup mock session
    mock_session.get.return_value.json.return_value = mock_response
    mock_session.get.return_value.raise_for_status = Mock()
    
    with patch('buzzsprout_client.client.requests.Session', return_value=mock_session):
        client = BuzzsproutClient(api_key=test_key)
        
        # Call the method
        episodes = client.get_episodes(podcast_id)
        
        # Verify the request was made correctly
        expected_url = f"https://www.buzzsprout.com/api/{podcast_id}/episodes.json"
        mock_session.get.assert_called_once_with(expected_url)
        
        # Verify the response
        assert episodes == mock_response
        assert len(episodes) == 1
        assert episodes[0]["title"] == "Test Episode"

def test_authentication_in_requests(mock_session):
    test_key = "test_api_key_456"
    
    # Set up mock headers as a real dictionary
    mock_headers = {
        "Authorization": f"Token token={test_key}",
        "Accept": "application/json"
    }
    mock_session.headers = mock_headers
    
    # Create client with mocked session
    with patch('buzzsprout_client.client.requests.Session', return_value=mock_session):
        client = BuzzsproutClient(api_key=test_key)
        
        # Make a test request
        client.get_podcasts()
        
        # Verify the Authorization header was sent
        mock_session.get.assert_called_once()
        
        # Verify headers
        assert mock_session.headers.get('Authorization') == f"Token token={test_key}"
