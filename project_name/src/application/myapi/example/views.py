from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from myapi.extensions import apispec
from flask_jwt_extended import jwt_required



blueprint = Blueprint("example", __name__, url_prefix="/example")
example = Api(blueprint)


@blueprint.route("/hello_world", methods=["POST"])
def hello_world():
    """Hello world msg

    ---
    post:
      tags:
        - example
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Hello world!
        400:
          description: bad request
      security: []
    """

    ret = {"message": "Hello world!"}

    return jsonify(ret), 200



@blueprint.before_app_first_request
def register_views():
    apispec.spec.path(view=hello_world, app=current_app)


