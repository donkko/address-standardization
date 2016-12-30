# -*- coding: utf-8 -*-

import gc
import codecs
from app.services.addr_modules.addr_tree.addr_tree_node import AddrTreeNode


# the value for the root node
ROOT_VALUE = u'ROOT'


class AddrTreeBuilder(object):
    '''
    AddrTreeNode 를 잎으로 하는 주소트리를 생성하는 클래스.
    '''

    def __init__(self):
        self.__inputAddrSetFilePath__ = None
        self.__root__ = None

    @property
    def treeRoot(self):
        return self.__root__

    def buildAddrTree(self, inputAddrSetFilePath):

        self.__inputAddrSetFilePath__ = inputAddrSetFilePath
        self.__root__ = AddrTreeNode(0, ROOT_VALUE)

        addrLineSet = set()

        numAddrLines = 0
        with codecs.open(self.__inputAddrSetFilePath__, 'r', encoding='utf-8') as inputF:
            for line in inputF:
                numAddrLines += 1
                addrLineSet.add(line.strip())
        print "[AddrTreeBuilder::buildAddrTree] address file <{0}> closed? <{1}>, how many addresses? <{2}>"\
            .format(self.__inputAddrSetFilePath__, inputF.closed, numAddrLines)
        addrLineList = sorted(addrLineSet)

        del addrLineSet

        gc.collect()

        print '[AddrTreeBuilder::buildAddrTree] total # of unique addresses:<{0}>'.format(len(addrLineList))

        stack = [self.__root__]
        curNodeID = 0

        for addrLine in addrLineList:
            termList = addrLine.split()
            stackIdx = 1  # for the case the stack is empty at first
            for stackIdx in range(1, len(stack)):
                if stackIdx > len(termList):
                    break
                if stack[stackIdx].value != termList[stackIdx - 1]:
                    break
            if len(stack) - 1 > len(termList):
                for _ in range(stackIdx, len(stack)):
                    node = stack.pop()
                    node.countOfDescendents = curNodeID - node.key
            elif len(stack) - 1 <= len(termList):
                if stackIdx == len(stack) - 1 and stack[stackIdx].value == termList[stackIdx - 1]:
                    stackIdx += 1
                else:
                    pass
                for _ in range(stackIdx, len(stack)):
                    node = stack.pop()
                    node.countOfDescendents = curNodeID - node.key
            for i in range(stackIdx - 1, len(termList)):
                curNodeID += 1
                child = AddrTreeNode(curNodeID, termList[i])
                parent = stack[len(stack) - 1]
                parent.addChild(child)
                stack.append(child)

        while 0 < len(stack):
            node = stack.pop()
            node.countOfDescendents = curNodeID - node.key

        print '[AddrTreeBuilder::buildAddrTree] # of total nodes:<{0}>'.format(curNodeID)

        del addrLineList
        gc.collect()

        return self.__root__


if __name__ == '__main__':
    from app.constants import ADDR_JIBEON_SET_FILEPATH
    from app.constants import ADDR_ROAD_SET_FILEPATH
    
    builder = AddrTreeBuilder()
    builder.buildAddrTree(ADDR_JIBEON_SET_FILEPATH)
    #builder.buildAddrTree(ADDR_ROAD_SET_FILEPATH)
