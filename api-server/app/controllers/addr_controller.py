# coding=utf-8

from flask import Blueprint, Response, request, json

addr_controller = Blueprint('addr_controller', __name__)

from app import constants

from app.services.addr_service import AddrService
addr_service = AddrService()


@addr_controller.route('/api/addr/normalize', methods=['GET'])
def normalize_address():

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


@addr_controller.route('/api/addr/transform', methods=['GET'])
def transform_address():

    addr = request.args.get('addr')
    result_type = request.args.get('result_type')
    if (addr is None or result_type is None) or (result_type != 'jibeon' and result_type != 'road'):
        result = {
            'status_code': constants.CODE_400
            , 'status_msg': constants.MSG_400
            , 'full_addr': ''
        }
    else:
        full_addr = addr_service.transform(addr, result_type)

        result = {
            'status_code': constants.CODE_200
            , 'status_msg': constants.MSG_200
            , 'full_addr': full_addr
        }

    return Response(json.dumps(result), mimetype=constants.MIME_TYPE_APPLICATION_JSON)


@addr_controller.route('/api/addr/geocode', methods=['GET'])
def geocode_address():

    addr = request.args.get('addr')
    if addr is None:
        result = {
            'status_code': constants.CODE_400
            , 'status_msg': constants.MSG_400
            , 'coords': []
        }
    else:
        coord_list = addr_service.geocode(addr)

        result = {
            'status_code': constants.CODE_200
            , 'status_msg' : constants.MSG_200
            , 'coords': coord_list
        }

    return Response(json.dumps(result), mimetype=constants.MIME_TYPE_APPLICATION_JSON)
