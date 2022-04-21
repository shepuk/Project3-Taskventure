# Taskventure

Taskventure is an RPG inspired task-tracking app powered by Flask & MongoDB. Track quests, choose a hero, battle enemies and collect treasures.

![amiresponsive screenshot](/static/images/screenshots/screenshot_responsive.png)

- [Contents](#taskventure)
    + [Objectives](#backend-project)
    + [Screenshots](#screenshots)
    + [User Experience](#user-experience)
    + [Design](#design)
    + [Wireframes](#wireframes)
    + [Features](#features)
    + [Security](#security)
    + [Technologies](#technologies)
    + [Testing](#testing)
    + [Bugs & Issues](#bugs---issues)
    + [Setup, Backups & Deployment](#setup--backups---deployment)
    + [Credits](#credits)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

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

The main quests page - showing the current list of active and completed tasks below a full profile summary. Full CRUD functionality can be complerted from here - add, delete, and edit tasks. Doing so will provide various rewards to the player. Users can search and filter tasks with the tools provided above the quest list.
![1080 profile screenshot](/static/images/screenshots/screenshot_create_1080.png)

Still within the profile area of the app, users can use the blue tabs to navigate. This screenshot shows the new quest form below the profile information. Upon completion, a new quest is added to the database and users are redirected to the tasks page where they will find their newly created entry.
![1080 create task screenshot](/static/images/screenshots/screenshot_tasks_1080.png)

From the profile area, users can battle enemies or collect treasures. These are both presented in a grid-view made with Bulma columns. Colours clearly indicate wheather a user has defeated an enemy or not, and the same functionality extends to the treasures list. This is all kept track of via PyMongo & MongoDB on the backend.
![1080 enemies page screenshot](/static/images/screenshots/screenshot_enemies_1080.png)

When signing up, users are presented with a simple form and choice of hero to represent them. Retro pixel art is used throughout and credited below. These tiny images are scaled up and use the CSS `image-rendering: pixelated;` style to keep their crisp edges and maintain a retro feel to the website.
![register screenshot](/static/images/screenshots/screenshot_register.png)

All pages are designed with mobile in mind and scale well. Columns stack on smaller screens and a hamburger-style menu is offered. All information and features are still available at smaller screen sizes.
[Mobile / small screen screenshots](https://github.com/shepuk/Project3-Taskventure/tree/main/static/images/screenshots/mobile_screenshots)


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
    - 32x32 retro-style sprites were used throughout the design to provide a nostalgic fantasy feel. These were scaled up for modern screens and retained their pixel designs with CSS. Without this, images appear blurry and stretched.

![wireframe](/static/images/characters/1.png) ![wireframe](/static/images/characters/2.png) ![wireframe](/static/images/characters/3.png) ![wireframe](/static/images/characters/4.png) ![wireframe](/static/images/characters/5.png) ![wireframe](/static/images/characters/6.png) ![wireframe](/static/images/characters/7.png) ![wireframe](/static/images/characters/8.png) ![wireframe](/static/images/characters/9.png) ![wireframe](/static/images/characters/10.png)

- #### Accessibility
    - All images have a descriptive `alt` attribute.
    - Contract is high throughout the website and all text is clearly readable.
    - All forms utilise a `label` tag.
    - Headings and paragraphs are used appropriately.
    - Semantic markup is used throughout the website.
    - Tables are used in place of divs where appropriate.
    - Clear flash messages are shown at the top of the screen and offer feedback for interaction.

- #### Database Design
    - I began designing my databases by identifying the categories which would need their own collection. After scoping out the project size and deciding on a final set of features, I was able to recognise 4 main categories - users, tasks, enemies & treasures. 
        1. **Users** would contain the most information. Login details, charater stats, experience, total experience, defeated enemies and more. In total, 18 key:value pairs. This would allow me to a) display rich and detailed profie information, and b) provide a diverse set of requirements to fulfil for enemy battles and treasures.
        2. **Tasks** would contain all relevant information to make a task detailed and trackable. Name and description are a good start, and due dates, urgency, category & creation date would all allow for deeper tracking and sorting.
        3. **Enemies** are fairly simple, and contain a name, level and requirement. The name allows an img to be linked to the database entry and level and requirement are check as the user arttempts to battle. To check if a user has already defeated an enemy, the enemies name is taken as a string and concatenated onto the players 'defeat_list' key. When loading the enemies page, a check is made to see if the enemy name is included at any point in the 'defeat_list'.
        4. **Treasures** are handled the same way as enemies, and check if the players requirement matches the treasure level before the player can claim.


- ### Wireframes
    - Early design descisions were made using wireframes. I was able to stick to the inidial wireframe designs closely and only minor changes were made. For example, more information was added to the profile section as ideas were expanded upon, and the new quest form was ultimately created with a more stacked, vertical design.
[Wireframe Screenshots](https://github.com/shepuk/Project3-Taskventure/tree/main/static/images/screenshots/wireframes)

- ### Flow diagram
    - A flow diagram was also created early on, to help structure the flow of the app. [See it here](https://github.com/shepuk/Project3-Taskventure/blob/main/static/images/screenshots/screenshot_flowchart.png)


### Features
- #### Current features
    - Deep MongoDB integration used for task tracking, user account stats, and enemy / treasure interaction logging.
    - Designed with scaleability in mind - database can be expanded and receive new features easily quickly.
    - Rich user profiles with several tracked player counters and attributes.
    - Deep task-tracking features, along with search and sorting features. Users can sort by date, urgency and more.
    - Experience tracking and logic - checks if user is over the 500 EXP limit, and if they are, reset to zero, gain a level and add any remmaining EXP.
    - Multiple CRUD operations performed during task completion, editing, monster battling or treasure collecting.
    - Clear user feedback in the form of Flask flash messaging.
    - Secure login/register process with password hashing.
    - Functional contact page writted with Flask Mail and Python.
    - Enemy and Treasure progress handled efficiently in the user's database entry with a small amout of code.
    - Defensive features built in with regards to deleting databse entries in particular.
    - Register process performs database checks for existing usernames, to avoid clashes.

- #### Features to implement
    - (Planned) include a greater roster of enemies/treasures for increased longevity.
    - All completed tasks are displayed currently - introduce pagination to limit this.


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
 1. Design and implement a backend for a web application using Python and a micro-framework.
    - I have successfully designed and deployed the above with Taskventure. Flask and Python power the logic and database maniplulation while MongoDB hosts all data which can be accessed by the code securely. 
 2. Model and manage data.
    - Although MongoDB uses a flat data model by design, I have implemented relational-like features which compare data/fields for player progression purposes. For example, when a user decides to challenge an enemy, the backend will check both player stat and enemy requirement values in order to reward or redirect. Data is managed well with several checks in place, to avoid matching username fields for example. Only relevant data is shown to each user on the frontend.
 3. Query and manipulate data.
    - **C** Create operations - registering new users, creating new quests
    - **R** Read operations - fetching profile information, fetching login details, checking if enemy/treasure has been defeated/claimed, checking if user meets enemy/treasure requirement, fetching current task data for edit page, fetching quest details, fetching leaderboard.
    - **U** Update operations - marking quests as complete, editing quests, updating user profile information (stats, level, experience, defeated list, treasure list, several other progress tracking fields).
    - **D** Delete operations - deleting quests
    - **QUERY** - searching quests (searches name and description fields), sorting quests by date, urgency, name, or due date
 4. Deploy to a cloud platform.
    - Final build was deployed to Heroku cloud platform.
 5. Identify and apply security features.
    - Outlined in [security](#security) section.

- #### Early ideas & goals
 1. Design and build a task-tracking app with a deep set of additional features.
    - Built a fully featured task app with significant additional functionality - a full and progressable user profile experience, alongside extra challengeg in the form of enemies to defeat and treasures to collect - each requiring a diverse set of user benchmarks to be hit. 
 2. Implement database CRUD functionality into the design.
    - Outlined in the above section
 3. Design a databse in which fields can be compared against each other. 
    - My intent was to build a progression system which would use and compare player data to other data and reward users with a feeling of atchievement and progress as they complete quests. This was achieved with several comparing functions which allowed players to progress their profile as their character grew stronger.
 4. Create a varied & fun experience with longevity in mind.
    - Taskventure provides several enjoyable interactions and and sense of addictive progression - key features of a fun experience. Longevity was in mind from the beginning, with no upper limit on character stats. Additionally, adding new enemies or treasures can be done with ease thanks to their lightweight database entries.
 5. The content should be justified, accessible, responsive and presented logically.
    - More detail in the [accessibility](#Accessibility) section. To expand slightly, Taskventure conforms to more several key accessibility guidelines; buttons are clear and coloured appropriately (ie. red for warning or info, blue/green for proceeding forward), `<article>` and `<section>` tags are used appropriately. The idea is justified and well thought-out for an audience which has little in the way of this kind of product. Using Bulma's components and build blocks, the design is presented in a logical way and information is easilly found.

- #### Target Audience
1. Taskventure is available and accessible to everyone, with an emphesis on users with an interest in fictional fantasy-sytle content.
    - The app does well in catering to a wide audience, while offering additional features which would draw in users interested in a product with a fantasy style. As outlines in the above sections, the site is hugely accessible to all users and provides a way to track activities and jobs etc. To cater to a fantasy and pop-culture audience, several key steps were taken: a retro pixel art style is reminiscent to classic fantasy-adventure tales and games. Character stat-building, as well as character selection, is integral to any well-known fantasy game and provides a role-playing element to the app. Less significant choices such as naming tasks 'quests', and welcoming the user with 'Greetings' is a small touch which adds to the fantasy style and caters to this audience.

- #### User Stories
1. 'As a  typical user, I want to track and organise tasks and projects'
    - The app allows for a positive task-tracking experiences and give great control in terms of tracking and sorting tasks. Multiple options are given to a new task, such as an urgent toggle, and a task type. Descriptions can be as in-depth as required and are clearly shown in a well presented way.
2. 'As a fan of fantasy, I want features based around my interests'
    - As mentioned in the above target audience section, a great deal of thought has went into creating the app based on the interests of fans of the fantasy genre. There is an ample amount of content which caters to this audience which makes the app an ideal choice for the target audience.
3. 'As an advanced user, I want to sort, search and track my tasks easily'
    - Search and sort features are easy to access and provide deep query functionality for active quests. Completed quests are also viewable, searchable and sorted when these controls.
4. 'As an inexperienced user, I need simple navigation and controls with clear feedback'
    - Conformant navbar and clear profile tabular navigation provide clear and unambiguous access too all areas of the website. Flash messaging provides clear feedback to the user upon user interaction.

- #### New Visitors
1. App should be clear in it's intent, and designed around user-friendliness.
    - A striking hero provides instant information to the user and shows the use and intent of the app. Accessibility was in mind during the website's design phase and confirms to all user accessibility guidelines. Upon registration, a tutorial task is generated to provide the user with instructions on how to use the website. An about page goes into more depth regarding the usage of the website.
2. Clear feedback for user interaction is important.
    - Defensive programming for deletions and flash messaging provide clear feelback at all times.

- #### Returning Visitors
1. Content should be easilly and quickly accessible.
    - Minimal navigation options and unintrusive design allows users to browse the app extremely quickly. Users are typically only one click away from any page in the app.
2. User information such as profile data should be displayed clearly and quickly.
    - After a quick sign-in process (or instant sign-in with session cookies) the user is redirected to their main task page. The important profile information is always displayed at the top of the page when interacting with the database for quick feedback.
3. As a returning user, I want to compete with my friends when using the app.
    - A leaderboard page has been included, listing player profiles and sorting by level.

- #### Manual Testing
    - Multiple browsers and devices were used to test the application.
    - The deployed website was also tested againt the development version to ensure everything worked as expected.
    - BrowserStack was used for their large variety of testing functionalty. I was able to test the app on over 50 devices including different OS, tablets and mobiles.
    - Modern browsers such as Chrome, Firefox and Edge display and load content as expected. Older browsers such as Internet Explorer are incompatible with large portions of the website, and are not reccomended. 
    - Mobile browsers handle styling and responsive design very well. Identical functionality to desktop/laptop screens.
    - Friends and family were utilised to test links, spelling, design and responsiveness.

- #### Testing the code
 - Validators were used for the deployed code.
    - [PEP8 Online](http://pep8online.com/) was used to make sure Python code was written to guidelines and falls within PEP8 compliancy. [See the PEP8 results here](https://github.com/shepuk/Project3-Taskventure/tree/main/static/images/screenshots/screenshot_pep8.jpg))

### Bugs & Issues
- #### Resolved bug examples
    - While testing the app line on a Heroku server, the browser would display error messages related to an insecure JavaScript file within my file directory. This was due to the .js file being issued over HTTP rather than HTTPS. The fix for this was to remove my {{Jinja2}} link in the script tag, and use a normal link to the file within my directory.
    - I ran into a couple of issues when implementing email in my app. While building and testing, the contact form would get stuck during the mail.send() function and display an abiguous error message. This was due to Gitpod blocking traffic on GMail's email ports. A smaller issue was discovered when testing on Heroku - when sending mail via SMTP, SSL was enabled but going through port 587. I had to change this to port 465 which is the SSL port number.
    - When implementing sort functionality to my quests page, I included sorting alphibetically. However, MongoDB has a known issue in which capitalisations are sorted with more priority than letters, meaning 'Z' would come before 'a' when sorting this was. A simple fix was to use the .lower() function when querying the database.
    - When using a for loop in an HTML document with Jinja, trying to use a second for loop on the same list will not work as Jinja essentiallyunpacks and emptied the list. This is because it's not actually a list, but a Mongo corsor object. A fix for this is to convert this object into a list with list(). However, this created more issues...
    - When adding the functionality to sort tasks, I would typically use the PyMongo sort() function. However, this will no longer work, because like I mentioned above, I converted the Mongo cursor object to a list which is not recognisable to the sort() function anymore. However, I still need it to be in list form for my double for loop. My fix for this was to pass through the sort_by option from the Jinja link throgh to the Python function. From there I could retrieve the tasks from MongoDB and pass in the sort_by option then, and finally convert the object to a list at the end of my function, so that it could be looped through twice by Jinja.

### Setup, Backups & Deployment
[Gitpod](https://www.gitpod.io/) was used as my primary IDE.
A template was provided by Code Institute which I cloned for my project repository.
Opening the repository in Gitpod is made simple thanks to a [Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki).

Git / Github were used for file versioning and hosting.
`$ git add -A` was used initially to add my files and folders to the staging area, followed by git `$ commit -m "commit message"` and `$ git push` to add everything to my Github repository. These three commands allow me to commit changes and upload new code to Github. Git commits were used often, for any changes, new features or bug fixes.

The Github repository was linked to Heroku for hosting and teasting early in development. After an issue with Github/Heroku connections due to security issues outside of my control, Github functionality was removed from Heroku. Using the Heroku CLI, I was able to continue to upload code to the Heroku hosting service with the following commands;
`$ heroku login` (use Heroku login credentials here)
`$ git add .`
`$ git commit -am "Heroku commit message"`
`$ git push heroku main`

### Credits

#### Specific Cases
- [StackOverflow - Help with JavaScript file being rejected by browser](https://stackoverflow.com/questions/37387711/page-loaded-over-https-but-requested-an-insecure-xmlhttprequest-endpoint)
- [StackOverflow - MongoDB sorting by capitalised instead of alphibetically](https://stackoverflow.com/questions/19855147/mongodb-returns-capitalized-strings-first-when-sorting)

#### Documentation & Online Help
- [Python Documentation](https://www.python.org/doc/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)
- [PyMongo Documentation](https://flask-pymongo.readthedocs.io/en/latest/)
- [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/column-count)
- [W3 Schools](https://www.w3schools.com/)

#### Media
- [Open Game Art](https://opengameart.org/content/dungeon-crawl-32x32-tiles) for user avatars, enemy sprites and treasure sprites.
- [Kyrise](https://kyrise.itch.io/kyrises-free-16x16-rpg-icon-pack) for character stat icons.
- [From Software](https://en.bandainamcoent.eu/elden-ring/elden-ring) for use of their public screenshot of the game 'Elden Ring'.

#### Content
All content was written by me.

#### Acknowledgements
Code Institute & Newcastle College.