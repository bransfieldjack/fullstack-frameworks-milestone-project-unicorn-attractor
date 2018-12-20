from django.contrib.auth.models import User


class EmailAuth:   # Authenticates a user by an exact match of their email and password. 
    
    def authenticate(self, username=None, password=None):   # Gets an instance of user based on email, verifies the password. 
    
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):   # Check the password for the username. 
                return user
            return None
            
        except User.DoesNotExist:   # Do nothing if the user doesnt exist already. 
            return None
        
    def get_user(self, user_id):    # Retrieves an instance of user.
            
        try:
            user = User.objects.get(pk=user_id) # Get the user from the user id. 
                
            if user.is_active: 
                return user
            return None
            
        except User.DoesNotExist:
            return None
                
                