# imdbrestapi


1.first create virtualenvironment then activate it.

Windows:
##python -m venv env
##env\scripts\activate


2.pip install -r requirements.txt

3.python server.py

4.login page username:admin password:password


If you want to do from scratch

step 1:
make imdb.db

1.sqlite3 imdb.db
2.CREATE TABLE MOVIES(ID INTEGER PRIMARY KEY,TITLE TEXT,RATING NUMBER,RELEASEDATE TEXT,DURATION TEXT,DESCRIPTION TEXT);

exit

step 2:

python task.py

it will take time to scrap data from https://www.imdb.com/chart/top?ref_=nv_mv_250

nearly 5 minutes to scrap and store data in imdb.db

step 3:
python tablelogin.py

sqlite3 tablelogin.db
INSERT INTO user(username,password) VALUES('admin','password');

step 4:
python server.py

