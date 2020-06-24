import os
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


def update_lists(the_list, new_elements):
    for x in new_elements:
        exist = 0
        x = x.lower()
        for y in the_list:
            if x == y:
                exist = 1
                break

        if exist == 0:
            x = x.lower()
            the_list.append(x)

    the_list = sorted(the_list)
    return the_list


def lowerList(the_list):
    for position in range(len(the_list)):
        the_list[position] = the_list[position].lower()

    return the_list

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook_idea_db'
app.config["MONGO_URI"] = 'mongodb+srv://chief_user:cookpass@cookbook-zwtc4.mongodb.net/cook_idea_db?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes_list.html', recipes=mongo.db.recipes.find(), zones=mongo.db.country.find(), types=mongo.db.dish_types.find())


@app.route("/find_recipes", methods=["POST", "GET"])
def display_recipes():
    rep_name = request.form.get("search_name").lower()
    rep_zone = request.form.getlist("zones")
    rep_type = request.form.getlist("types")
    rep_vegan = request.form.get("vegan_search")
    if not rep_zone:
        rep_zone.append("world wide")
    else:
        rep_zone = lowerList(rep_zone)


    if not rep_type:
        rep_type.append("any")
    else:
        rep_type = lowerList(rep_type)

    if not rep_vegan:
        rep_vegan = 'no'
    else:
        rep_vegan.lower()

    return render_template('recipes_list.html',
                            recipes=mongo.db.recipes.find(
                                {
                                    "name": {"$regex": rep_name},
                                    "country": {"$all": rep_zone},
                                    "types": {"$all": rep_type},
                                    "vegan": rep_vegan
                                })
                                , zones=mongo.db.country.find(), types=mongo.db.dish_types.find())


@app.route("/add_recipe")
def add_recipe():
    return render_template('add_recipe.html',zones=mongo.db.country.find(), types=mongo.db.dish_types.find())


@app.route("/recipe_details/<rep_id>")
def rep_details(rep_id):
    return render_template('recipe_details.html', recipe=mongo.db.recipes.find_one({'_id': ObjectId(rep_id)}))


@app.route("/insert_recipe", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        recipe_name = request.form.get("rep_name").lower()
        recipe_country = request.form.getlist("rep_country")
        recipe_type = request.form.getlist("rep_type")
        recipe_vegan = request.form.get("rep_vegan")
        recipe_country.append('world wide')
        recipe_type.append('any')
        if not recipe_vegan:
            recipe_vegan = 'no'
        recipe_description = request.form.get("rep_description").lower()
        recipe_url = request.form.get("rep_url")
        recipe_tools = request.form.getlist("rep_tool")
        recipe_tools = lowerList(recipe_tools)
        recipe_igd = request.form.getlist("rep_igd")
        recipe_igd = lowerList(recipe_igd)
        recipe_steps = request.form.getlist("rep_step")
        recipe_steps = lowerList(recipe_steps)
        recipe_author = request.form.get("rep_author").lower()
        recipe_source = request.form.get('rep_source').lower()
        time = datetime.now()
        date = time.strftime("%d/%m/%Y")
        new_recipe = {
                    "name": recipe_name,
                    "description": recipe_description,
                    "tools": recipe_tools,
                    "ingredients": recipe_igd,
                    "steps": recipe_steps,
                    "country": recipe_country,
                    "types": recipe_type,
                    "vegan": recipe_vegan,
                    "rating": ["0", "0"],
                    "url": recipe_url,
                    "author": recipe_author,
                    "upload_date": date,
                    "source": recipe_source
                }

        mongo.db.recipes.insert_one(new_recipe)
        coll_country = mongo.db.country
        countries = coll_country.find_one()['zone']
        new_list = update_lists(countries, recipe_country)
        coll_country.update_one({}, {
                '$set': {
                                'zone': new_list
                                }
                        })

        coll_dish_type =  mongo.db.dish_types               
        types = coll_dish_type.find_one()['rep_type']
        new_list = update_lists(types, recipe_type)
        coll_dish_type.update_one({}, {
                '$set': {
                                'rep_type': new_list
                            }
                    })

        return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<rep_id>')
def edit(rep_id):
    recipes = mongo.db.recipes
    recipe = recipes.find_one({'_id': ObjectId(rep_id)})
    return render_template('edit_recipe.html', recipe=recipe, zones=mongo.db.country.find(), types=mongo.db.dish_types.find())


@app.route('/upload/<rep_id>', methods=["POST", "GET"])
def upload(rep_id):
    recipes = mongo.db.recipes
    if request.method == "POST":
        recipe_name = request.form.get("rep_name").lower()
        recipe_country = request.form.getlist("rep_country")
        recipe_type = request.form.getlist("rep_type")
        recipe_vegan = request.form.get("rep_vegan")
        recipe_country.append('world wide')
        recipe_type.append('any')
        if not recipe_vegan:
            recipe_vegan = 'no'
        recipe_description = request.form.get("rep_description").lower()
        recipe_url = request.form.get("rep_url")
        recipe_tools = request.form.getlist("rep_tool")
        recipe_tools = lowerList(recipe_tools)
        recipe_igd = request.form.getlist("rep_igd")
        recipe_igd = lowerList(recipe_igd)
        recipe_steps = request.form.getlist("rep_step")
        recipe_steps = lowerList(recipe_steps)
        recipe_author = request.form.get("rep_author").lower()
        recipe_source = request.form.get('rep_source').lower()
        time = datetime.now()
        date = time.strftime("%d/%m/%Y")
        recipes.update_one({"_id": ObjectId(rep_id)}, {
                '$set': {
                        "name": recipe_name,
                        "description": recipe_description,
                        "tools": recipe_tools,
                        "ingredients": recipe_igd,
                        "steps": recipe_steps,
                        "country": recipe_country,
                        "types": recipe_type,
                        "vegan": recipe_vegan,
                        "rating": ["0", "0"],
                        "url": recipe_url,
                        "author": recipe_author,
                        "upload_date": date,
                        "source": recipe_source
                        }
                 })
        coll_country = mongo.db.country
        countries = coll_country.find_one()['zone']
        new_list = update_lists(countries, recipe_country)
        coll_country.update_one({}, {
                '$set': {
                                'zone': new_list
                                }
                        })

        coll_dish_type = mongo.db.dish_types
        types = coll_dish_type.find_one()['rep_type']
        new_list = update_lists(types, recipe_type)
        coll_dish_type.update_one({}, {
                '$set': {
                                'rep_type': new_list
                            }
                    })

    return redirect(url_for('get_recipes'))


@app.route('/like/<rep_id>')
def like(rep_id):
    recipes = mongo.db.recipes
    recipe = recipes.find_one({'_id': ObjectId(rep_id)})
    value = int(recipe['rating'][0])
    value += 1
    value = str(value)
    recipes.update_one({'_id': ObjectId(rep_id)}, {
        '$set': {
                'rating.0': value
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
    recipes.update_one({'_id': ObjectId(rep_id)}, {
        '$set': {
                    'rating.1': value
                }
    })
    return redirect(url_for('get_recipes'))


@app.route("/delete/<rep_id>")
def delete(rep_id):
    rep_coll = mongo.db.recipes
    rep_coll.delete_one({'_id': ObjectId(rep_id)})
    return redirect(url_for('get_recipes'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/comment', methods=["POST", "GET"])
def comment():
    coll_com = mongo.db.comments
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        comment = request.form.get('comment')
        new_comment = {
            "name": name,
            "email": email,
            "comment": comment
        }
        coll_com.insert_one(new_comment)
    return redirect(url_for('about'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
