# -*- coding: utf-8 -*-

from addr_modules.addr_normalize import AddrNormalizer
from addr_modules.addr_transform import AddrTransformer


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
