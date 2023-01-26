from flask import Flask, request, Response
from flask_cors import cross_origin, CORS
from login_client import login
from admin_client import add_user, remove_user
from python.schemas.LoginSchema import LoginSchema
from python.schemas.AddUserSchema import AddUserSchema
import json
from marshmallow.exceptions import ValidationError

app = Flask(__name__)
# This cors is essentially stating that they can make GET, POST, or DELETE calls
# From any origin, and with Authorization and Content-Type headers
admin_cors = {
    "origins": ["*"],
    "methods": ["POST", "DELETE"],
    "allow_headers": ["Authorization", "Content-Type"]
}

generic_cors = {
    "origins": ["*"],
    "methods": ["GET", "POST"],
    "allow_headers": ["Authorization", "Content-Type", "Access-Control-Allow-Origin"]
}


@app.route("/api/generic/login", methods=["GET"])
@cross_origin(**generic_cors)
def login_api():
    # Converting parameters to dictionary for consinstency
    data = {
        "username": request.args.get('username'),
        "password": request.args.get('password')
    }
    try:
        # Validate against the LoginSchema
        validate = LoginSchema().load(data)
    except Exception as e:
        # If it isn't valid, return why and a 400 code
        return Response(json.dumps({"error": str(e)}, status=400))
    result = login(data)
    # Message will return "valid": True or "valid": False if it's good, but if it threw an error
    # It will return "error": error_message
    object = ""
    if result.object != "":
        json.loads(result.object)
    response = Response(
        json.dumps({"user" if result.object else "error": result.error if result.error else object}),
        status=result.status_code)
    return response


@app.route("/api/admin/add_user", methods=["POST"])
@cross_origin(**admin_cors)
def add_user_api():
    info = request.get_json()
    try:
        # Validate against AddUserSchema
        validate = AddUserSchema().load(info)
    except ValidationError as v:
        # For prettier errors, I extracted into a list and appended to it
        errors = []
        for i in v.messages.values():
            errors.append(i[0])
        # This only works for Validation Errors, but it's essentially identical to the next except clause
        return Response(json.dumps({"errors": errors}), status=400)
    except Exception as e:
        # Generic error returns 400 code
        return Response(json.dumps({"errors": str(e)}), status=400)
    result = add_user(info)
    # This response returns "message": message unless there is an error in which case it is
    # "error" error
    return Response(
        json.dumps({"message" if result.message else "error": result.message if result.message else result.error}),
        status=result.status_code)


@app.route("/api/admin/remove_user", methods=["DELETE"])
@cross_origin(**admin_cors)
def remove_user_api():
    info = request.get_json()
    result = remove_user(info)
    # This response returns "message": message unless there is an error in which case it is
    # "error" error
    return Response(
        json.dumps({"message" if result.message else "error": result.message if result.message else result.error}),
        status=result.status_code)


@app.route("/api/generic/check", methods=["GET"])
@cross_origin(**generic_cors)
def check():
    # An easy way to see if the API is visible to others
    return "check successful"


def main():
    app.run(host='0.0.0.0', port=8000)


if __name__ == "__main__":
    main()
# This is what everyone else sees
# http://136.34.239.66:8001/check
