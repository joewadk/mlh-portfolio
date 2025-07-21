import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client for the Flask app
        self.client = app.test_client()
        
    def test_home(self):
        """Test the home page loads and contains expected content."""
        response = self.client.get("/")
        assert response.status_code == 200  # Home page should load successfully
        html = response.get_data(as_text=True)
        # Check HTML content
        assert '<h1 class="profile-title">Jawad Kabir</h1>' in html
        assert '<p class="profile-role">MLH Fellow | Software Developer</p>' in html
    
    def test_timeline(self):
        """Test timeline API and HTML endpoints for posting and retrieving timeline posts."""
        # Test GET req: should start empty
        response = self.client.get("/api/timeline")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "posts" in json
        assert len(json["posts"]) == 0
        # Test client POST req: add a timeline post
        post_response = self.client.post("/api/timeline", data = {
            "name" : "John",
            "email" : "john@example.com",
            "content" : "Hello world"
        })  
        assert post_response.status_code == 200 
        assert post_response.is_json
        json = post_response.get_json()
        assert json["name"] == "John"  # Response should contain the posted name
        # Test client GET req: should now have one post
        get_response = self.client.get("/api/timeline")
        assert get_response.status_code == 200
        assert get_response.is_json
        json = get_response.get_json()
        assert len(json["posts"]) == 1
        assert json["posts"][0]["name"] == "John"
        # Test html endpoint
        html_response = self.client.get("/timeline")
        assert html_response.status_code == 200
        html = html_response.get_data(as_text=True)
        assert "No posts yet. Be the first to post!" in html
        
    def test_malformed_timeline_post(self):
        """Test posting malformed data to the timeline API returns appropriate errors."""
        # POST request missing name 
        response = self.client.post("/api/timeline", data = {
            "email" : "john@example.com",
            "content" : "Hello world, I'm John!"
        })
        assert response.status_code == 400  
        html = response.get_data(as_text=True)
        assert "Invalid name" in html
        
        # POST request with empty content 
        response = self.client.post("/api/timeline", data = {
            "name" : "John Doe",
            "email" : "john@example.com",
            "content" : ""
        })
        assert response.status_code == 400  
        html = response.get_data(as_text=True)
        assert "Invalid content" in html
        
        # POST request with malformed email 
        response = self.client.post("/api/timeline", data = {
            "name" : "John Doe",
            "email" : "not-an-email"
        })
        assert response.status_code == 400  
        html = response.get_data(as_text=True)
        assert "Invalid email" in html