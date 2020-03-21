# flask environment for API Development

WELCOME GEEK! 🐍 + 💻 = 🤓
The following commands are available to run your code:
- \033[94m$ pipenv run init\033[0m create migrations folder.
- \033[94m$ pipenv run migrate\033[0m create database migrations (if models.py is edited)
- \033[94m$ pipenv run upgrade\033[0m run database migrations (if pending)
- \033[94m$ pipenv run start\033[0m start flask web server (if not running)

On new projects, yo need to remeber:

- change .env.example file's name to: .env
- create database in mysql, and set the name of the database URI inside .env file
- run migrations commands to create new schema.