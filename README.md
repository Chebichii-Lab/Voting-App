# A-Poll Voting App

## Author
Natasha Serem

### Description
A-Poll is a full featured polling app. You have to register in this app to show the polls and to vote. If you already voted you can not vote again. Only the owner of a poll can add poll , edit poll, update poll, delete poll , add choice, update choice, delete choice and end a poll. If a poll is ended it can not be voted. Ended poll only shows user the final result of the poll.

### Setup and Installations
To get the code, clone the repository:   https://github.com/Chebichii-Lab/Voting-App.git
And run the following commands;

    $ cd Voting-App
    $ pip install -r requirements.txt

### Installing and activate virtual environment

    $ python3.8 -m venv virtual
    $ source virtual/bin/activate

### Create database

    $ psql
    $ CREATE DATABASE (name_of_databse);

### Make Migrations

    $ python3.8 manage.py check
    $ python3.8 manage.py makemigrations (app_name)
    $ python3.8 manage.py migrate 

### Testing the Application

    $ python3.8 manage.py test (app_name)

### Running the application

    $python3.8 manage.py runserver

Then once you are done, open your browser with the local host; 127.0.0.1:8000

## Dependencies
1. python3.8
2. Django 3.2.5
3. Virtual environment
4. Heroku
5. Heroku

### Technologies used
1. python 3.8.10
2. HTML
3. Django 3.2.5
4. Bootstrap 3
5. Heroku
6. Postgresql


