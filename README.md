# imdbrestapi


1.first create virtualenvironment then activate it.

Windows:
## python -m venv env
## env\scripts\activate


2.pip install -r requirements.txt


3.python server.py

4.login page username:admin password:password


# If you want to do from scratch

Delete logindata.db and imdb.db

## step 1.first create virtualenvironment then activate it.

Windows:
##python -m venv env
##env\scripts\activate


## step 2.pip install -r requirements.txt


## step 3.make imdb.db

1.sqlite3 imdb.db
2.CREATE TABLE MOVIES(ID INTEGER PRIMARY KEY,TITLE TEXT,RATING NUMBER,RELEASEDATE TEXT,DURATION TEXT,DESCRIPTION TEXT);



## step 4.python task.py

it will take time to scrap data from https://www.imdb.com/chart/top?ref_=nv_mv_250

nearly 5 minutes to scrap and store data in imdb.db


## step 5.python tablelogin.py

1.sqlite3 logindata.db
2.CREATE TABLE users(id INTEGER PRIMARY KEY,username TEXT,password TEXT);
3.INSERT INTO users(username,password) VALUES('admin','password');

## step 6.python server.py

