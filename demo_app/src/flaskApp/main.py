import logging
import os

import flask
from flask import request

from flaskApp.logger import setup_logger

app = flask.Flask(__name__)

LOGGER = logging.getLogger("demo-app")
VIEWS = 0


def get_user(username):
    """Mock of the database connect."""
    users = {
        "user1": "John Smith",
        "user2": "James Smith",
        "user3": "Mary Smith"
    }
    full_name = users.get(username)
    if full_name is None:
        raise Exception('User not found')
    else:
        return full_name


# application status
@app.route("/")
def hello():
    LOGGER.debug("Displaying the main page")
    return "Hello World!"


@app.route("/health")
def health():
    LOGGER.debug("health check")
    return "I am OK"


# visualization demo
@app.route('/views')
def views():
    global VIEWS
    VIEWS += 1
    LOGGER.info(
        "Displaying the views page",
        extra={
            "views": VIEWS,
            "user_agent": request.headers['User-Agent']
        }
    )
    return "Views count: {}".format(VIEWS)


# troubleshooting demo
@app.route("/replicas")
def replicas():
    return "Hello from: {}".format(os.getenv("HOSTNAME", "unknown"))


@app.route('/user/<username>')
def user_profile(username):
    try:
        full_name = get_user(username)
    except Exception:
        LOGGER.exception("Can't get user")
        flask.abort(404)
    LOGGER.debug("Displaying user page")
    return "User: {}".format(full_name)


def main():
    setup_logger()
    LOGGER.info("Demo app is running.")
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
