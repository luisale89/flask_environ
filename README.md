# flask environment for API Development

WELCOME GEEK! 🐍 + 💻 = 🤓

The following commands are available to run your code:

- pipenv run init: create migrations folder.
- pipenv run migrate: create database migrations (if models.py is edited)
- pipenv run upgrade: run database migrations (if pending)
- pipenv run start: start flask web server (if not running)

On new projects, yo need to remeber:

- create a copy of .env.example file in root folder, and change the name of that copy to .env
- create database in mysql, and set the URI inside .env file
- run migrations commands to create new schema.
- start coding