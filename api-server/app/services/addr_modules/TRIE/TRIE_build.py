# -*- coding: utf-8 -*-

import gc
import codecs
import os
from app.services.addr_modules.TRIE.TRIE_node import TrieNode


# the value for the root node
ROOT_VALUE = u'ROOT'


class TrieTreeBuilder(object):
    '''
    TrieNode 를 노드로 하는 TRIE 트리를 생성하는 클래스. addr_tree_build 를 참고로 구현.
    '''

    def __init__(self):
        self.__inputTrieDictSetFilePath__ = None
        self.__root__ = None

    @property
    def treeRoot(self):
        return self.__root__

    def buildTrieTree(self, inputTrieDictSetFolderPath):

        self.__inputTrieDictSetFilePath__ = inputTrieDictSetFolderPath
        self.__root__ = TrieNode(0, ROOT_VALUE, 0)

        trieLineSet = set()

        numTrieLines = 0
        for file_name in os.listdir(self.__inputTrieDictSetFilePath__):
            with codecs.open(self.__inputTrieDictSetFilePath__ + '/' + file_name, 'r', encoding='utf-8') as inputF:
                for line in inputF:
                    numTrieLines += 1
                    trieLineSet.add(line.strip())
        print "[TrieTreeBuilder::buildTrieTree] how many items in trie dicts(GovDic.txt, UserDic.txt)? <{0}>"\
            .format(numTrieLines)
        trieLineList = sorted(trieLineSet)

        del trieLineSet

        gc.collect()

        print '[TrieTreeBuilder::buildTrieTree] total # of unique trie items in dict:<{0}>'.format(len(trieLineList))

        stack = [self.__root__]
        curNodeID = 0

        for trieLine in trieLineList:
            char_list = []
            char_list += trieLine
            stackIdx = 1  # for the case the stack is empty at first
            for stackIdx in range(1, len(stack)):
                if stackIdx > len(char_list):
                    break
                if stack[stackIdx].value != char_list[stackIdx - 1]:
                    break
            if len(stack) - 1 > len(char_list):
                for _ in range(stackIdx, len(stack)):
                    node = stack.pop()
                    node.countOfDescendents = curNodeID - node.key
            elif len(stack) - 1 <= len(char_list):
                if stackIdx == len(stack) - 1 and stack[stackIdx].value == char_list[stackIdx - 1]:
                    stackIdx += 1
                else:
                    pass
                for _ in range(stackIdx, len(stack)):
                    node = stack.pop()
                    node.countOfDescendents = curNodeID - node.key
            for i in range(stackIdx - 1, len(char_list)):
                curNodeEndState = 1 if i == len(char_list) - 1 else 0
                curNodeID += 1
                child = TrieNode(curNodeID, char_list[i], curNodeEndState)
                parent = stack[len(stack) - 1]
                parent.addChild(child)
                stack.append(child)

        while 0 < len(stack):
            node = stack.pop()
            node.countOfDescendents = curNodeID - node.key

        print '[TrieTreeBuilder::buildTrieTree] # of total nodes:<{0}>'.format(curNodeID)

        del trieLineList
        gc.collect()

        return self.__root__

if __name__ == '__main__':
    trieTreeBuilder = TrieTreeBuilder()
    trieTreeBuilder.buildTrieTree('data')
