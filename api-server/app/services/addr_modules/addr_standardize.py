# -*- coding: utf-8 -*-

import json
import codecs
from app.services.addr_modules.addr_preprocess import do_cleansing
from app.services.addr_modules.addr_tree.addr_tree_build import AddrTreeBuilder
from app.services.addr_modules.addr_tree.addr_tree_common import get_depth
from app.services.addr_modules.TRIE.TRIE_build import TrieTreeBuilder
from app.services.addr_modules.TRIE.TRIE_common import get_split_points


from app.constants import ADDR_JIBEON_SET_FILEPATH
from app.constants import ADDR_ROAD_SET_FILEPATH
from app.constants import TRIE_DICT_FOLDERPATH
from app.constants import TRIE_GOVDIC_FILEPATH
from app.constants import TRIE_USERDIC_FILEPATH
from app.constants import SHORT_ADDR_SET_FILEPATH


class AddrStandardizer(object):
    '''
    주소정규화 클래스. addr_preprocess 와 addr_tree 를 이용하여 입력된 주소를 정규화.
    '''
    def __init__(self):
        builder = AddrTreeBuilder()
        self.__root_node_jibeon__ = builder.buildAddrTree(ADDR_JIBEON_SET_FILEPATH)
        self.__root_node_road__ = builder.buildAddrTree(ADDR_ROAD_SET_FILEPATH)
        self.__short_addr_dict__ = json.load(codecs.open(SHORT_ADDR_SET_FILEPATH, encoding='utf-8'))
        trie_builder = TrieTreeBuilder()
        self.__root_node_TRIE__ = trie_builder.buildTrieTree(TRIE_DICT_FOLDERPATH)


    def normalize(self, addr_str):
        result_list = []
        clean_addr_str = do_cleansing(addr_str)
        print "[clean_addr_str]", clean_addr_str

        split_addr_list_by_trie_addr = get_split_points(self.__root_node_TRIE__, clean_addr_str)
        for idx, split_addr in enumerate(split_addr_list_by_trie_addr):
            print '[split_addr_candidate_' + str(idx) + ']' + split_addr
            addr_candidate_tuple = self.recover_short_addr(split_addr)
            result_list.append(addr_candidate_tuple)
            print "[addr_candidate_" + str(idx) + ']' + ' [depth]' + str(addr_candidate_tuple[0]) \
                  + ' [addr]' + addr_candidate_tuple[1]

        result_list = sorted(result_list, reverse=True)
        if result_list:
            print '[final]', result_list[0][1]
            print ''
            return result_list[0][1]


    def recover_short_addr(self, addr_str):
        def _create_list_combination(combi_list, stack, result):
            if len(combi_list) == len(stack):
                result.append(" ".join(stack))
                return None

            now = len(stack)
            for term in combi_list[now]:
                stack.append(term)
                _create_list_combination(combi_list, stack, result)
                stack.pop()

        complete_addr_list = []
        addr_term_list = addr_str.split()
        combi_addr_list = []
        for addr_term in addr_term_list:
            tmp_term_list = [addr_term]
            if addr_term in self.__short_addr_dict__:
                print "[recover_short_addr] input:", addr_term
                for level in sorted(self.__short_addr_dict__[addr_term].keys()):
                    tmp_term_list.extend(self.__short_addr_dict__[addr_term][level])
                print "[recover_short_addr] output:"
                for elem in tmp_term_list:
                    print elem
            combi_addr_list.append(tmp_term_list)

        stack = []
        _create_list_combination(combi_addr_list, stack, complete_addr_list)
        del stack

        max_depth_by_jibeon_tree = 0
        addr_candidate_by_jibeon_tree = ""
        max_depth_by_road_tree = 0
        addr_candidate_by_road_tree = ""
        print "[recover_short_addr] complete_addr_list:"
        #TODO: 누락 주소 recover(예: 서울 창동 11-1 > 서울 도봉구 창동 11-1)시 tree depth 체크하면서 누락분 후보군 리스트 만들고 다시 돌리면 해결 될듯
        for complete_addr in complete_addr_list:
            print complete_addr
            depth_by_jibeon_tree = get_depth(self.__root_node_jibeon__, complete_addr)
            if depth_by_jibeon_tree > max_depth_by_jibeon_tree:
                addr_candidate_by_jibeon_tree = complete_addr
                max_depth_by_jibeon_tree = depth_by_jibeon_tree

            depth_by_road_tree = get_depth(self.__root_node_road__, complete_addr)
            if depth_by_road_tree > max_depth_by_road_tree:
                addr_candidate_by_road_tree = complete_addr
                max_depth_by_road_tree = depth_by_road_tree

        if max_depth_by_road_tree > max_depth_by_jibeon_tree:
            return (max_depth_by_road_tree,
                    (addr_candidate_by_road_tree if addr_candidate_by_road_tree else addr_str))
        else:
            return (max_depth_by_jibeon_tree,
                    (addr_candidate_by_jibeon_tree if addr_candidate_by_jibeon_tree else "None"))


# if __name__ == '__main__':
#
#     addr_list = [
#         u"서울시 양천구 목3동 648-1 102호"
#         ,u"경기도 안양시 동안구 비산동 1102-9번지 주공관악상가204호"
#         ,u"경기도 광명시 철산동 473-14 2층(광명시청정문앞)"
#         ,u"서울시 구로구신도림동 460-26 (2호선 신도림역)"
#         ,u"경기도 부천시 원미구 역곡동 106-7 101호"
#         ,u"서울시 중구 충무로4가 125-3 지하1층(충무로4가, 충무로역)"
#         ,u"서울특별시 관악구 신림동 240-1"
#         ,u"서울특별시 서초구 서초동 1659-1"
#         ,u"서울특별시 송파구 가락동 105-1"
#         ,u"경기도광주시목현동 이배재로405"
#         ,u"경기도 안산시 상록구 월피동508번지105호"
#         ,u"서울시 강남구 대치동 890-54 풍림아이원 레몬아파트 203호"
#         ,u"경기도 안산시 단원구 초지동 719-6"
#         ,u"부산 진구 부전동 516-40,4층"
#         ,u"경기도 파주시 문산읍 문산리 10-42"
#         ,u"서울 강남구 논현동 3-8 토마스빌딩 3층 (신사역1번)"
#         ,u"서울 강남구 대치동 900-56 백제빌딩 2층"
#         ,u"서울 강동구 천호동 429-4번지 2층 (천호역3번)"
#         ,u"서울 마포구 서교동 391-17호 3층 (합정역2번)"
#         ,u"경남 김해시 삼계동 1487-7 우리빌딩 602호"
#         ,u"서울 강동구 성내동 164-1"
#         ,u"서울 강서구 화곡동 1024-10. 2층 클린안마원"
#         ,u"서울 강서구 화곡6동 1104-5 202호"
#         ,u"서울 중구 신당동 288-6. 1F"
#         ,u"서울 강남구 삼성동 159-6번지 도심공항 내 칼트몰"
#         ,u"인천 남동구 만수2동 72-16번지 3층"
#         ,u"경기 군포시 산본동 1142-12 군포상가 5층 504호 (산본역3번)"
#         ,u"경기 부천시 원미구 상동 544-4번지 308호 (상동역3번)"
#         ,u"경기도 광주시 초월읍 지월리 550-6"
#         ,u"종로구 창성동 144"
#         ,u"경남 창원시 성산구 중앙동 67-12"
#         ,u"광주시 광산구 운남동 785-1"
#         ,u"경기도 수원시 장안구 파장동 579-38번지 2층"
#         ,u"경기도 성남시 분당구 구미동 40-6"
#         ,u"경기 고양시 일산동구 백석동 1351번지 흰돌마을 상가동 202호(청구코아상가 2층 백석동 이마트 맞은편)"
#         ,u"서울특별시 종로구 종로5가 165 종오쇼핑센타 다열 5호"
#         ,u"경기도안양시만안구안양동 1384청솔프라자206호"
#         ,u"경기도안산시상록구건건동 532덕천빌딩403호"
#         ,u"경기도 수원시 팔달구 인계동 1046-13번지 에스팝타워 202호"
#         ,u"경기도 수원시 팔달구 우만동 561-2번지 우암빌딩2층"
#         ,u"경기도 용인시 수지구 신봉동 40-2번지 신봉상가2층"
#         ,u"경기도 파주시 탄현면 헤이리마을길 59-78"
#         ,u"서울 마포구 서교동 357-1번지 2층"
#         ,u"대구달서구송현동 55-3번지"
#         ,u"옥암동 1038-6"
#         ,u"경상북도포항시남구상도동 615-1"
#         ,u"서울 강남구 논현동 187-5 1층 /서울특별시 강남구 강남대로 118길 64(논현동, 1층)"
#         ,u"경상남도 함안군 칠원면 오곡리 251-3번지"
#         ,u"경상남도 창원시 마산회원구 회원동 50-5 천지리치빌상가 2층"
#         ,u"인천 서구 당하동 39블럭 1롯트 선혜프라자 102호(검단 4동 사무소)"
#         ,u"경기도 수원시 팔달구 팔달로3가 84-5"
#         ,u"부천시 원미구 원미동 51-6번지 원미스파랜드 1층"
#         ,u"경기도안양시만안구안양동 622-233"
#         ,u"경기 수원시 영통구 매탄동 1263-3번지 4층"
#         ,u"대구 수성구 두산동  138-10"
#         ,u"대구광역시남구봉덕2동 1002-35번지"
#         ,u"대구광역시수성구만촌동 1046-10"
#         ,u"대구광역시수성구범물동 1352-4"
#         ,u"서울 강남구 삼성동 142-2번지 인화빌딩 2층"
#         ,u"대구광역시 달서구 본동 721-1 타이어테크"
#         ,u"대구광역시달서구송현동 530-12"
#         ,u"대구시 남구 봉덕동 729-13번지"
#         ,u"서울시 관악구 신림동 543-20 2층"
#         ,u"서울 마포구 용강동 21번지 솔하우스 1층"
#         ,u"경상북도포항시북구대흥동 663-19"
#         ,u"서울 강남구 역삼동 709. 아이파크상가 1층 21호"
#         ,u"경상남도 창원시 성산구 마디미로15번길 2"
#         ,u"울산광역시동구전하동 648-16번지2층"
#         ,u"대전광역시 유성구 교촌동 245"
#         ,u"경기 수원시 영통구 영통동 958-1번지"
#         ,u"충청남도 천안시 동남구 봉명동 493-4번지"
#         ,u"서울 강서구 등촌동 78-7. 길훈엔트레스빌 2층"
#         ,u"경기도 안양시 동안구 호계동 208-5 B"
#         ,u"서울 마포구 서교동 330-21 2층"
#         ,u"경기도 구리시 수택동 376-23번지"
#         ,u"경남 진주시 상대동 767-5"
#         ,u"경남 창원시 의창구 소답동 141-13"
#         ,u"전북 군산시 문화동 30-3"
#         ,u"충청북도 청주시 흥덕구 가경동 1503-17"
#         ,u"대구 남구 대명동 1137-1번지"
#         ,u"서울특별시 마포구 서교동 391-17"
#         ,u"서울 종로구 수송동 85번지 서머셋팰리스서울 1층"
#         ,u"서울 송파구 신천동 11-4 잠실푸르지오월드마크1층"
#         ,u"경기 수원시 영통구 매탄동 863"
#         ,u"서울시 강남구 신사동 636-29번지 3층"
#         ,u"서울시 강남구 대치동 900-7 2층"
#         ,u"서울시 강남구 도곡동 952-10번지"
#         ,u"경기도 하남시 덕풍동 744-2 풍산캐슬 3층 303호 벨스킨"
#         ,u"경기도 수원시 영통구 영통동 975-3번지"
#         ,u"서울 마포구 서교동 346-33 / 2층"
#         ,u"경기도 파주시 탄현면 법흥리 1652-34"
#         ,u"경기도 성남시 분당구 서현동 246-2 신영팰리스타워 2층 203호"
#         ,u"경기 고양시 일산동구 풍동 665-3번지"
#         ,u"경기도안양시동안구인덕원로13 1층"
#         ,u"경기도 광주시 오포읍 신현리 532-2  (네비 검색시에는"
#         ,u"경기도안양시동안구호계동 1039롯데백화점 지하 1층"
#         ,u"경기 수원시 영통구 망포동  483번지 1층 102"
#         ,u"서울 서대문구 창천동 52-51"
#         ,u"대구광역시달서구이곡동 443번지"
#         ,u"대구달서구장동 832번지"
#     ]
#
#     normalizer = AddrStandardizer()
#     for addr in addr_list:
#         normalizer.normalize(addr)

    # addr = u"부산 진구 부전동 516-40"
    # result = normalizer.normalize(addr)
    # print addr + ", " + (result if result else "None")
