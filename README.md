## Deplyment ##

The steps are the same as deploying a python/Django webapp

`
# Install virtualenv an pip
sudo apt-get install virtualenv python-pip
 
virtualenv venv/
source venv/bin/activate

# Install Django and other project dependencies
pip install -r requirements.txt

# Might want to change the DB configurations as per 
# https://docs.djangoproject.com/en/1.10/ref/databases/
python manage.py migrate

# Import the database file

# Fire up the dev web server
python manage.py runserver

`

Hosted at https://treebodeals.herokuapp.com/