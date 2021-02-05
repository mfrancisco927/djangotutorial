#!/bin/bash

rm -f db.sqlite3 recommender/migrations/0*.py recommender/migrations/__pycache__/0*.pyc
python manage.py migrate recommender zero && python manage.py makemigrations && python manage.py migrate

echo "*********************************************"
echo "If needed, now create super user and insert data into database"

