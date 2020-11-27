from django.db import models
from user.models import is_loggedin , get_user_id

# Create your models here.

def is_admin(request, handle):
    """
        authenticate admin, if username == 'admin'
    """
    if(is_loggedin(request=request)==True):
        if(handle=='admin'):
            return True
        else:
            return False



