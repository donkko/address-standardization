# -*- coding: utf-8 -*-

import requests
from xml.dom.minidom import parseString
from app.constants import NAVER_MAP_API_KEY
from app.constants import NAVER_MAP_API_URL


class AddrGeocoder(object):
    __map_API_key__ = NAVER_MAP_API_KEY
    __params__ = {}
    __api_url__ = None
    __response__ = None

    def __init__(self):
        pass

    @staticmethod
    def do_geocoding(addr):
        return AddrGeocoder._do_geocoding_using_naver(addr)

    @staticmethod
    def _do_geocoding_using_naver(addr):

        if unicode == type(addr):
            addr = addr.encode('utf-8')

        AddrGeocoder.__params__['key'] = AddrGeocoder.__map_API_key__
        AddrGeocoder.__params__['encoding'] = 'utf-8'
        AddrGeocoder.__params__['coord'] = 'latlng'
        AddrGeocoder.__params__['query'] = addr

        AddrGeocoder.__api_url__ = NAVER_MAP_API_URL

        req = requests.get(AddrGeocoder.__api_url__, params=AddrGeocoder.__params__)
        if req.status_code != 200:
            return None
        req.encoding = 'utf-8'

        coord_list = []
        xmldoc = parseString(req.text.encode('utf-8'))
        point_list = xmldoc.getElementsByTagName('point')
        for point in point_list:

            point_x_list = point.getElementsByTagName('x')
            point_y_list = point.getElementsByTagName('y')

            if 1 != len(point_x_list) or 1 != len(point_y_list):
                # 'point' tag is supposed to have only only pair of x & y
                continue

            point_x = float(str(point_x_list[0].toxml()).replace('<x>', '').replace('</x>', ''))
            point_y = float(str(point_y_list[0].toxml()).replace('<y>', '').replace('</y>', ''))
            coord_list.append({"lng": point_x, "lat": point_y})

        return coord_list

    @staticmethod
    def do_reverse_geocoding(lat, lng):
        pass


# if __name__ == '__main__':
#     print '[AddrGeocoder::main] invoked.'
#
#     testList = [
#             '대전 유성 복용동',
#             '전라북도 정읍시 태인 태흥리',
#             '전라북도 진안군 마령면 덕천리',
#             '충북 제천시 청풍면 연론리',
#             '세종시 연기면 해밀리',
#             '서울 강남 논현',
#             '전라북도 무주 무풍면 금평리 2121-1',
#             '경기도 수원시 팔달구 남창동 130-14',
#             '전라남도 광양시 진상면 금이리 492-1',
#             '경기도 수원시 팔달구 남창(산)동 1-72',
#             '경기도 오산시 서동 10-7',
#             '서울 성동구 성수동2가 299-235 101호',
#             '서울특별시 금천구 독산3동 953번지 삼부 르네상스 빌딩 2층 베니스뷔페',
#             '대전 서구 용문동 590-2 대산빌딩 101호',
#             '인천광역시 남동구 구월동 1408 인천종합문화예술회관',
#             '대전광역시 서구 둔산로 18(향촌월드프라자) 향촌월드프라자 901호 둔산아트홀',
#             '부산광역시 강서구 대저 34-78',
#             '서울시 강남구 개포3동 3-4번지',
#             '서울 강남 가로수길',
#             '서울 강남 가로수',
#             '서울 강남 가로수 서초',
#             '제주도 서귀포시 천지동 299-3',
#             '서울 강북 상봉동/망우동',
#             '서울 강남 방배동',
#             '서울 강남 방배동 2-3',
#             '제주도 제주시 일도1동 1048-10',
#             '서울특별시 서초구 서초동 1566-3',
#             '경기도 수원시 팔달구 북수동 21-10',
#             '경기도 성남시 분당구 서현동 256',
#             '서울시 서초구 서초동 서초대로 46길 92',
#             '서울시 서초구 서초동 1566-3'
#             ]
#
#     for elem in testList:
#         print 'INPUT:', elem
#         coord_list = AddrGeocoder.do_geocoding(elem)
#         for coord in coord_list:
#             print '\t', coord['lat'], coord['lng']
