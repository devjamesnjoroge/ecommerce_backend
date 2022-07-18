init:
	python manage.py runserver
m-migrate:
	python manage.py makemigrations
migrate:
	python manage.py migrate
shell:
	python manage.py shell
check:
	python manage.py check
test:
	python manage.py test
admin:
	python manage.py createsuperuser
heroku-migrate:
	heroku run python manage.py migrate