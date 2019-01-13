from django.test import TestCase


class TestDjango(TestCase): # Trivial initial test. 
    
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)
        
        