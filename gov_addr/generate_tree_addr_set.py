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
OUTPUT_FILEPATH_JIBEON = '../api-server/app/services/addr_modules/addr_tree/addr_set_data/GovAddrSet_Jibeon.txt'
OUTPUT_FILEPATH_ROAD = '../api-server/app/services/addr_modules/addr_tree/addr_set_data/GovAddrSet_Road.txt'


def gen_tree(inputFilePath):
    line_jibeon_list = []
    line_road_list = []

    # 파일 읽기
    r = codecs.open(inputFilePath, 'r', 'EUC-KR', 'ignore')

    ### 라인 리드 # print type(line)
    for line in r:
        try:
            # 라인 trip, |로 스프리트
            columns = line.strip().split('|')

            province = columns[1].strip()  # 특별시도
            county = columns[2].strip()  # 시구군
            town = columns[3].strip()  # 동읍면가
            village = columns[4].strip()  # 리통
            roadname = columns[9].strip()
            # hengjungdong = columns[18].strip() # 행정동 사용안함

            jibeon_string = province + " " + county + " " + town + " " + village
            jibeon_string = jibeon_string.replace("  ", " ")
            jibeon_string = jibeon_string.strip()

            road_string = province + " " + county
            if village == "":
                road_string += " " + roadname
            else:
                road_string += " " + town + " " + roadname

            # 세종시 예외처리
            if county == "" and village == "":
                road_string = province + " " + town + " " + roadname

            road_string = road_string.replace("  ", " ")
            road_string = road_string.strip()

            if jibeon_string not in line_jibeon_list:
                line_jibeon_list.append(jibeon_string)

            if road_string not in line_road_list:
                line_road_list.append(road_string)

        ### line read end ###
        except Exception as error:
            print "LINE:", line
            print "errorMsg :", error
            exit(1)

    # return province_list + county_list + town_list + village_list + roadname_list + hengjungdong_list

    yield line_jibeon_list
    yield line_road_list


def generate_tree_addr_set():
    res_jibeon_list = []  # 각 파일 읽어서 담기
    res_road_list = []

    # filename = "전체주소_제주특별자치도.txt"
    # filepath = os.path.join(INPUT_DATA_DIRECTORY, filename)
    #
    # res.extend(gen_tree(filepath))

    # 리소스 파일 전체 확인
    for filename in os.listdir(INPUT_DATA_DIRECTORY):
        # 파일경로 합치고
        print "----Start File Name----", filename
        filepath = os.path.join(INPUT_DATA_DIRECTORY, filename)
        # 각 파일 읽어서 담기
        line_jibeon_list, line_road_list = gen_tree(filepath)
        res_jibeon_list.extend(line_jibeon_list)
        res_road_list.extend(line_road_list)
        print "-----------EoF---------"

    # 변환해서 한글로 보기위한 출력
    # print MyPrettyPrinter().pformat(res)

    # 결과 res 파일저장 OUTPUT_FILEPATH
    filesave(OUTPUT_FILEPATH_JIBEON, res_jibeon_list)
    print "지번 데이터 저장 완료"
    filesave(OUTPUT_FILEPATH_ROAD, res_road_list)
    print "도로명 데이터 저장 완료"


def filesave(inputFilePath, result):
    with open(inputFilePath, 'w') as f:
        for line in result:
            print >> f, line.encode('utf-8')


if __name__ == '__main__':
    generate_tree_addr_set()
