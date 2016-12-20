# coding=utf-8

import os
import codecs
import json



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
OUTPUT_FILEPATH = '../api-server/app/services/addr_modules/ShortAddr.json'

import time

t = time.time()


def generate_short_addr():
    # 결과 딕셔너리
    short2full = {
        u'서울': {'1': [u'서울특별시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'서울특별시': {'1': [u'서울특별시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'서울시': {'1': [u'서울특별시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'부산': {'1': [u'부산광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'부산시': {'1': [u'부산광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'부산광역시': {'1': [u'부산광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'대구': {'1': [u'대구광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'대구시': {'1': [u'대구광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'대구광역시': {'1': [u'대구광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'인천': {'1': [u'인천광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'인천시': {'1': [u'인천광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'인천광역시': {'1': [u'인천광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'광주': {'1': [u'광주광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'광주시': {'1': [u'광주광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'광주광역시': {'1': [u'광주광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'대전': {'1': [u'대전광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'대전시': {'1': [u'대전광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'대전광역시': {'1': [u'대전광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'울산': {'1': [u'울산광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'울산시': {'1': [u'울산광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'울산광역시': {'1': [u'울산광역시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'세종': {'1': [u'세종특별자치시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'세종시': {'1': [u'세종특별자치시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'세종특별시': {'1': [u'세종특별자치시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'세종자치시': {'1': [u'세종특별자치시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'세종특별자치시': {'1': [u'세종특별자치시'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'제주': {'1': [u'제주특별자치도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'제주도': {'1': [u'제주특별자치도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'제주특별자치도': {'1': [u'제주특별자치도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'경기': {'1': [u'경기도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'경기도': {'1': [u'경기도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'강원': {'1': [u'강원도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'강원도': {'1': [u'강원도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'충북': {'1': [u'충청북도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'충청북도': {'1': [u'충청북도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'충남': {'1': [u'충청남도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'충청남도': {'1': [u'충청남도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'전북': {'1': [u'전라북도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'전라북도': {'1': [u'전라북도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'전남': {'1': [u'전라남도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'전라남도': {'1': [u'전라남도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'경북': {'1': [u'경상북도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'경상북도': {'1': [u'경상북도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'경상남도': {'1': [u'경상남도'], u'2': [], u'3': [], u'4': [], u'5': []},
        u'경남': {'1': [u'경상남도'], u'2': [], u'3': [], u'4': [], u'5': []}
    }
    hengjung2beopjung = {}

    # 리소스 파일 전체 읽기

    for filename in os.listdir(INPUT_DATA_DIRECTORY):
        # 파일경로 합치고
        print "----Start File Name----", filename
        filepath = os.path.join(INPUT_DATA_DIRECTORY, filename)

        # 각 파일 읽어서 담기
        # 파일 읽기
        with codecs.open(filepath, 'r', 'EUC-KR', 'ignore') as r:
            # 라인 리드 #print type(line)
            for line in r:
                try:

                    # 라인 trip, |로 스프리트
                    columns = line.strip().split('|')

                    province = columns[1]
                    county = columns[2].strip()
                    town = columns[3].strip()
                    village = columns[4].strip()
                    roadname = columns[9].strip()
                    hengjungdong = columns[18].strip()

                    level_1 = [u'특별시', u'광역시', u'도', u'시']
                    level_2 = [u'시', u'구', u'군']
                    level_3 = [u'읍', u'면', u'동', u'가']
                    level_4 = [u'리', u'통']
                    # 18은 예외가 더 있을것으로 보임
                    level_henjung = [u'동', u'읍', u'면', u'통', u'리']

                    ############# county ############

                    if county == "":
                        pass  # print "COUNTY: ##시단위 결과없음##"
                    else:
                        if ' ' in county:  # 수원시 팔달구 처리용
                            county1, county2 = county.split()
                            # suffix 자른 애들 - 수원, 팔달

                            for suffix in level_2:
                                # 수원시 처리
                                if county1.endswith(suffix):
                                    county1_shorten = county1[:len(county1) - 1]
                                    # init_chk(short2full, county1_shorten, 2, county1)

                                # 팔달구 처리
                                if county2.endswith(suffix):
                                    county2_shorten = county2[:len(county2) - 1]
                                    # init_chk(short2full, county2_shorten, 2, county2)

                            if len(county1_shorten) > 1 and county1_shorten not in short2full:
                                init_chk(short2full, county1_shorten, 2, county1)
                                # short2full[county1_shorten].append(county1_shorten)

                            if len(county2_shorten) > 1 and county2_shorten not in short2full:
                                init_chk(short2full, county2_shorten, 2, county2)
                                # short2full[county2_shorten].append(county2_shorten)

                            # suffix 안자른 애들 - 수원시, 팔달구
                            if county1 not in short2full:
                                init_chk(short2full, county1, 2, county1)
                            if county2 not in short2full:
                                init_chk(short2full, county2, 2, county2)

                        else:  # 일반 케이스 _ 구미시, 경주시
                            # suffix 자른 애 - 구미
                            for suffix in level_2:
                                if county.endswith(suffix):
                                    county_shorten = county[:len(county) - 1]
                                    # init_chk(short2full, county_shorten, 2, county)

                            if len(county_shorten) > 1 and county_shorten not in short2full:
                                init_chk(short2full, county_shorten, 2, county)

                            # suffix 안자른 애 - 구미시
                            if county not in short2full:
                                init_chk(short2full, county, 2, county)

                    ############ town ############
                    if town == "":
                        pass  # print "TOWN: ##마을단위 결과없음##"
                    else:
                        # 일반케이스 봉천동, 목1동, 안심1동 , suffix 자른 타운레벨
                        ###
                        for suffix in level_3:
                            if town.endswith(suffix):
                                town_shorten = town[:len(town) - 1]
                                # init_chk(short2full, town_shorten, 3, town)

                        # 자른 맨 끝이 숫자인 경우 맨 끝 한개의 숫자 삭제
                        if town_shorten[len(town_shorten) - 1:].isdigit():
                            town_shorten = town_shorten[:len(town_shorten) - 1]
                            # init_chk(short2full, town_shorten, 3, town)
                        if town_shorten[len(town_shorten) - 1:].isdigit():
                            town_shorten = town_shorten[:len(town_shorten) - 1]
                        # init_chk(short2full, town_shorten, 3, town)

                        if len(town_shorten) > 1 and town_shorten not in short2full:
                            init_chk(short2full, town_shorten, 3, town)

                        # suffix 안자른 타운 이름
                        if town not in short2full:
                            init_chk(short2full, town, 3, town)

                    ############ village ############
                    if village == "":
                        pass  # print "VILLAGE: ##촌락단위 결과없음##"
                    else:
                        # print "VILLAGE:" + village
                        if village not in short2full:
                            init_chk(short2full, village, 4, village)

                    ########### roadname ############
                    if roadname == "":
                        pass  # print "ROADNAME: ##도로명 없음##"
                    else:
                        # print "ROADNAME:" + roadname
                        if roadname not in short2full:
                            init_chk(short2full, roadname, 5, roadname)



                    # ############ hengjungdong ############
                    if hengjungdong == "":
                        pass
                    else:
                        ### 행정동
                        for suffix in level_3:
                            if hengjungdong.endswith(suffix):
                                hengjungdong_shortened = hengjungdong[:len(hengjungdong) - 1]

                        # 자른 맨 끝이 숫자인 경우 맨 끝 한개의 숫자 삭제
                        if hengjungdong_shortened[len(hengjungdong_shortened) - 1:].isdigit():
                            hengjungdong_shortened = hengjungdong_shortened[:len(hengjungdong_shortened) - 1]
                        if hengjungdong_shortened[len(hengjungdong_shortened) - 1:].isdigit():
                            hengjungdong_shortened = hengjungdong_shortened[:len(hengjungdong_shortened) - 1]
                        if len(hengjungdong_shortened) > 1 and hengjungdong_shortened not in short2full:
                            init_chk(short2full, hengjungdong_shortened, 'h', town)

                        # suffix 안자른 행정동 이름.
                        if hengjungdong not in short2full:
                            init_chk(short2full, hengjungdong, 'h', town)
                except Exception as e:
                    print line
                    print e
                    exit(1)
    # ### line read end ###
    #
    # except Exception as error:
    # print "LINE:", line
    #     print "errorMsg :", error
    #     exit(1)

    # 변환해서 한글로 보기위한 출력
    # print MyPrettyPrinter().pformat(short2full)

    # 파일 쓰기
    with codecs.open(OUTPUT_FILEPATH, "w", encoding="utf-8") as f:
        f.write(json.dumps(short2full, ensure_ascii=False))
    f.close()


def init_chk(list, chkdata, level, insertdata):
    if level == 1:
        if chkdata not in list:
            # 처음넣는경우
            list[chkdata] = {'1': [], '2': [], '3': [], '4': [], '5': []}
            list[chkdata]['1'].append(insertdata)
        else:
            # 추가하는경우, 해당 리스트 내 내용이 비었나 체크 후 추가
            if insertdata not in list[chkdata]['1']:
                list[chkdata]['1'].append(insertdata)
    elif level == 2:
        if chkdata not in list:
            # 처음넣는경우
            list[chkdata] = {'1': [], '2': [], '3': [], '4': [], '5': []}
            list[chkdata]['2'].append(insertdata)
        else:
            # 추가하는경우, 해당 리스트 내 내용이 비었나 체크 후 추가
            if insertdata not in list[chkdata]['2']:
                list[chkdata]['2'].append(insertdata)
    elif level == 3:
        if chkdata not in list:
            # 처음넣는경우
            list[chkdata] = {'1': [], '2': [], '3': [], '4': [], '5': []}
            list[chkdata]['3'].append(insertdata)
        else:
            # 추가하는경우, 해당 리스트 내 내용이 비었나 체크 후 추가
            if insertdata not in list[chkdata]['3']:
                list[chkdata]['3'].append(insertdata)

    elif level == 4:
        if chkdata not in list:
            # 처음넣는경우
            list[chkdata] = {'1': [], '2': [], '3': [], '4': [], '5': []}
            list[chkdata]['4'].append(insertdata)
        else:
            # 추가하는경우, 해당 리스트 내 내용이 비었나 체크 후 추가
            if insertdata not in list[chkdata]['4']:
                list[chkdata]['4'].append(insertdata)

    elif level == 5:
        if chkdata not in list:
            # 처음넣는경우
            list[chkdata] = {'1': [], '2': [], '3': [], '4': [], '5': []}
            list[chkdata]['5'].append(insertdata)
        else:
            # 추가하는경우, 해당 리스트 내 내용이 비었나 체크 후 추가
            if insertdata not in list[chkdata]['5']:
                list[chkdata]['5'].append(insertdata)

    elif level == 'h':
        if chkdata not in list:
            # 처음넣는경우
            list[chkdata] = {'1': [], '2': [], '3': [], '4': [], '5': []}
            list[chkdata]['3'].append(insertdata)
        else:
            # 추가하는경우, 해당 리스트 내 내용이 비었나 체크 후 추가
            if insertdata not in list[chkdata]['3']:
                list[chkdata]['3'].append(insertdata)

    return list[chkdata]


if __name__ == '__main__':
    generate_short_addr()

    print 'Python Elapsed %.02f' % (time.time() - t)
