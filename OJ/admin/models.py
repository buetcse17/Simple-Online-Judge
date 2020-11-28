from django.db import models
from user.models import is_loggedin , get_user_id

# Create your models here.

def is_admin(handle):
    return handle == 'admin'


