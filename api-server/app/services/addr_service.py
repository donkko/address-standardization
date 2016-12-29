# -*- coding: utf-8 -*-

from addr_modules.addr_standardize import AddrStandardizer


class AddrService(object):
    def __init__(self):
        self.__standardizer__ = AddrStandardizer()

    def normalize(self, addr):
        normalized_addr = self.__standardizer__.normalize(addr)
        return normalized_addr

    def analyze(self, addr):
        pass
