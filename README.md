# About this app

This is just a simple flask app I wrote for the purposes of intercepting requests from smoke tests and printing them. It's a quick and dumb way to find out what request body andy/or headers are being sent from tests without setting up the associated service(s).

# How to use it

Create a virtual environment, activate it, then install the requirements.

Then, simply run `python app.py`

You may need to update your `/etc/hosts` file with an entry depending on the service you are hoping to intercept.

Once the hosts file has been updated and the server is running, run your tests like this:

`ENV_FOR_DYNACONF=smoke iqe tests plugin <plugin_name>`

