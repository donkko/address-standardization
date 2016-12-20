# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os, codecs
import psycopg2
import psycopg2.extras

DB_HOST = u'127.0.0.1'
DB_PORT = u'1234'
DB_DATABASE = u'dbname'
DB_USER = u'username'
DB_PASSWORD = u'password'


INPUT_DATA_DIRECTORY = './raw_data'


def main():
    for each_file_name in os.listdir(INPUT_DATA_DIRECTORY):
        with codecs.open(INPUT_DATA_DIRECTORY + '/' + each_file_name, 'r', 'euc-kr', 'ignore') as f:
            conn = psycopg2.connect(host=DB_HOST
                        , port=DB_PORT
                        , database=DB_DATABASE
                        , user=DB_USER
                        , password=DB_PASSWORD
                        , cursor_factory=psycopg2.extras.DictCursor
            )
            cursor = conn.cursor()

            batch_count = 0
            for line in f:
                term_list = line.split('|')
                term_dict = {
                    'bubjung_code_id': term_list[0],
                    'province_name': term_list[1],
                    'county_name': term_list[2],
                    'town_name': term_list[3],
                    'village_name': term_list[4],
                    'is_mountain': term_list[5],
                    'jibeon_main_no': term_list[6],
                    'jibeon_sub_no': term_list[7],
                    'road_code_id': term_list[8],
                    'road_name': term_list[9],
                    'is_basement': term_list[10],
                    'road_main_no': term_list[11],
                    'road_sub_no': term_list[12],
                    'building_name': term_list[13],
                    'building_name_detail': term_list[14],
                    'building_code_id': term_list[15],
                    'town_class': term_list[16],
                    'jibeon_code_id': term_list[17],
                    'jibeon_name': term_list[18],
                    'post_code': term_list[19],
                    'post_serial_code': term_list[20],
                    'multiple_deliveriable_place_name': term_list[21],
                    'move_reason_code': term_list[22],
                    'road_created_at': term_list[23],
                    'old_road_addr': term_list[24],
                    'building_name_for_county': term_list[25],
                    'is_shared_house': term_list[26]
                }
                #
                # select_where_clause_list = []
                # select_where_clause_list.append("bubjung_code_id = %(bubjung_code_id)s") if term_dict['bubjung_code_id'] else ""
                # select_where_clause_list.append("province_name = %(province_name)s") if term_dict['province_name'] else ""
                # select_where_clause_list.append("county_name = %(county_name)s") if term_dict['county_name'] else ""
                # select_where_clause_list.append("town_name = %(town_name)s") if term_dict['town_name'] else ""
                # select_where_clause_list.append("village_name = %(village_name)s") if term_dict['village_name'] else ""
                # select_where_clause_list.append("is_mountain = %(is_mountain)s") if term_dict['is_mountain'] else ""
                # select_where_clause_list.append("jibeon_main_no = %(jibeon_main_no)s") if term_dict['jibeon_main_no'] else ""
                # select_where_clause_list.append("jibeon_sub_no = %(jibeon_sub_no)s") if term_dict['jibeon_sub_no'] else ""
                # select_where_clause_list.append("road_code_id = %(road_code_id)s") if term_dict['road_code_id'] else ""
                # select_where_clause_list.append("road_name = %(road_name)s") if term_dict['road_name'] else ""
                # select_where_clause_list.append("is_basement = %(is_basement)s") if term_dict['is_basement'] else ""
                # select_where_clause_list.append("road_main_no = %(road_main_no)s") if term_dict['road_main_no'] else ""
                # select_where_clause_list.append("road_sub_no = %(road_sub_no)s") if term_dict['road_sub_no'] else ""
                # select_where_clause_list.append("building_name = %(building_name)s") if term_dict['building_name'] else ""
                # select_where_clause_list.append("building_name_detail = %(building_name_detail)s") if term_dict['building_name_detail'] else ""
                # select_where_clause_list.append("building_code_id = %(building_code_id)s") if term_dict['building_code_id'] else ""
                # select_where_clause_list.append("town_class = %(town_class)s") if term_dict['town_class'] else ""
                # select_where_clause_list.append("jibeon_code_id = %(jibeon_code_id)s") if term_dict['jibeon_code_id'] else ""
                # select_where_clause_list.append("jibeon_name = %(jibeon_name)s") if term_dict['jibeon_name'] else ""
                # select_where_clause_list.append("post_code = %(post_code)s") if term_dict['post_code'] else ""
                # select_where_clause_list.append("post_serial_code = %(post_serial_code)s") if term_dict['post_serial_code'] else ""
                # select_where_clause_list.append("multiple_deliveriable_place_name = %(multiple_deliveriable_place_name)s") if term_dict['multiple_deliveriable_place_name'] else ""
                # select_where_clause_list.append("move_reason_code = %(move_reason_code)s") if term_dict['move_reason_code'] else ""
                # select_where_clause_list.append("road_created_at = %(road_created_at)s") if term_dict['road_created_at'] else ""
                # select_where_clause_list.append("old_road_addr = %(old_road_addr)s") if term_dict['old_road_addr'] else ""
                # select_where_clause_list.append("building_name_for_county = %(building_name_for_county)s") if term_dict['building_name_for_county'] else ""
                # select_where_clause_list.append("is_shared_house = %(is_shared_house)s") if term_dict['is_shared_house'] else ""
                #
                # select_where_clause = " AND ".join(select_where_clause_list)
                #
                # cursor.execute("""
                #     SELECT COUNT(*)
                #     FROM addr_gov
                #     WHERE {0}
                # """.format(select_where_clause), term_dict)
                #
                # if cursor.fetchone()[0]:
                #     continue

                set_clause = "bubjung_code_id," if term_dict['bubjung_code_id'] else ""
                set_clause += "province_name," if term_dict['province_name'] else ""
                set_clause += "county_name," if term_dict['county_name'] else ""
                set_clause += "town_name," if term_dict['town_name'] else ""
                set_clause += "village_name," if term_dict['village_name'] else ""
                set_clause += "is_mountain," if term_dict['is_mountain'] else ""
                set_clause += "jibeon_main_no," if term_dict['jibeon_main_no'] else ""
                set_clause += "jibeon_sub_no," if term_dict['jibeon_sub_no'] else ""
                set_clause += "road_code_id," if term_dict['road_code_id'] else ""
                set_clause += "road_name," if term_dict['road_name'] else ""
                set_clause += "is_basement," if term_dict['is_basement'] else ""
                set_clause += "road_main_no," if term_dict['road_main_no'] else ""
                set_clause += "road_sub_no," if term_dict['road_sub_no'] else ""
                set_clause += "building_name," if term_dict['building_name'] else ""
                set_clause += "building_name_detail," if term_dict['building_name_detail'] else ""
                set_clause += "building_code_id," if term_dict['building_code_id'] else ""
                set_clause += "town_class," if term_dict['town_class'] else ""
                set_clause += "jibeon_code_id," if term_dict['jibeon_code_id'] else ""
                set_clause += "jibeon_name," if term_dict['jibeon_name'] else ""
                set_clause += "post_code," if term_dict['post_code'] else ""
                set_clause += "post_serial_code," if term_dict['post_serial_code'] else ""
                set_clause += "multiple_deliveriable_place_name," if term_dict['multiple_deliveriable_place_name'] else ""
                set_clause += "move_reason_code," if term_dict['move_reason_code'] else ""
                set_clause += "road_created_at," if term_dict['road_created_at'] else ""
                set_clause += "old_road_addr," if term_dict['old_road_addr'] else ""
                set_clause += "building_name_for_county," if term_dict['building_name_for_county'] else ""
                set_clause += "is_shared_house" if term_dict['is_shared_house'] else ""

                values_clause = "%(bubjung_code_id)s," if term_dict['bubjung_code_id'] else ""
                values_clause += "%(province_name)s," if term_dict['province_name'] else ""
                values_clause += "%(county_name)s," if term_dict['county_name'] else ""
                values_clause += "%(town_name)s," if term_dict['town_name'] else ""
                values_clause += "%(village_name)s," if term_dict['village_name'] else ""
                values_clause += "%(is_mountain)s," if term_dict['is_mountain'] else ""
                values_clause += "%(jibeon_main_no)s," if term_dict['jibeon_main_no'] else ""
                values_clause += "%(jibeon_sub_no)s," if term_dict['jibeon_sub_no'] else ""
                values_clause += "%(road_code_id)s," if term_dict['road_code_id'] else ""
                values_clause += "%(road_name)s," if term_dict['road_name'] else ""
                values_clause += "%(is_basement)s," if term_dict['is_basement'] else ""
                values_clause += "%(road_main_no)s," if term_dict['road_main_no'] else ""
                values_clause += "%(road_sub_no)s," if term_dict['road_sub_no'] else ""
                values_clause += "%(building_name)s," if term_dict['building_name'] else ""
                values_clause += "%(building_name_detail)s," if term_dict['building_name_detail'] else ""
                values_clause += "%(building_code_id)s," if term_dict['building_code_id'] else ""
                values_clause += "%(town_class)s," if term_dict['town_class'] else ""
                values_clause += "%(jibeon_code_id)s," if term_dict['jibeon_code_id'] else ""
                values_clause += "%(jibeon_name)s," if term_dict['jibeon_name'] else ""
                values_clause += "%(post_code)s," if term_dict['post_code'] else ""
                values_clause += "%(post_serial_code)s," if term_dict['post_serial_code'] else ""
                values_clause += "%(multiple_deliveriable_place_name)s," if term_dict['multiple_deliveriable_place_name'] else ""
                values_clause += "%(move_reason_code)s," if term_dict['move_reason_code'] else ""
                values_clause += "%(road_created_at)s," if term_dict['road_created_at'] else ""
                values_clause += "%(old_road_addr)s," if term_dict['old_road_addr'] else ""
                values_clause += "%(building_name_for_county)s," if term_dict['building_name_for_county'] else ""
                values_clause += "%(is_shared_house)s" if term_dict['is_shared_house'] else ""

                cursor.execute("""
                    INSERT INTO addr_gov ({0})
                    VALUES ({1})
                """.format(set_clause, values_clause), term_dict)

                if batch_count == 100:
                    conn.commit()
                    batch_count = 0

                batch_count += 1

            conn.close()

if __name__ == '__main__':
    main()
