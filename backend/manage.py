#!/usr/bin/env python
import os
import sys

import dotenv

if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.dev")
    
    dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    
    if os.getenv('DJANGO_SETTINGS_MODULE'):
        os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')
        print(os.getenv('DJANGO_SETTINGS_MODULE'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
