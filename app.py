import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_idea_db'
app.config["MONGO_URI"] = 'mongodb+srv://chief_user:cookpass@cookbook-zwtc4.mongodb.net/cook_idea_db?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes_list.html', recipes=mongo.db.recipes.find(),
     zones=mongo.db.country.find(), types=mongo.db.type.find())
    

@app.route('/add_recipe.html')
def add_recipe():
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)