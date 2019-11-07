from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import pandas as pd
db_connect = create_engine('sqlite:///imdb.db')
app = Flask(__name__)
api = Api(app)


class Movies(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("SELECT * FROM MOVIES; ")  # This line performs query and returns json result
        return {'movies': [i[1] for i in query.cursor.fetchall()]}  # Fetches first column that is Employee ID




class Movies_Name(Resource):
    def get(self, ID):
        conn = db_connect.connect()
        query = conn.execute("select * from MOVIES where ID =%d " %int(ID))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

class sortbyname(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from MOVIES ORDER BY TITLE ASC")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

class sortbyrating(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from MOVIES ORDER BY RATING DESC")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

class sortbyrd(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from MOVIES ORDER BY RELEASEDATE ASC")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

class sortbyduration(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from MOVIES ORDER BY DURATION ASC")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)




class Search(Resource):
    def get(self, data):
        conn = db_connect.connect()
        query = conn.execute("select * from MOVIES where TITLE OR DESCRIPTION LIKE ? ",("%"+data+"%",))
        #sql="""select * from MOVIES where TITLE LIKE '%'+{}+'%'""".format(data)
        #newquery=pd.read_sql_query(sql,conn)
        #print(newquery)
        print("hello")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)
api.add_resource(Movies, '/movies')  # Route_1

api.add_resource(Movies_Name, '/movies/<ID>')  # Route_3
api.add_resource(sortbyname,'/sortbyname')
api.add_resource(sortbyrating,'/sortbyrating')
api.add_resource(sortbyduration,'/sortbyduration')
api.add_resource(Search, '/search/<data>')
if __name__ == '__main__':
    app.run(debug="true")