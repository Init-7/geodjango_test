"""
WSGI config for geodjango_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ec2-user/env-staff/lib/python2.7/site-packages')
sys.path.append('/var/www/html/staff_est')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geodjango_test.settings-deploy")

application = get_wsgi_application()
