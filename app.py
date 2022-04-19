import os
from flask import (Flask, flash, render_template,
                    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
from datetime import datetime
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL")
app.config['MAIL_PASSWORD'] = os.environ.get("EMAIL_KEY")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route("/")
@app.route("/home")
def load_homepage():
    """
    Loads the home page upon starting app
    """
    return render_template("home.html")


@app.route("/profile_tasks/<username>/<sort_by>", methods=["GET", "POST"])
def profile_tasks(username, sort_by):
    """
    Bounce back to login screen is no session user
    Gets list of tasks from MongoDB
    Loads profile data of session user
    Converts tasks to list to iterate multiple times (flask)
    """
    if session.get("user") == None:
        return render_template(
            "login.html")

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    character = mongo.db.users.find_one(
        {"username": session["user"]})["character"]
    tasks = mongo.db.tasks.find(
        {"created_by": session["user"]}).sort(sort_by)
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
    exp = mongo.db.users.find_one(
        {"username": session["user"]})["exp"]
    claimed = mongo.db.users.find_one(
        {"username": session["user"]})["claimed_amount"]
    defeated = mongo.db.users.find_one(
        {"username": session["user"]})["defeated"]

    # Convert tasks into a list for flask multiple for loops
    tasks = list(tasks)

    if session["user"]:
        return render_template(
            "profile_tasks.html", tasks=tasks,
            username=username, character=character,
            level=level, strength=strength,
            stamina=stamina, intellect=intellect,
            skill=skill, social=social,
            active_tasks = active_tasks,
            finished_tasks = finished_tasks,
            urgent_tasks = urgent_tasks, exp = exp,
            claimed = claimed, defeated = defeated)

    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Gets info from registrarion form
    Creates and adds 1 user + 1 task to MongoDB
    Checks if username already exists
    Generates hashed password
    Redirects to tasks page
    """
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
            "social": 1,
            "defeated": 0,
            "defeat_list": "",
            "exp": 0,
            "total_exp": 0,
            "complete_tasks": 0,
            "urgent_completed": 0,
            "claimed_list": "",
            "claimed_amount": 0
        }

        tutorial_task = {
            "task_name": "your first quest",
            "task_description": """Welcome to taskventure! This is a quest. 
            You can create more by clicking 'new quest' above. Quests provide two 
            things - stat increases and experience. Increasing your stats will 
            allow you to fight stronger monsters, and gaining 500 experience (EXP) 
            will level your character up. Completing quests, fighting monsters 
            and finding treasures will all provide experience. This particular 
            quest will increase your strength stat (indicated by the sword icon). 
            Collect treasures by meeting certain requirements and turn your to-do 
            list into a fun adventure!""",
            "is_urgent": "off",
            "due_date": "2023-12-31",
            "stat_increase": 'strength',
            "created_by": request.form.get("username").lower(),
            "is_completed": "no",
            "date_created": datetime.now()
        }

        # Add new user, task to MongoDB
        mongo.db.users.insert_one(register)
        mongo.db.tasks.insert_one(tutorial_task)

        # Add new user to session cookie
        session["user"] = request.form.get("username").lower()
        flash("Beginning quest...")
        return redirect(url_for("profile_tasks", username=session["user"], sort_by='due_date'))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Checks existence of name in MongoDB
    Check hashed password for match
    Ambiguous incorrect user/password flash
    Redirect to profile / login
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile_tasks", username=session["user"], sort_by='due_date'))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/create_task", methods=["GET", "POST"])
def create_task():
    """
    Retreive profile information
    Get info from HTML form
    Insert into tasks database
    """
    if session.get("user") == None:
        return render_template(
            "login.html")

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
    exp = mongo.db.users.find_one(
        {"username": session["user"]})["exp"]
    claimed = mongo.db.users.find_one(
        {"username": session["user"]})["claimed_amount"]
    defeated = mongo.db.users.find_one(
        {"username": session["user"]})["defeated"]

    if session["user"]:
        if request.method == "POST":
            is_urgent = "on" if request.form.get("is_urgent") else "off"
            task = {
                "task_name": request.form.get("task_name").lower(),
                "task_description": request.form.get("task_description"),
                "is_urgent": is_urgent,
                "due_date": request.form.get("due_date"),
                "stat_increase": request.form.get("stat_increase"),
                "created_by": session["user"],
                "is_completed": "no",
                "date_created": datetime.now()
            }
            mongo.db.tasks.insert_one(task)
            flash("New Quest Added")
            return redirect(url_for(
                        "profile_tasks", username=session["user"], sort_by='due_date'))

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
                                urgent_tasks = urgent_tasks,
                                exp = exp,
                                claimed = claimed,
                                defeated = defeated)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    """
    Gets the task ID from the clicked task
    Loads that ID info into form
    Updates existing task via _id number
    """
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})

    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task_edit = {"$set": {
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "stat_increase": request.form.get("stat_increase"),
            "created_by": session["user"],
            "is_completed": "no"
            }}

        mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, task_edit)
        flash("Quest Updated")
        return redirect(url_for("profile_tasks", username=session["user"], sort_by='due_date'))

    return render_template("edit_task.html", task=task)


@app.route("/profile_battle/<username>", methods=["GET", "POST"])
def profile_battle(username):
    """
    Loads profile info
    Loads monster info from enemies database
    """
    if session.get("user") == None:
        return render_template(
            "login.html")
    
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
    exp = mongo.db.users.find_one(
        {"username": session["user"]})["exp"]
    claimed = mongo.db.users.find_one(
        {"username": session["user"]})["claimed_amount"]
    defeated = mongo.db.users.find_one(
        {"username": session["user"]})["defeated"]

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
            enemies = enemies, defeat_list = defeat_list,
            exp = exp, claimed = claimed, defeated = defeated)

    return redirect(url_for("login"))


@app.route("/battle_enemy/<enemy>")
def battle_enemy(enemy):
    """
    Loads and compares info from user and enemy
    Checks if player stat is greater than requirement
    Either awards player with upgrade & EXP, or
    notifys that enemy is too strong.
    """
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
        # used to list enemy as defeated or not in HTML
        defeat_list = mongo.db.users.find_one(
            {"username": session["user"]})["defeat_list"]
        mongo.db.users.update_one(
            {"username": session["user"]},
            {"$set": {"defeat_list": defeat_list + " " + enemy}})
        # incremenrt relevant user details
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {str(player_stat): int(1)},
                "$currentDate": {"lastModified": True}},)
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"exp": int(150)},
                "$currentDate": {"lastModified": True}},)
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"total_exp": int(150)},
                "$currentDate": {"lastModified": True}},)
        # check if EXO is over 500, if so reduce to 0 and add remainder
        total_exp = int(mongo.db.users.find_one(
            {"username": session["user"]})["exp"])

        if total_exp >= 500:
            flash("Level Up!")
            mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"level": int(1)},
                "$currentDate": {"lastModified": True}},)
            leftover_exp = total_exp - 500
            mongo.db.users.update_one(
            {"username": session["user"]}, {"$set": {"exp": int(leftover_exp)},
                "$currentDate": {"lastModified": True}},)

    elif player_stat < enemy_level:
        flash("Enemy Too Powerful...")

    return redirect(url_for(
                    "profile_battle", username=session["user"]))


@app.route("/profile_treasures/<username>", methods=["GET", "POST"])
def profile_treasures(username):
    """
    Get profile info
    Get treasures info
    """
    if session.get("user") == None:
        return render_template(
            "login.html")

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
    exp = mongo.db.users.find_one(
        {"username": session["user"]})["exp"]
    treasures = mongo.db.treasures.find().sort("level")
    claimed_list = mongo.db.users.find_one(
        {"username": session["user"]})["claimed_list"]
    claimed = mongo.db.users.find_one(
        {"username": session["user"]})["claimed_amount"]
    defeated = mongo.db.users.find_one(
        {"username": session["user"]})["defeated"]
    # Check no. of active tasks for certain requirements
    active_tasks = mongo.db.tasks.count_documents(
        {"created_by": username, "is_completed": "no"})
    mongo.db.users.update_one(
            {"username": session["user"]},
            {"$set": {"active_tasks": int(active_tasks)}})

    if session["user"]:
        return render_template(
            "profile_treasures.html", tasks=tasks,
            username=username, character=character,
            level=level, strength=strength,
            stamina=stamina, intellect=intellect,
            skill=skill, social=social,
            active_tasks = active_tasks,
            finished_tasks = finished_tasks,
            urgent_tasks = urgent_tasks,
            enemies = enemies, defeat_list = defeat_list,
            exp = exp, treasures = treasures,
            claimed_list = claimed_list,
            claimed = claimed, defeated = defeated)

    return redirect(url_for("login"))


@app.route("/claim_treasure/<treasure>")
def claim_treasure(treasure):
    """
    Compare player info and treasure requirement,
    then reward or re-load accordingly.
    """
    treasure_requirement = mongo.db.treasures.find_one(
        {"name": treasure})["requirement"]
    player_stat = mongo.db.users.find_one(
        {"username": session["user"]})[treasure_requirement]
    treasure_level = mongo.db.treasures.find_one(
        {"name": treasure})["level"]
    if player_stat >= treasure_level:
        flash("Treasure Climed!")
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"claimed_amount": int(1)},
            "$currentDate": {"lastModified": True}},)
        claimed_list = mongo.db.users.find_one(
            {"username": session["user"]})["claimed_list"]
        mongo.db.users.update_one(
            {"username": session["user"]},
            {"$set": {"claimed_list": claimed_list + " " + treasure}})

        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"exp": int(75)},
                "$currentDate": {"lastModified": True}},)
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"total_exp": int(75)},
                "$currentDate": {"lastModified": True}},)

        total_exp = int(mongo.db.users.find_one(
            {"username": session["user"]})["exp"])

        if total_exp >= 500:
            flash("Level Up!")
            mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"level": int(1)},
                "$currentDate": {"lastModified": True}},)
            leftover_exp = total_exp - 500
            mongo.db.users.update_one(
            {"username": session["user"]}, {"$set": {"exp": int(leftover_exp)},
                "$currentDate": {"lastModified": True}},)

    elif player_stat < treasure_level:
        flash("Cannot yet claim...")

    return redirect(url_for(
                    "profile_treasures", username=session["user"]))



@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    """
    Removes task from document library
    """
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash("Quest Abandoned")
    return redirect(url_for(
                    "profile_tasks", username=session["user"], sort_by='due_date'))


@app.route("/complete_task/<task_id>")
def complete_task(task_id):
    """
    Set finished task as 'complete'
    Award user with EXP increase
    Award more EXP if task is urgent
    Check EXP for limit and reset accordingly
    """
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
    mongo.db.users.update_one(
        {"username": session["user"]}, {"$inc": {"exp": int(100)},
            "$currentDate": {"lastModified": True}},)
    mongo.db.users.update_one(
        {"username": session["user"]}, {"$inc": {"total_exp": int(100)},
            "$currentDate": {"lastModified": True}},)
    mongo.db.users.update_one(
        {"username": session["user"]}, {"$inc": {"complete_tasks": int(1)},
            "$currentDate": {"lastModified": True}},)
    
    is_urgent = mongo.db.tasks.find_one({"_id": completed_task})["is_urgent"]

    if is_urgent == "on":
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"urgent_completed": int(1)},
                "$currentDate": {"lastModified": True}},)
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"exp": int(50)},
                "$currentDate": {"lastModified": True}},)
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$inc": {"total_exp": int(50)},
                "$currentDate": {"lastModified": True}},)

    total_exp = int(mongo.db.users.find_one(
        {"username": session["user"]})["exp"])

    if total_exp >= 500:
        flash("Level Up!")
        mongo.db.users.update_one(
        {"username": session["user"]}, {"$inc": {"level": int(1)},
            "$currentDate": {"lastModified": True}},)
        leftover_exp = total_exp - 500
        mongo.db.users.update_one(
            {"username": session["user"]}, {"$set": {"exp": int(leftover_exp)},
                "$currentDate": {"lastModified": True}},)

    flash("Quest Completed, " + stat + " increased!")
    return redirect(url_for(
                    "profile_tasks", username=session["user"], sort_by='due_date'))


@app.route("/leaderboard")
def leaderboard():
    """
    Get user list and sort by level
    """
    users = mongo.db.users.find().sort("level", -1)
    return render_template("leaderboard.html", users=users)


@app.route("/about")
def about():
    """
    Load 'about' page
    """
    return render_template("about.html")


@app.route("/contact", methods=("GET", "POST"))
def contact():
    """
    Flask Mail used here
    Get info from HTML form
    Use variables set above to use the mail send function
    """
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        msg = Message(sender = name, recipients = ['os.environ.get("EMAIL")'])
        msg.body = message
        mail.send(msg)
        flash("Email Sent")
    return render_template("contact.html")


@app.route("/logout")
def logout():
    """
    Remove session user cookie and redirect to home
    """
    flash("Logged Out")
    session.pop("user")
    return redirect(url_for("load_homepage"))


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Loads profile info for page refresh
    Searches a pre-made index in MongoDB
    """
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find(
        {"created_by": session["user"], "$text": {"$search": query}}))
    
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
    exp = mongo.db.users.find_one(
        {"username": session["user"]})["exp"]
    claimed = mongo.db.users.find_one(
        {"username": session["user"]})["claimed_amount"]
    defeated = mongo.db.users.find_one(
        {"username": session["user"]})["defeated"]

    if session["user"]:
        return render_template(
            "profile_tasks.html", tasks=tasks,
            username=username, character=character,
            level=level, strength=strength,
            stamina=stamina, intellect=intellect,
            skill=skill, social=social,
            active_tasks = active_tasks,
            finished_tasks = finished_tasks,
            urgent_tasks = urgent_tasks, exp = exp,
            claimed = claimed, defeated = defeated)

    return redirect(url_for(
                    "profile_tasks", username=session["user"], sort_by='due_date'))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# Update debug to false when finished!
