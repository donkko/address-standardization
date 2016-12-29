# -*- coding: utf-8 -*-

from addr_modules.addr_normalize import AddrNormalizer


class AddrService(object):
    def __init__(self):
        self.__normalizer__ = AddrNormalizer()

    def normalize(self, addr):
        normalized_addr = self.__normalizer__.normalize(addr)
        return normalized_addr

    def analyze(self, addr):
        pass
