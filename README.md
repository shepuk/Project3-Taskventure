# Taskventure

Taskventure is an RPG inspired task-tracking app powered by Flask & MongoDB. Track quests, choose a hero, battle enemies and collect treasures.

### Visit the website

[View the live project here.](https://taskventure.herokuapp.com/)

### Backend Project

Built with backend technilogy in mind, Taskventure utilises primarilly Python, Flask and MongoDB, along with several other packages outlined in the [technologies](#technologies) section below.

### Primary Objectives

 - Design and implement a backend for a web application using Python and a micro-framework.
 - Model and manage data.
 - Query and manipulate data.
 - Deploy to a cloud platform.
 - Identify and apply security features.

### Early ideas & goals

 - Design and build a task-tracking app with a deep set of additional features.
 - Implement database CRUD functionality into the design.
 - Design a databse in which fields can be compared against each other. 
 - Create a varied & fun experience with longevity in mind.
 - The content should be justified, accessible, responsive and presented logically.

 ### Screenshots
The hero section of the homepage, displaying responsively in different browser sizes. A hamburger-style menu is offered at tablet-sized screens and below. 
![amiresponsive screenshot](/static/images/screenshots/screenshot_responsive.png)

The main quests page - showing the current list of active and completed tasks below a full profile summary. Full CRUD functionality can be complerted from here - add, delete, and edit tasks. Doing so will provide various rewards to the player. Users can search and filter tasks with the tools provided above the quest list.
![1080 profile screenshot](/static/images/screenshots/screenshot_tasks_1080.png)

Still within the profile area of the app, users can use the blue tabs to navigate. This screenshot shows the new quest form below the profile information. Upon completion, a new quest is added to the database and users are redirected to the tasks page where they will find their newly created entry.
![1080 create task screenshot](/static/images/screenshots/screenshot_create_1080.png)

From the profile area, users can battle enemies or collect treasures. These are both presented in a grid-view made with Bulma columns. Colours clearly indicate wheather a user has defeated an enemy or not, and the same functionality extends to the treasures list. This is all kept track of via PyMongo & MongoDB on the backend.
![1080 enemies page screenshot](/static/images/screenshots/screenshot_enemies_1080.png)

When signing up, users are presented with a simple form and choice of hero to represent them. Retro pixel art is used throughout and credited below. These tiny images are scaled up and use the CSS `image-rendering: pixelated;` style to keep their crisp edges and maintain a retro feel to the website.
![register screenshot](/static/images/screenshots/screenshot_register.png)

All pages are designed with mobile in mind and scale well. Columns stack on smaller screens and a hamber-style menu is offered. All information and features are still available at smaller screen sizes.
![mobile tasks screenshot](/static/images/screenshots/screenshot_tasks_mobile.png)
![mobile gtreasures screenshot](/static/images/screenshots/screenshot_treasures_mobile.png)
![mobile leaderboard screenshot](/static/images/screenshots/screenshot_leaderboard.png)


 ### User Experience
- #### Target Audience
    - Taskventure is available and accessible to everyone, with an emphesis on users with an interest in fictional fantasy-sytle content. As a simple task-tracking app, Taskventure has a full set of features to allow anyone to track any kind of activities. Furthermore, it incorporates a deep user-progression system and allows users to increase their character's abilities and attributes in a variety of ways, appealing to fans of high-fantasy literature or RPG videogames, for example.

- #### User Stories
    - 'As a  typical user, I want to track and organise tasks and projects'
    - 'As a fan of fantasy, I want features based around my interests'
    - 'As an advanced user, I want to sort, search and track my tasks easily'
    - 'As an inexperienced user, I need simple navigation and controls with clear feedback'
    - 'As a typical user, I want to compete with my friends when using the app'

- #### New Visitors
    - App should be clear in it's intent, and designed around user-friendliness.
    - Clear feedback for user interaction is important.

- #### Returning Visitors
    - Content should be easilly and quickly accessible.
    - User information such as profile data should be displayed clearly and quickly.


### Design
- #### Colours
    - Primarily a backend-focussed project, I wanted to utilise a standard BulmaCSS palette when building the app. This ensures good contrast and complimentary colour choice. With a lot of colourful pixel art in use, a light background colour allows the art to stand out.
    ![colour palette](/static/images/screenshots/taskventure_colours.png)

- #### Typography
    - Along with built-in BulmaCSS font styling, Google Fonts Averia Serif Libre was used for titles, headings and logos. This font is fantasy-esque and fits the subject matter well.
    ![Averia Libre font](/static/images/screenshots/screenshot_font.png)

- #### Imagery
    - content

- #### Accessibility
    - content

### Wireframes
    - Early design descisions were made using wireframes. I was able to stick to the inidial wireframe designs closely and only minor changes were made. For example, more information was added to the profile section as ideas were expanded upon, and the new quest form was ultimately created with a more stacked, vertical design.
![wireframe](/static/images/screenshots/wireframe_task_view.png)
![wireframe](/static/images/screenshots/wireframe_create_task.png)
![wireframe](/static/images/screenshots/wireframe_enemy_treasure_view.png)
![wireframe](/static/images/screenshots/wireframe_mobile.png)


### Features

### Security
    - Werkzeug was used for user authentication and provided secure pashword hashing for new signups or logging in.
    - Session user cookies are used to grant access to profile areas, and profile links are removed from navigation if the cookie is not present.
    - Environmental variables are included in a .gitingore file to prevent any sensitive data being publicly available.

### Technologies
- [Python](https://www.python.org/) was the primary backend language used.
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) framework was used to build the project.
- [MongoDB](https://www.mongodb.com/) held database information for users, profiles, tasks, enemies and treasures.
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) allowed interaction with the MongoDB database from within Python.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.1.x/) provided secure login authentication and password hashing.
- [Flask Mail](https://pythonhosted.org/Flask-Mail/) provides functionality to the contact page of the app.
- [JavaScript](https://www.javascript.com/) was used to offer some interactivity to various Bulma CSS elements.
- [jQueryUI](https://jquery.com/) was used for the calendar widget.
- [Bulma CSS](https://bulma.io/) components were used throughout the app for their attractive and easy implementation.
- [HTML](https://en.wikipedia.org/wiki/HTML) formed the structure of the site and also included significant Jinja templating
- [Font Awesome](https://fontawesome.com/) provided some icons throughout the site.
- [Google Fonts](https://fonts.google.com/) provided the use of the Averia Libre font.
- [Git](https://git-scm.com/) was used via the terminal for version control.
- [Github](https://github.com/) was used to host and store the project files.
- [Heroku](https://dashboard.heroku.com/login) is used to host the app.
- [Gitpod](https://gitpod.io/workspaces) was my primary IDE during project development.
- [AmIResponsive](http://ami.responsivedesign.is/)
- [Figma](https://www.figma.com/) was used during the design phase for wireframes and flowcharts.

### Testing
- #### Primary Objectives

- #### Early ideas & goals

- #### Target Audience

- #### User Stories

- #### Testing the code
 - Validators were used for all deployed code.
    - [PEP8 Online](http://pep8online.com/)
    - [JSLint](https://www.jslint.com/)
    - [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

### Bugs & Issues
- #### Resolved bug examples

- #### Known bug examples

## Setup, Backups & Depoyment
[Gitpod](https://www.gitpod.io/) was used as my primary IDE.
A template was provided by Code Institute which I cloned for my project repository.
Opening the repository in Gitpod is made simple thanks to a [Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki).

Git / Github were used for file versioning and hosting.
`$ git add -A` was used initially to add my files and folders to the staging area, followed by git `$ commit -m "commit message"` and `$ git push` to add everything to my Github repository. These three commands allow me to commit changes and upload new code to Github. Git commits were used often, for any changes, new features or big fixes.

The Github repository was linked to Heroku for hosting and teasting early in development. After an issue with Github/Heroku connections due to security issues outside of my control, Github functionality was removed from Heroku. Using the Heroku CLI, I was able to continue to upload code to the Heroku hosting service. with the following commands;
`$ heroku login` (use Heroku login credentials here)
`$ git add .`
`$ git commit -am "Heroku commit message"`
`$ git push heroku main`

### Credits

#### Specific Cases

#### Documentation & Online Help
- [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/column-count)
- [W3 Schools](https://www.w3schools.com/)

#### Media
- [Open Game Art](https://opengameart.org/content/dungeon-crawl-32x32-tiles) for user avatars, enemy sprites and treasure sprites.
- [Kyrise](https://kyrise.itch.io/kyrises-free-16x16-rpg-icon-pack) for character stat icons.
- [From Software](https://en.bandainamcoent.eu/elden-ring/elden-ring) for use of their public screenshot of the game 'Elden Ring'.

#### Content
All content was written by me.

#### Acknowledgements
Code Institute & Newcastle College for their support.