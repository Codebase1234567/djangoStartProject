import django.urls
import os
import sys


from models import School
from django.core.exceptions import ValidationError

try:
     s = School(state="enugu",principal="me",phonenumber="0707")
     s.full_clean()
except ValidationError as e:
     print(e.message_dict)



file_path = django.urls.__file__
dir= os.path.dirname(file_path)
#x=dir(django.urls)
print(dir)