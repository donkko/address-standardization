# -*- coding: utf-8 -*-

from flask import Blueprint, Response, request, json
from app import constants
from app.services.addr_service import AddrService


addr_controller = Blueprint('addr_controller', __name__)
addr_service = AddrService()


@addr_controller.route('/api/addr/standardize', methods=['GET'])
def standardize_address():

    addr = request.args.get('addr')
    if addr is None:
        result = {
            'status_code': constants.CODE_400
            , 'status_msg': constants.MSG_400
            , 'normalized_addr': ''
        }
    else:
        normalized_addr = addr_service.normalize(addr)
        result = {
            'status_code': constants.CODE_200
            , 'status_msg': constants.MSG_200
            , 'normalized_addr': normalized_addr
        }

    return Response(json.dumps(result), mimetype=constants.MIME_TYPE_APPLICATION_JSON)


# @addr_controller.route('/api/addr/analyze', methods=['GET'])
# def analyze_address():
#
#     something = addr_service.analyze()
#     result = {
#         'status_code': ''
#         , 'status_msg' : ''
#     }
#
#     return Response(json.dumps(result), mimetype=constants.MIME_TYPE_APPLICATION_JSON)
