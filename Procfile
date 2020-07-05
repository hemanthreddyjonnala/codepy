release: python manage.py migrate
web: gunicorn agrofarming.wsgi --timeout 3000 --log-file -