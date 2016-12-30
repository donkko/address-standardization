# -*- coding: utf-8 -*-

import re


def do_cleansing(address):
    def remove_bracket_with_contents(addr):
        addr = re.sub("\(.*\)", "", addr)
        return re.sub("\(.*", "", addr)

    def remove_special_character(addr):
        addr = re.sub(",", " ", addr)
        return re.sub("\.", " ", addr)

    def remove_whitespaces(addr):
        return re.sub("\s{1,}", "", addr)

    def remove_useless(addr):
        if u'번지' in addr:
            return addr[:addr.find(u'번지')]

        # print addr
        # for term in addr.split():
        #     print re.match(u"^(\d+-\d+|\d+)$"), term

        #TODO: 번지 추출하는 방식을 좀더 우아하게 바꿀수 있을듯. 예를 들면 n-gram으로?
        for item in re.findall(u"(\d+-\d+|\d+)", addr):
            after_item_idx = addr.find(item) + len(item)
            if after_item_idx <= len(addr) - 1:
                if not (u'읍' in addr[after_item_idx] or
                u'면' in addr[after_item_idx] or
                u'리' in addr[after_item_idx] or
                u'동' in addr[after_item_idx] or
                u'가' in addr[after_item_idx] or
                u'산' in addr[after_item_idx] or
                u'길' in addr[after_item_idx] or
                u'로' in addr[after_item_idx] or
                u'번' in addr[after_item_idx] or
                u'층' in addr[after_item_idx]):
                    return addr[:addr.find(item) + len(item)]
        return addr

    address = remove_bracket_with_contents(address)
    address = remove_special_character(address)
    address = remove_useless(address)
    address = remove_whitespaces(address)
    return address


if __name__ == '__main__':
    addr_list = [
        u"경기 고양시 일산동구 백석동 1351번지 흰돌마을 상가동 202호(청구코아상가 2층 백석동 이마트 맞은편)"
        , u"서울특별시 종로구 종로5가 165 종오쇼핑센타 다열 5호"
        , u"경기도안양시만안구안양동 1384청솔프라자206호"
        , u"경기도안산시상록구건건동 532덕천빌딩403호"
        , u"경기도 수원시 팔달구 인계동 1046-13번지 에스팝타워 202호"
        , u"경기도 수원시 팔달구 우만동 561-2번지 우암빌딩2층"
        , u"경기도 용인시 수지구 신봉동 40-2번지 신봉상가2층"
        , u"경기도 파주시 탄현면 헤이리마을길 59-78"
        , u"서울 마포구 서교동 357-1번지 2층"
        , u"대구달서구송현동 55-3번지"
        , u"옥암동 1038-6"
        , u"경상북도포항시남구상도동 615-1"
        , u"서울 강남구 논현동 187-5 1층 /서울특별시 강남구 강남대로 118길 64(논현동, 1층)"
        , u"경상남도 함안군 칠원면 오곡리 251-3번지"
        , u"경상남도 창원시 마산회원구 회원동 50-5 천지리치빌상가 2층"
        , u"인천 서구 당하동 39블럭 1롯트 선혜프라자 102호(검단 4동 사무소)"
        , u"경기도 성남시 분당구 서현동 246-2 신영팰리스타워 2층 203호"
        , u"경기 고양시 일산동구 풍동 665-3번지"
        , u"경기도안양시동안구인덕원로13 1층"
        , u"경기도 광주시 오포읍 신현리 532-2  (네비 검색시에는"
        , u"경남 김해시 신문동 1414 김해관광유통단지 1B 4L번지 3층"
    ]

    for addr in addr_list:
        print 'INPUT: ' + addr
        print 'OUTPUT: ' + do_cleansing(addr)
