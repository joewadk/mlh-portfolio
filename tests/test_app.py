import unittest
import os

os.environ['TESTING'] = 'true'

from app import app 

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Jawad Kabir" in html
        assert "MLH Fellow | Software Developer" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "posts" in json

        #just tests for inital empty timeline
        assert isinstance(json["posts"], list)
        assert len(json["posts"]) == 0

        post_response = self.client.post("/api/timeline", data={
            "name": "Test User",
            "email": "test@example.com",
            "content": "Test content!"
        })
        assert post_response.status_code == 200 #check if post was successful


        get_response = self.client.get("/api/timeline") 
        assert get_response.status_code == 200 #check if get was successful
        json2 = get_response.get_json()
        assert len(json2["posts"]) == 1 #check post
        post = json2["posts"][0] #should only be one post
        assert post["name"] == "Test User"
        assert post["email"] == "test@example.com"
        assert post["content"] == "Test content!"

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline", data={
            "email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline", data={
            "name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline", data={
            "name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html



if __name__ == "__main__":
    unittest.main()
