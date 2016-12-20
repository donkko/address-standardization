# coding=utf-8

from app.services.addr_modules.addr_normalize import AddrNormalizer
from app.services.addr_modules.addr_transform import AddrTransformer
from app.services.addr_modules.addr_geocode import AddrGeocoder


class AddrService(object):
    def __init__(self):
        self.__normalizer__ = AddrNormalizer()
        self.__transformer__ = AddrTransformer()

    def normalize(self, addr):
        normalized_addr = self.__normalizer__.normalize(addr)
        return normalized_addr

    def analyze(self, addr):
        pass

    def transform(self, addr, result_type):
        if result_type == 'jibeon':
            result = self.__transformer__.road2jibeon(addr)
        elif result_type == 'road':
            result = self.__transformer__.jibeon2road(addr)
        return result

    def geocode(self, addr):
        coord_list = AddrGeocoder.do_geocoding(addr)
        if coord_list is None:
            return []
        return coord_list
