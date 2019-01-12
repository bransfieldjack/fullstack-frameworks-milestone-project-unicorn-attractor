from django.test import TestCase    
from .models import Features, Comments


class TestFeatureModel(TestCase):
    
    def test_status_default_assigned(self):
        feature = Features(title="Test Feature 1")
        feature.save()
        self.assertEqual(feature.title, "Test Feature 1")
        self.assertEqual(feature.status, "assigned")
        
    def test_can_create_a_feature(self):
        feature = Features(name="Create a test", done=True)
        feature.save()
        self.assertEqual(feature.name, "Create a test")
        self.assertTrue(feature.done)