# -*- coding: utf-8 -*-


class AddrTreeNode(object):
    '''
    트리의 각 노드 클래스.
    '''
    def __init__(self, key, value, *children):
        self.__key__ = key  # node ID
        self.__value__ = value  # address term
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
    def children(self):
        return self.__children__

    # hide children setter property
    '''
    @children.setter
    def children(self, value):
        if list is not type(value):
            print '[AddrTreeNode::children.setter] no type other than list is'\
                ' allowed for children.'
            return  # error
        self.__children__ = value
    '''

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
        if None == child or AddrTreeNode != type(child):
            print '[AddrTreeNode::addChild] only valid AddrTreeNode argument is allowed'
            return  # error

        self.__children__.append(child)
        self.__subTreeSize__ += 1

    def deleteChild(self, child):
        if None == child or AddrTreeNode != type(child):
            print '[AddrTreeNode::deleteChild] only valid AddrTreeNode argument is allowed'
            return  # error

        try:
            self.__children__.remove(child)
            self.__subTreeSize__ -= 1
        except ValueError as ve:
            print '[AddrTreeNode::deleteChild] ValueError: [{0}] [{1}]'.format(child, ve.message)
            raise ve
        except Exception as e:
            print '[AddrTreeNode::deleteChild] Exception: [{0}]'.format(e.message)
            raise e
