release: python manage.py migrate
web: python project/manage.py collectstatic --noinput;
gunicorn social_networking.wsgi