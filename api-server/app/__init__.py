# coding=utf-8

from flask import Flask, Response, json

app = Flask(__name__)


from app.controllers.addr_controller import addr_controller
app.register_blueprint(addr_controller)


from app import constants


@app.route("/")
def hello():
    return "Hello Api!"


@app.errorhandler(404)
def page_not_found(e):
    result = {
        'status_code': constants.CODE_404
        , 'status_msg': constants.MSG_404
    }

    return Response(json.dumps(result),  mimetype=constants.MIME_TYPE_APPLICATION_JSON)


@app.errorhandler(500)
def internal_server_error(e):
    result = {
        'status_code': constants.CODE_500
        , 'status_msg': constants.MSG_500
    }

    return Response(json.dumps(result),  mimetype=constants.MIME_TYPE_APPLICATION_JSON)


# @app.errorhandler(Exception)
# def unhandled_exception(e):
#     result = {
#         'status_code': constants.CODE_500
#         , 'status_msg': constants.MSG_500
#     }
#
#     return Response(json.dumps(result),  mimetype=constants.MIME_TYPE_APPLICATION_JSON)
