# coding=utf-8

import re


def do_cleansing(addr):
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
                if not (u'읍' in addr[after_item_idx] or \
                    u'면' in addr[after_item_idx] or \
                    u'리' in addr[after_item_idx] or \
                    u'동' in addr[after_item_idx] or \
                    u'가' in addr[after_item_idx] or \
                    u'산' in addr[after_item_idx] or \
                    u'길' in addr[after_item_idx] or \
                    u'로' in addr[after_item_idx] or \
                    u'번' in addr[after_item_idx] or \
                    u'층' in addr[after_item_idx]):
                    return addr[:addr.find(item) + len(item)]
        return addr

    addr = remove_bracket_with_contents(addr)
    addr = remove_special_character(addr)
    addr = remove_useless(addr)
    addr = remove_whitespaces(addr)
    return addr


# if __name__ == '__main__':
#     addr_list = [
#         u"경남 김해시 신문동 1414 김해관광유통단지 1B 4L번지 3층"
#     ]
#
#     for addr in addr_list:
#         print 'INPUT: ' + addr
#         print 'OUTPUT: ' + do_cleansing(addr)
#
#     import psycopg2
#     import psycopg2.extras
#
#     DB_HOST = u'211.234.111.33'
#     DB_PORT = u'5433'
#     DB_DATABASE = u'jarvisv1'
#     DB_USER = u'kiwiple'
#     DB_PASSWORD = u'herb##140'
#
#     conn = psycopg2.connect(host=DB_HOST
#                             , port=DB_PORT
#                             , database=DB_DATABASE
#                             , user=DB_USER
#                             , password=DB_PASSWORD
#                             , cursor_factory=psycopg2.extras.DictCursor
#                 )
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT id, addr
#         FROM poi_temp
#         ORDER BY random()
#         LIMIT 500
#     """)
#     result_list = cursor.fetchall()
#
#     for row in result_list:
#         id = str(row['id'])
#         raw_addr = row['addr'].decode('utf-8')
#         print '[input]', raw_addr
#         print '[ouput]', do_cleansing(raw_addr)
#
#     cursor.close()
