from django.test import TestCase
from .forms import UserLoginForm, UserProfileForm


class TestUserLoginForm(TestCase):
    
    def test_UserLoginForm(self):   # Test user login functionality. 
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        
    def test_UserLoginForm_validation(self):    # Form validation testing. 
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
  