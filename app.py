import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_idea_db'
app.config["MONGO_URI"] = 'mongodb+srv://chief_user:cookpass@cookbook-zwtc4.mongodb.net/cook_idea_db?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_receipes')
def get_receipes():
    return render_template('receipes_list.html', receipes=mongo.db.receipes.find())
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)