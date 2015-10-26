
# Description
* The easiest way to access our app is to go to http://gentle-gorge-7175.herokuapp.com/.  The app is being hosted online.
* This is a Django app that has similar functionality to Stack Overflow, allowing users to ask questions, answer questions, and vote on answers.
* This was built by Bob Amand, Andrew Pierce, and Will Butts
* Core data was generated randomly.

## Building the Database

* First run $ pip install -r requirements.txt.
* You will need to have a PostgreSQL server running.  For details on getting it set up check https://github.com/tiyd-python-2015-08/course-resources/blob/master/week7/PostgreSQL-and-Django.md
* For info on the PostgresSQL information check settings.py
* Run python manage.py makemigrations
* Run python manage.py migrate to setup the database
* Run python manage.py generate_data.
* Run python manage.py loaddata box/fixtures/questions.json box/fixtures/answers.json box/fixtures/tags.json
* Run python manage.py link_tags
* Run python manage.py runserver and go to localhost:8000 in a browser to see the database.
