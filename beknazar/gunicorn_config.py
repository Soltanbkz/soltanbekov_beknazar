command = '/root/code/project1/env/bin/gunicorn'
pythonpath = '/root/code/project1/soltanbekov_beknazar'
bind = '127.0.0.1:8001'
workers = 5
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=beknazar.settings'