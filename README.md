# Flask Todo Application
The entire backend is being powered by Python. I decided to do this project as challenge, for a company that I have intentions in applying too. Took me about *3-4 days* to create a simple application with the usage of user authentication, database, and CRUD operation.


# Things to implement

Definetevely there are a lot of things that I still need to implement in the application, I've been spending about 2 days in breaking up my folder structure in MVC pattern

**Original Structure**
```
| - app.py
| - model.py
| - route.py
| - form.py
| - database.db
| - config.py
| - custom_class/
|    - XP.py
| - template/
|   | - base/
|       - base.html
|   | - dashboard/
|       - create.html
|       - hiscore.html
|       - list.html
|       - complete.html
|    - index.html
|    - login.html
|    - signup.html
| - static/
|   | - img/
|   | - js/
|   | - lib/
|   | - css/
```
The major issue with this design layout I had was my logic was being mixed with the modes, controllers, views and etc... It was getting a mess, at my `app.py`, so I decided to break down the components something more duabable.

**New Structure**
```
| - app.py
| - database.db
| - config.py
| - route.py
| - models/
|    - __init__.py
|    - user.py
|    - task.py
|    - experience.py
|    - experience_table.py
| - controllers/
|    - __init__.py
|    - task_controller.py
|    - experience_controller.py
| - forms/
|    - __init__.py
|    - login_form.py
|    - register_form.py
|    - task_form.py
| - templates/
|   | - base/
|       - base.html
|   | - dashboard/
|       - create.html
|       - hiscore.html
|       - list.html
|       - complete.html
|    - index.html
|    - login.html
|    - signup.html
| - static/
|   | - img/
|   | - js/
|   | - lib/
|   | - css/
```
I am still working on the new logic for my web application. I am trying to make a MVC pattern, which is easier to scale in future. I am planning to expand and make it RESTful, therefore my `route.py` will be split into: `view.py` and `api.py` and be registered in `Blueprint`.