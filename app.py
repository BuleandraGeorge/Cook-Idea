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
    

@app.route("/find_recipes")
def display_recipes():
    name=request.form.get['search_name']
    zones=request.form.get['zones']
    types=request.form.get['types']
    vegan=request.form.get['vegan']
    return render_template('recipe_list.html', recipes=mongo.db.recipes.find({"name":name,
                                                                              "country":zones,
                                                                              "type":types,
                                                                              "vegan":vegan}))


@app.route('/add_recipe.html')
def add_recipe():
    return render_template('add_recipe.html')


@app.route('/like/<rep_id>')
def like(rep_id):
    recipes=mongo.db.recipes
    recipe = recipes.find_one({'_id': ObjectId(rep_id)})
    value= int(recipe['rating'][0])
    value+=1
    value=str(value)
    recipes.update_one({'_id': ObjectId(rep_id)},
    { '$set':{
                'rating.0' : value
            }   
    })
    return redirect(url_for('get_recipes'))

@app.route('/dislike/<rep_id>')
def dislike(rep_id):
    recipes=mongo.db.recipes
    recipe = recipes.find_one({'_id': ObjectId(rep_id)})
    value= int(recipe['rating'][0])
    value+=1
    value=str(value)
    recipes.update_one({'_id': ObjectId(rep_id)},
    { '$set':{
                'rating.1' : value
            }   
    })
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)