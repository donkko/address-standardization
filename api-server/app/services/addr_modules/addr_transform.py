# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from app.constants import JUSO_API_URL
from app.constants import JUSO_API_KEY


class AddrTransformer(object):
    '''
    지번주소 <-> 도로명주소 변환 클래스
    '''

    api_url = JUSO_API_URL
    api_params = {
        'confmKey': JUSO_API_KEY,
        'currentPage': '1',
        'countPerPage': '10',
        'keyword': ''
    }

    def __init__(self):
        pass

    def road2jibeon(self, road_addr):
        self.api_params['keyword'] = road_addr
        req = requests.get(self.api_url, params=self.api_params)
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text)
        if not soup.find('juso'):
            return None
        raw_jibeon = soup.find('juso').jibunaddr.string
        cleaned_jibeon = re.sub("\s{2,}", " ", raw_jibeon)
        return cleaned_jibeon

    def jibeon2road(self, jibeon_addr):
        self.api_params['keyword'] = jibeon_addr
        req = requests.get(self.api_url, params=self.api_params)
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text)
        if not soup.find('juso'):
            return None
        raw_road = soup.find('juso').roadaddrpart1.string
        cleaned_road = re.sub("\s{2,}", " ", raw_road)
        return cleaned_road


# if __name__ == '__main__':
#     transformer = AddrTransformer()
#     print transformer.road2jibeon('전라남도 목포시 평화로61번길 19')
