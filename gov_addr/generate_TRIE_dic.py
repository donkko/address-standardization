# coding=utf-8

import os
import codecs

# 인코딩처리
import pprint


class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, _object, context, maxlevels, level):
        if isinstance(_object, unicode):
            return "'%s'" % _object.encode('utf8'), True, False
        elif isinstance(_object, str):
            _object = unicode(_object, 'utf8')
            return "'%s'" % _object.encode('utf8'), True, False
        return pprint.PrettyPrinter.format(self, _object, context, maxlevels, level)


INPUT_DATA_DIRECTORY = './raw_data'
OUTPUT_FILEPATH = '../api-server/app/services/addr_modules/TRIE/data/GovDic.txt'


def generate_TRIE_dic():
    res = []  # 각 파일 읽어서 담기

    # filename ="전체주소_세종특별자치시.txt"
    # filepath = os.path.join(INPUT_DATA_DIRECTORY, filename)
    # res.extend(file_rotation(filepath))

    # 리소스 파일 전체 확인
    for filename in os.listdir(INPUT_DATA_DIRECTORY):
        # 파일경로 합치고
        print "----Start File Name----", filename
        filepath = os.path.join(INPUT_DATA_DIRECTORY, filename)
        # 각 파일 읽어서 담기
        res.extend(file_rotation(filepath))
        print "-----------EoF---------"

    # 변환해서 한글로 보기위한 출력
    # print MyPrettyPrinter().pformat(res)

    # 결과 res 파일저장 OUTPUT_FILEPATH
    filesave(OUTPUT_FILEPATH, res)


def filesave(inputFilePath, result):
    with open(inputFilePath, 'w') as f:
        for line in result:
            print >> f, line.encode('utf-8')


def file_rotation(inputFilePath):
    """
    1. 특별시/광역시/특별자치시/도/특별자치도
    2. 시/특별시/행정시/군/자치구/일반구 *
    3. 읍/면/동/로/가 *
    4. 리/통 *
    5. 산여부
    6. 지번본번
    7. 지번부번
    8. 도로명코드
    9. 도로명 *
    10. 지하여부
    11. 건물본번
    12. 건물부번
    13. 건축물대장 건물명
    14. 상세건물명
    15. 건물관리번호
    16. 읍면동일렬번호
    17. 행정동코드
    18. 행정동명 *
    -생략-
    24. 변경전도로명주소코드
    25. 시구군용 건물명
    26. 공동주택여부
    -끝-

    특이사항 예외처리

    1. 시단위 레벨에서 ['수원시 장안구'] 같은 케이스 때문에 split ' '으로 한번 더 해서 담아야함.
    2. 서초3동의 경우 저장. 서초3으로 되는 경우 3을 날리고 서초로 처리. 기반에 서초동은 존재할 것임.
    3. 2글자 레벨은 원본 그대로 저장. ['목동', '중구'] 등등등
    """
    # res_rotation_data=[]

    # 파일 읽기
    r = codecs.open(inputFilePath, 'r', 'EUC-KR', 'ignore')

    # province_list = []
    county_list = []
    town_list = []
    village_list = []
    roadname_list = []
    hengjungdong_list = []

    # 라인 리드 #print type(line)
    for line in r:
        try:
            # 라인 trip, |로 스프리트
            columns = line.strip().split('|')

            # province = columns[1]
            county = columns[2].strip()
            town = columns[3].strip()
            village = columns[4].strip()
            roadname = columns[9].strip()
            hengjungdong = columns[18].strip()

            # level_1 = [u'시', u'특별시', u'행정시', u'광역시', u'도']
            level_2 = [u'시', u'구', u'군']
            level_3 = [u'읍', u'면', u'동', u'가']
            level_4 = [u'리', u'통']
            # 18은 예외가 더 있을것으로 보임
            level_henjung = [u'동', u'읍', u'면', u'통', u'리']

            ############ county ############
            if county == "":
                pass  # print "COUNTY: ##시단위 결과없음##"
            else:
                # print "COUNTY:" + county
                if ' ' in county:  # 수원시 팔달구 처리용
                    county1, county2 = county.split()

                    # suffix 자른 애들 - 수원, 팔달
                    for suffix in level_2:
                        if county1.endswith(suffix):
                            county1_shortened = county1.rstrip(suffix)
                        if county2.endswith(suffix):
                            county2_shortened = county2.rstrip(suffix)
                    if len(county1_shortened) > 1 and county1_shortened not in county_list:
                        county_list.append(county1_shortened)
                    if len(county2_shortened) > 1 and county2_shortened not in county_list:
                        county_list.append(county2_shortened)

                    # suffix 안자른 애들 - 수원시, 팔달구
                    if county1 not in county_list:
                        county_list.append(county1)
                    if county2 not in county_list:
                        county_list.append(county2)

                else:  # 일반 케이스 _ 구미시, 경주시
                    # suffix 자른 애 - 구미
                    for suffix in level_2:
                        if county.endswith(suffix):
                            county_shortened = county.rstrip(suffix)
                    if len(county_shortened) > 1 and county_shortened not in county_list:
                        county_list.append(county_shortened)

                    # suffix 안자른 애 - 구미시
                    if county not in county_list:
                        county_list.append(county)


            ############ town ############
            if town == "":
                pass  # print "TOWN: ##마을단위 결과없음##"
            else:
                # print "TOWN:" + town
                # 일반케이스 봉천동, 목1동, 안심1동 , suffix 자른 타운레벨
                ###
                for suffix in level_3:
                    if town.endswith(suffix):
                        town_shortened = town.rstrip(suffix)

                # 자른 맨 끝이 숫자인 경우 맨 끝 한개의 숫자 삭제
                if town_shortened[len(town_shortened) - 1:].isdigit():
                    town_shortened = town_shortened[:len(town_shortened) - 1]
                if town_shortened[len(town_shortened) - 1:].isdigit():
                    town_shortened = town_shortened[:len(town_shortened) - 1]
                if len(town_shortened) > 1 and town_shortened not in town_list:
                    town_list.append(town_shortened)

                # suffix 안자른 타운 이름
                if town not in town_list:
                    town_list.append(town)

            ############ village ############
            if village == "":
                pass  # print "VILLAGE: ##촌락단위 결과없음##"
            else:
                # print "VILLAGE:" + village
                if village not in village_list:
                    village_list.append(village)

            ############ roadname ############
            if roadname == "":
                pass  # print "ROADNAME: ##도로명 없음##"
            else:
                # print "ROADNAME:" + roadname
                if roadname not in roadname_list:
                    roadname_list.append(roadname)

            ############ hengjungdong ############
            if hengjungdong == "":
                pass  # print "HENGJUNGDONG: ##행정동 결과없음##"
            else:
                # print "HENGJUNGDONG:" + hengjungdong

                # 행정동 suffix 자른 케이스
                for suffix in level_henjung:
                    if hengjungdong.endswith(suffix):
                        hengjungdong_shortened = hengjungdong.rstrip(suffix)

                # 자른 행정동의 끝이 숫자인 경우 삭제
                if hengjungdong_shortened[len(hengjungdong_shortened) - 1:].isdigit():
                    hengjungdong_shortened = hengjungdong_shortened[:len(hengjungdong_shortened) - 1]
                if hengjungdong_shortened[len(hengjungdong_shortened) - 1:].isdigit():
                    hengjungdong_shortened = hengjungdong_shortened[:len(hengjungdong_shortened) - 1]
                if len(hengjungdong_shortened) > 1 and hengjungdong_shortened not in hengjungdong_list:
                    hengjungdong_list.append(hengjungdong_shortened)

                # 자르지 않은 행정동
                if hengjungdong not in hengjungdong_list:
                    hengjungdong_list.append(hengjungdong)

        ### line read end ###

        except Exception as error:
            print "LINE:", line
            print "errorMsg :", error
            exit(1)


            # # 명칭 유니코드 처리 후 각 행정 구역 호출
            # for hengjung_area in add_level_list:
            # # print add_level_list[1] + '\n'
            #     # add_list 종류별로 데이터 자르기
            #     uni_string = unicode(hengjung_area)
            #
            #     # 멀쩡한 데이터 우선저장 저장 if 데이터에 내용이 있으면 저장하지않고 패스
            #     if uni_string not in res_rotation_data:
            #         res_rotation_data.append(uni_string)
            #         # print uni_string
            #
            #         # 그 후 멀쩡한 데이터를 splite_level에 따라 자르고 저장 하는데, 글자 길이가 3글자인 경우만 잘라서 저장.
            #         # 숫자날려야하는데...
            #         if len(uni_string) > 2:
            #             rstrip_string = uni_string.rstrip(level_2[1])
            #
            #             # 자른 데이터 저장 if 데이터에 내용이 있으면 저장하지않고 패스
            #             if rstrip_string not in res_rotation_data:
            #                 # print rstrip_string
            #                 res_rotation_data.append(rstrip_string)
            #         else:
            #             continue

    # print res_rotation_data
    # 상위 함수로 리턴
    return county_list + town_list + village_list + roadname_list + hengjungdong_list


if __name__ == '__main__':
    generate_TRIE_dic()
