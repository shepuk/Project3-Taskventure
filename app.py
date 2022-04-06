import os
from flask import (Flask, flash, render_template,
                    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def load_homepage():
    return render_template("home.html")


@app.route("/profile_tasks/<username>", methods=["GET", "POST"])
def profile_tasks(username):
    # Get the session user's username form the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    character = mongo.db.users.find_one(
        {"username": session["user"]})["character"]
    tasks = list(mongo.db.tasks.find(
        {"created_by": session["user"]}))
    level = mongo.db.users.find_one(
        {"username": session["user"]})["level"]
    strength = mongo.db.users.find_one(
        {"username": session["user"]})["strength"]
    stamina = mongo.db.users.find_one(
        {"username": session["user"]})["stamina"]
    intellect = mongo.db.users.find_one(
        {"username": session["user"]})["intellect"]
    skill = mongo.db.users.find_one(
        {"username": session["user"]})["skill"]
    social = mongo.db.users.find_one(
        {"username": session["user"]})["social"]
    active_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "no"})
    finished_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "yes"})
    urgent_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "no", "is_urgent": "on"})

    if session["user"]:
        return render_template(
            "profile_tasks.html", tasks=tasks,
            username=username, character=character,
            level=level, strength=strength,
            stamina=stamina, intellect=intellect,
            skill=skill, social=social,
            active_tasks = active_tasks,
            finished_tasks = finished_tasks,
            urgent_tasks = urgent_tasks)

    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_username = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_username:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "character": request.form.get("character"),
            "level": 1,
            "strength": 1,
            "stamina": 1,
            "intellect": 1,
            "skill": 1,
            "social": 1
        }
        # Add new user (dict) to MongoDB
        mongo.db.users.insert_one(register)

        # Add new user to session cookie
        session["user"] = request.form.get("username").lower()
        flash("Beginning quest...")
        return redirect(url_for("profile_tasks", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile_tasks", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/create_task", methods=["GET", "POST"])
def create_task():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    character = mongo.db.users.find_one(
        {"username": session["user"]})["character"]
    level = mongo.db.users.find_one(
        {"username": session["user"]})["level"]
    strength = mongo.db.users.find_one(
        {"username": session["user"]})["strength"]
    stamina = mongo.db.users.find_one(
        {"username": session["user"]})["stamina"]
    intellect = mongo.db.users.find_one(
        {"username": session["user"]})["intellect"]
    skill = mongo.db.users.find_one(
        {"username": session["user"]})["skill"]
    social = mongo.db.users.find_one(
        {"username": session["user"]})["social"]
    active_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "no"})
    finished_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "yes"})
    urgent_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "no", "is_urgent": "on"})
    
    if session["user"]:
        if request.method == "POST":
            is_urgent = "on" if request.form.get("is_urgent") else "off"
            task = {
                "task_name": request.form.get("task_name"),
                "task_description": request.form.get("task_description"),
                "is_urgent": is_urgent,
                "due_date": request.form.get("due_date"),
                "stat_increase": request.form.get("stat_increase"),
                "created_by": session["user"],
                #"task_level": request.form.get("task_level"),
                "is_completed": "no"
            }
            mongo.db.tasks.insert_one(task)
            flash("New Quest Added")
            return redirect(url_for(
                        "profile_tasks", username=session["user"]))

        return render_template("create_task.html",
                                username=username,
                                character=character,
                                level=level,
                                strength=strength,
                                stamina=stamina,
                                intellect=intellect,
                                skill=skill,
                                social=social,
                                active_tasks = active_tasks,
                                finished_tasks = finished_tasks,
                                urgent_tasks = urgent_tasks)


@app.route("/profile_battle/<username>", methods=["GET", "POST"])
def profile_battle(username):
    # Get the session user's username form the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    character = mongo.db.users.find_one(
        {"username": session["user"]})["character"]
    tasks = list(mongo.db.tasks.find(
        {"created_by": session["user"]}))
    level = mongo.db.users.find_one(
        {"username": session["user"]})["level"]
    strength = mongo.db.users.find_one(
        {"username": session["user"]})["strength"]
    stamina = mongo.db.users.find_one(
        {"username": session["user"]})["stamina"]
    intellect = mongo.db.users.find_one(
        {"username": session["user"]})["intellect"]
    skill = mongo.db.users.find_one(
        {"username": session["user"]})["skill"]
    social = mongo.db.users.find_one(
        {"username": session["user"]})["social"]
    active_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "no"})
    finished_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "yes"})
    urgent_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "no", "is_urgent": "on"})
    enemies = mongo.db.enemies.find().sort("level")
    defeat_list = mongo.db.users.find_one(
        {"username": session["user"]})["defeat_list"]

    if session["user"]:
        return render_template(
            "profile_battle.html", tasks=tasks,
            username=username, character=character,
            level=level, strength=strength,
            stamina=stamina, intellect=intellect,
            skill=skill, social=social,
            active_tasks = active_tasks,
            finished_tasks = finished_tasks,
            urgent_tasks = urgent_tasks,
            enemies = enemies, defeat_list = defeat_list)

    return redirect(url_for("login"))


@app.route("/battle_enemy/<enemy>")
def battle_enemy(enemy):
    enemy_stat = mongo.db.enemies.find_one(
        {"name": enemy})["attribute"]
    player_stat = mongo.db.users.find_one(
        {"username": session["user"]})[enemy_stat]
    enemy_level = mongo.db.enemies.find_one(
        {"name": enemy})["level"]
    if player_stat >= enemy_level:
        flash("Enemy Defeated!")
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"defeated": int(1)},
            "$currentDate": {"lastModified": True}},)
        defeat_list = mongo.db.users.find_one(
            {"username": session["user"]})["defeat_list"]
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$set": {"defeat_list": defeat_list + " " + enemy }})
        mongo.db.users.update_one(
        {"username": session["user"]}, {"$inc": {player_stat: int(1)},
            "$currentDate": {"lastModified": True}},)

    elif player_stat < enemy_level:
        flash("Enemy Too Powerful...")

    return redirect(url_for(
                    "profile_battle", username=session["user"]))


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    """ Removes task from document library """
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash("Quest Abandoned")
    return redirect(url_for(
                    "profile_tasks", username=session["user"]))


@app.route("/complete_task/<task_id>")
def complete_task(task_id):
    completed_task = ObjectId(task_id)
    # Mark as complete
    mongo.db.tasks.update_one(
        {"_id": completed_task}, {"$set": {"is_completed": "yes"},
            "$currentDate": {"lastModified": True}},)

    stat = mongo.db.tasks.find_one(
        {"_id": completed_task})["stat_increase"]
    mongo.db.users.update_one(
        {"username": session["user"]}, {"$inc": {stat: int(1)},
            "$currentDate": {"lastModified": True}},)
    flash("Quest Completed, " + stat + " increased!")
    return redirect(url_for(
                    "profile_tasks", username=session["user"]))


@app.route("/logout")
def logout():
    flash("Logged Out")
    session.pop("user")
    return redirect(url_for("load_homepage"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# Update debug to false when finished!
