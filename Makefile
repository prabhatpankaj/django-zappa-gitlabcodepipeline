.PHONY: install migrate localrun productionrun
	
install:
	pip install --upgrade setuptools pip
	pip install -r requirements.txt

lmigrate:
	python manage.py makemigrations --settings=djangostarter.local
	python manage.py migrate --settings=djangostarter.local

pmigrate:
	python manage.py migrate --settings=djangostarter.production --noinput

lcollectstatic:
	python manage.py collectstatic --settings=djangostarter.local --noinput

pcollectstatic:
	python manage.py collectstatic --settings=djangostarter.production --noinput

localrun:
	python manage.py runserver 0.0.0.0:8080 --settings=djangostarter.local

productionrun:
	python manage.py runserver 0.0.0.0:8080 --settings=djangostarter.production