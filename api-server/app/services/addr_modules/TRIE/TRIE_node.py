# -*- coding: utf-8 -*-


class TrieNode(object):
    '''
    TRIE 트리의 각 노드 클래스. addr_tree_node 를 참고로 구현.
    '''
    def __init__(self, key, value, isEnd, *children):
        self.__key__ = key
        self.__value__ = value
        self.__isEnd__ = isEnd
        self.__children__ = list(children)
        self.__subTreeSize__ = 0

    @property
    def key(self):
        return self.__key__

    @key.setter
    def key(self, value):
        self.__key__ = value

    @property
    def value(self):
        return self.__value__

    @value.setter
    def value(self, value):
        self.__value__ = value

    @property
    def isEnd(self):
        return self.__isEnd__

    @isEnd.setter
    def isEnd(self, value):
        self.__isEnd__ = value

    @property
    def children(self):
        return self.__children__

    @property
    def countOfDescendents(self):
        return self.__subTreeSize__

    @countOfDescendents.setter
    def countOfDescendents(self, value):
        self.__subTreeSize__ = value

    def __eq__(self, other):
        # return self.__dict__ == other.__dict__
        return None != other and self.__key__ == other.key and self.__value__ == other.value  # do not compare children

    def addChild(self, child):
        if None == child or TrieNode != type(child):
            print '[TrieNode::addChild] only valid TrieNode argument is allowed'
            return  # error

        self.__children__.append(child)
        self.__subTreeSize__ += 1

    def deleteChild(self, child):
        if None == child or TrieNode != type(child):
            print '[TrieNode::deleteChild] only valid TrieNode argument is allowed'
            return  # error

        try:
            self.__children__.remove(child)
            self.__subTreeSize__ -= 1
        except ValueError as ve:
            print '[TrieNode::deleteChild] ValueError: [{0}] [{1}]'.format(child, ve.message)
            raise ve
        except Exception as e:
            print '[TrieNode::deleteChild] Exception: [{0}]'.format(e.message)
            raise e
