# -*- coding: utf-8 -*-

from addr_modules.addr_standardize import AddrStandardizer


class AddrService(object):
    def __init__(self):
        self.__standardizer__ = AddrStandardizer()

    def standardize(self, addr):
        standardized_addr = self.__standardizer__.standardize(addr)
        return standardized_addr

    def analyze(self, addr):
        pass
