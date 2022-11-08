# blog_api

## Installation
   First clone the repository, using this command
   > git clone https://github.com/bolexs/blog_api.git

  cd into blog
  > cd blog

  Create your virtualenv
  > virtualenv venv

  Activate it using this command for mac and linux users
  > source venv/bin/activate

  For windows users
  > venv/Scripts/activate

  Then install the requirements needed for the project using 
  > pip install -r requirements.txt


## Deployment and Testing

To test the endpoints(POST,GET,PATCH AND DELETE), you can use postman. Firstly run the server by using this command

> python manage.py runserver

and going to the specified address 

>127.0.0.1:8000/posts to create new post using the post endpoint

>127.0.0.1:8000/post/pk to get/patch or delete


