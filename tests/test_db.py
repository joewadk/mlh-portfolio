import unittest
from peewee import *
from app import TimelinePost
from playhouse.shortcuts import model_to_dict

MODELS = [TimelinePost]

# Use in-memory SQLite database for testing
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    """Unit tests for TimelinePost model using an in-memory SQLite database."""
    def setUp(self):
        # Bind model to test database and create tables before each test
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)
    def tearDown(self):
        # Drop tables and close connection after each test
        test_db.drop_tables(MODELS)
        test_db.close()
    def test_timeline_post(self):
        """Test creating TimelinePost records and their IDs."""
        # Create first post and check its ID
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        # Create second post and check its ID
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
    def test_timeline_get(self):
        """Test retrieving TimelinePost records."""
        # Create two posts
        first_post = model_to_dict(TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!'))
        second_post = model_to_dict(TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!'))
        # Retrieve all posts 
        all_posts = [model_to_dict(post) for post in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
        assert len(all_posts) != 0 
        assert first_post in all_posts  
        assert second_post in all_posts  