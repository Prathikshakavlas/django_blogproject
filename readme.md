#create project & app
django-admin startproject blogproject
cd blogproject
python manage.py startapp blogapp

#install dependencies
pip install -r requirements.txt

#runmigrations
python manage.py makemigrations
python manage.py migrate

#runserver
python manage.py runserver

#testing
python manage.py test


#API Endpoints
POST /api/posts/ - Create a new post.
GET /api/posts/ - List all posts.
GET /api/posts/<id>/ - Retrieve a post by ID.
PUT /api/posts/<id>/ - Update a post by ID.
DELETE /api/posts/<id>/ - Delete a post by ID.
POST /api/posts/<post_id>/comments/ - Create a new comment on a post.
GET /api/posts/<post_id>/comments/ - List all comments on a post.
POST /api/token/ - Obtain a new token.
POST /api/token/refresh/ - Refresh a token.

