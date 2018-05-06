# Introduction

- Polls is a simple Django app for conducting web based polls created in Django.

- It provides basic features like creating ,reading, updating and deleting the questions and choices.

- For each question, visitors can choose between a fixed number of answers/choices.



# Contents

1. [Introduction][intro]
2. [Usage][usage]
3. [Installation][inst]
  1. [Requirements][req]
  2. [Installation][install]
  3. [Configuration][conf]
4. [Technologies used][tech]
5. [Contributing][contr]
6. [Contact][cont]
7. [License][lic]



# Usage
 -  The web app provides a simple easy to use interface for a polls .
 -  New questions and choices can be added using the input textbox at admin interface . 

# Installation

## Requirements
As this is a Django app, you will need a few things pre-installed and pre-configured on your system.

1. Python (Version: 3.5.x)
2. Django (Version: 1.10+)
3. Postgres or MySQL or any other database server (if you wish to use those, or else you are good to go with the Django default SQLite)

## Installation
#### Step 1.
Before you install this app, you need to make sure that you have Python installed on your system, particularly Python 3.5+.
To install Python, go to the [Official Python Website][python] to download the latest version of Python.

#### Step 2.

After you are set up with Python, you need to make sure you have pip installed.

Open your command window, and enter `pip -V`

It should display the version of pip that is installed on your system. If it shows an error, then that means that pip is not installed on your system.

To install pip checkout the documentation at [Python Packaging User Guide Documentation][PPUGD].

#### Step 3.

Now you need to install Django Framework. This is what provides the backend for the polls app.

To install Django, open your command window, and enter `pip install django==1.10` to install the version used for this app.
But you can also install the latest version by just `pip install django`. Although, I cannot guarantee whether the latest version will support the web app.

## Configuration

#### Step 1.

After installing Django, you just have to create a new project, using `django-admin startproject projectname`

This will create a new directory called 'projectname' in the current working directory.

#### Step 2.

Now copy the 'polls' directory from the git project and paste it inside the 'projectname' directory.

#### Step 3.

Now let's create a route so that the app can be visited through a web browser.

Add the following line inside the URL_PATTERNS list in 'projectname/urls.py' file

```python

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    # other routes...
]
```

This ensures that the web app can be visited via 'baseurl/polls/'.

#### Step 4.

Now to register the app with the Django project, open the 'settings.py' file from the 'projectname' directory, and add 'polls' inside the INSTALLED_APPS list as such:

```python
# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    # ...
    'django.contrib.admin',
    # other apps
]
```
#### Step 5.

After we have registered Django project, we need to migrate the database. This will create the necessary tables in the database.

```shell
$ django-admin makemigrations 
        or 
$ python manage.py runserver

$ django-admin migrate
     or
$ python manage.py migrate
```

#### Step 6.
Create a superuser for admin interface 


```shell
$ python manage.py createsuperuser 

Username (leave blank to use 'defaultname') :
Email address:
Password:
Password (again):

```

#### Step 7.

The app is finally ready to roll !!!

Just enter the following command in the command line to start the server.

```shell
$ django-admin runserver 
        or
$ python manage.py runserver         

```
You can create the polls via the link after admin login with superuser credentials

```
`http://127.0.0.1:8000/admin/polls/question`

```

You can view the polls via the link 
```
`http://127.0.0.1:8000/polls/`

```

# Technologies Used

- **Backend**: Python Django Framework 1.10
- **Database**: PostgreSQL or SQLite (Other Database engines, like MySQL, MongoDB, etc. can also be used)

# Contributing

This app was meant as a basic follow up tutorial for Django. I just wanted to see how it works out. One can find possibly many flaws in it. Or even missing features.
If you like this project and would like to contribute to it, you can do so by following a few basic steps:

1. Fork this repository
2. Clone it locally to your system
3. Create a new branch for your patch or feature
4. Add your code/patch
5. Commit your work, and write good/unambiguous commit messages
6. Push it to your origin repository
7. Create a Pull Request for your patch/feature
8. Respond to any code review/comments feedback

# Contact
For any queries or , you can contact me via:
- Gmail: [jha.sudhanshu1991@gmail.com][gmail]


# License

This project is licensed under the terms of the [MIT][lic] license.


[intro]: #introduction
[usage]: #usage
[inst]: #installation
[req]: #requirements
[install]: #installation-1
[conf]: #configuration
[tech]: #technologies-used
[contr]: #contributing
[cont]: #contact
[lic]: #license
[python]: https://www.python.org/downloads/
[PPUGD]: https://packaging.python.org/installing/#install-pip-setuptools-and-wheel
[lic]: https://github.com/sudhanshu-jha/django-polls/blob/master/LICENSE.txt
[gmail]:(mailto:jha.sudhanshu1991@gmail.com)














