# coding=utf-8
"""
AddrTreeBuilder 로 생성한 트리를 탐색하거나 이용하는 메소드들을 기술
"""

from app.services.addr_modules.addr_tree.addr_tree_build import ROOT_VALUE


def print_tree(root_node, depth=0):
    """
    입력받은 노드 이하 모든 노드 출력합니다.
    """

    if ROOT_VALUE == root_node.value:
        print '======================= TREE BEGIN ======================='

    for child in root_node.children:
        print child.value
        print_tree(child, depth + 1)

    if ROOT_VALUE == root_node.value:
        print '======================== TREE END ========================'


def get_depth(root_node, addr_str):
    """
    깊이 추출기, 주소를 넣으면 자료와 대조하여 깊이를 반환합니다.
    """

    tree_depth = 0
    term_list = addr_str.split()

    current_node = root_node
    for term in term_list:
        # 트리 탐색
        for idx, child in enumerate(current_node.children):
            if term == child.value:
                current_node = child
                tree_depth += 1
                break
        # 반복정리 결과값이 없으면 끝처리
        if (idx + 1) == len(current_node.children) and term != child.value:
            break
    return tree_depth


# if __name__ == '__main__':
#     print "///--Start--addr_tree_common.py--///"
#     # 메인 시작,AddrTreeBuilder() 불러와서 builder로 생성
#     from app.services.addr_modules.addr_tree.addr_tree_build import AddrTreeBuilder
#
#     builder = AddrTreeBuilder()
#
#     # 파일 선택 ㅣ filePath 에 GovAddrSet_Jibeon.txt 를 넣으면 지번주소트리가 생성되고 GovAddrSet_Road.txt 를 넣으면 도로명주소트리가 생성됨.
#
#     filepath = 'addr_set_data/GovAddrSet_Jibeon.txt'
#     # filepath = 'addr_set_data/GovAddrSet_Road.txt'
#
#     root_node = builder.buildAddrTree(filepath)  # 선택한 파일로
#
#     # print "트리출력"
#     # print_tree(root_node)  # 노드인덱스를 넣으면 그 노드 이하의 트리를 탐색하여 print
#
#     address_str = u"경기도 수원시 팔달구 북수동"
#     print 'INPUT :', address_str
#
#     depth = get_depth(root_node, address_str)  # 주소 스트링을 넣으면 depth 를 리턴
#     print 'depth :', str(depth)

