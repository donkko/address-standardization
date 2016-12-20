# coding=utf-8
"""
TRIE_build 로 생성한 트리를 탐색하거나 이용하는 메소드들을 기술
"""

from app.services.addr_modules.TRIE.TRIE_build import ROOT_VALUE
from app.services.addr_modules.TRIE.TRIE_build import TrieTreeBuilder
#from konlpy.utils import pprint

import re

def print_tree(root_node, depth=0):
    for child in root_node.children:
        print child.value, depth
        print_tree(child, depth + 1)


def do_search(addr_str, root_node):
    current_node = root_node
    tmp_term = ""
    tmp_candidate_term_list = []

    for addr_char in addr_str:
        for idx, child in enumerate(current_node.children):
            if addr_char == child.value:
                current_node = child
                tmp_term += addr_char
                if child.isEnd:
                    tmp_candidate_term_list.append(tmp_term)
                    if not child.children and tmp_candidate_term_list:
                        return tmp_candidate_term_list
                break
            else:
                if idx == len(current_node.children) - 1:
                    if tmp_term and tmp_candidate_term_list:
                        return tmp_candidate_term_list
                    else:
                        return []

    if tmp_candidate_term_list:
        return tmp_candidate_term_list
    else:
        return []


def get_split_points(root_node, addr_str):

    bungi = re.search("(\d+-\d+|\d+)$", addr_str).group() if re.search("(\d+-\d+|\d+)$", addr_str) else ''
    addr_str = re.sub(bungi, "", addr_str, 1)
    # print ''
    # print "[get_split_points] addr_str:", addr_str

    result_dic = {'ROOT': None}
    make_dic('ROOT', result_dic, addr_str, root_node)

    # print "[get_split_points] recursive dict:"
    # pprint(result_dic)

    result = []
    dict2combination(result_dic['ROOT'], [], result)

    # print "[get_split_points] final result list:"
    for idx, elem in enumerate(result):
        result[idx] = elem + " " + bungi
        # print result[idx]

    return result


def make_dic(key, result_dic, addr_str, root_node):

    # print "[make_dic] input key:"
    # print key
    # print "[make_dic] input addr_str:"
    # print addr_str
    # print "[make_dic] input result_dic:"
    # pprint(result_dic)


    candidate_list = do_search(addr_str, root_node)

    # print "[make_dic] do_search result:"
    # pprint(candidate_list)
    # print ""

    if len(candidate_list) == 0:
        if addr_str == '':
            result_dic[key] = 'SUCCESS'
            return
        else:
            result_dic[key] = 'FAIL'
            return

    else:
        result_dic[key] = {}
        for candidate in candidate_list:
            result_dic[key][candidate] = None
            make_dic(candidate, result_dic[key], addr_str[len(candidate):], root_node)


def dict2combination(dic, temp_l, result_l):

    # print ""
    # print "INVOKED"
    # print "[dict2combination] input dic:"
    # pprint(dic)
    # print "[dict2combination] input temp_l:"
    # pprint(temp_l)
    # print "[dict2combination] input result_l:"
    # pprint(result_l)
    # print ""

    for k, v in dic.items():
        temp_l.append(k)

        # print ""
        # print "[dict2combination] input dic:"
        # pprint(dic)
        # print "[dict2combination] input temp_l:"
        # pprint(temp_l)
        # print "[dict2combination] input result_l:"
        # pprint(result_l)
        # print ""

        if v == 'FAIL':
            temp_l.pop(-1)
            continue
        elif v == 'SUCCESS':
            result_l.append(" ".join(temp_l))
            temp_l.pop(-1)
            continue
        else:
            dict2combination(dic[k], temp_l, result_l)

        temp_l.pop(-1)


# if __name__ == '__main__':
#     trieTreeBuilder = TrieTreeBuilder()
#     root_node = trieTreeBuilder.buildTrieTree('data')
#
#     test_addr_list = [
#         u'서울강서구화곡6동1104-5'
#     ]
#     for addr in test_addr_list:
#         get_split_points(root_node, addr)

