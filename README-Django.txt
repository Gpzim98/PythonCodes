* 1 -
# Minimum Django Script
import sys
import traceback
import os

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

def main():
    pass

if __name__ == "__main__":
    main()
    
    
* 2 - 
# Include one path in python path

sys.path.append("/etc/myfolder/")

* 3 - Response DRF dictionary
from rest_framework.response import Response

                return Response({'errors': 'There was problem to generate the proposal',
                                 'null_before_values': True},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
