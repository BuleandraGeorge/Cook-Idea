import os
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


def update_lists(the_list, new_elements):
        exist = 1
        for x in the_list:
            for y in new_elements:
                if x != y:
                    the_list.append(y)
                    exist = 0
        the_list.sort()
        return [the_list, exist]


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
    name = request.form.get('search-name')
    return render_template('recipes_list.html', recipes=mongo.db.recipes.find({name: name}))


@app.route('/#modal1/<rep_id')
def modal():
    recipe = mongo.db.recipes.find_one('_id': ObjectId(rep_id))
    return render_template('recipe_details_modal.html', recipe=recipe)


@app.route('/edit_recipe.html/<rep_id>')
def edit(rep_id):
    recipes = mongo.db.recipes
    recipe = recipes.find_one({'_id': ObjectId(rep_id)})
    return render_template('edit_recipe.html', recipe=recipe)


@app.route('/upload/<rep_id>', methods=["POST", "GET"])
def upload(rep_id):
    recipes = mongo.db.recipes
    countries = mongo.db.country
    types = mongo.db.dish_types
    if request.method == "POST":
        recipe_name = request.form.get("rep_name")
        recipe_country = request.form.getlist("rep_country")
        recipe_type = request.form.getlist("rep_type")
        recipe_vegan = request.form.get("rep_vegan")
        recipe_description = request.form.get("rep_description")
        recipe_url = request.form.get("rep_url")
        recipe_tools = request.form.getlist("rep_tool")
        recipe_igd = request.form.getlist("rep_igd")
        recipe_steps = request.form.getlist("rep_step")
        recipe_author = request.form.get("rep_author")
        recipe_source = request.form.get('rep_source')
        time = datetime.now()
        date = time.strftime("%d/%m/%Y")
        recipes.update_one({"_id": ObjectId(rep_id)},
                    { 
                        '$set':{
                        "name": recipe_name,
                        "description": recipe_description,
                        "tools": recipe_tools,
                        "ingredients": recipe_igd,
                        "steps": recipe_steps,
                        "country": ('any', recipe_country),
                        "types": ('any',recipe_type),
                        "vegan": recipe_vegan,
                        "rating": ["0", "0"],
                        "url": recipe_url,
                        "author": recipe_author,
                        "upload_date": date,
                        "source": recipe_source
                        }
                 })
        new_list = update_lists(countries.zones, recipe_country)
        if new_list[1] == 0:
            countries.update_one({'_id': ObjectId(countries._id)},
                        {'$set': {
                                'zone' : new_list[0]
                                }
                        }) 

        new_list = update_lists(types.rep_type, recipe_type)
        if new_list[1] == 0:
            types.update_one({'_id': ObjectId(types._id)},
                    {'$set': {
                                'rep_type': new_list[0]
                            }
                    })

        return redirect(url_for('get_recipes'))


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
    recipes = mongo.db.recipes
    recipe = recipes.find_one({'_id': ObjectId(rep_id)})
    value = int(recipe['rating'][0])
    value += 1
    value = str(value)
    recipes.update_one({'_id': ObjectId(rep_id)},
    {'$set': {
                'rating.1' : value
            }   
    })
    return redirect(url_for('get_recipes'))


@app.route("/add_recipe", methods=["POST", "GET"])
def add():
    countries = mongo.db.country
    types = mongo.db.dish_types
    if request.method == "POST":
        recipe_name = request.form.get("rep_name")
        recipe_country = request.form.getlist("rep_country")
        recipe_type = request.form.getlist("rep_type")
        recipe_vegan = request.form.get("rep_vegan")
        recipe_description = request.form.get("rep_description")
        recipe_url = request.form.get("rep_url")
        recipe_tools = request.form.getlist("rep_tool")
        recipe_igd = request.form.getlist("rep_igd")
        recipe_steps = request.form.getlist("rep_step")
        recipe_author = request.form.get("rep_author")
        recipe_source = request.form.get('rep_source')
        time = datetime.now()
        date = time.strftime("%d/%m/%Y")
        new_recipe= {
                    "name" : recipe_name,
                    "description": recipe_description,
                    "tools": recipe_tools,
                    "ingredients": recipe_igd,
                    "steps": recipe_steps,
                    "country": ('any', recipe_country),
                    "types": ('any', recipe_type),
                    "vegan": recipe_vegan,
                    "rating": ["0", "0"],
                    "url": recipe_url,
                    "author": recipe_author,
                    "upload_date": date,
                    "source": recipe_source
                }
        recipes = mongo.db.recipes
        recipes.insert_one(new_recipe)
        new_list = update_lists(countries.zones, recipe_country)
        if new_list[1] == 0:
            countries.update_one({'_id': ObjectId(countries._id)},
                    {'$set': {
                             'zone' : new_list[0]
                            }
                    }) 
                
        new_list = update_lists(types.rep_type, recipe_type)
        if new_list[1] == 0:
            types.update_one({'_id': ObjectId(types._id)},
                    {'$set': {
                        'rep_type' : new_list[0]
                            }
                    })
                            
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)