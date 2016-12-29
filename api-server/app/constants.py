# -*- coding: utf-8 -*-

import os


CODE_200 = 200
MSG_200 = u"success"

CODE_400 = 400
MSG_400 = u"A required parameter was missing or a parameter was malformed."

# CODE_401 = 401
# MSG_401 = u"올바른 키를 입력해 주세요."
#
# CODE_404 = 404
# MSG_404 = u"찾을 수 없는 요청입니다."

CODE_500 = 500
MSG_500 = u"서비스에 문제가 있습니다. 잠시 뒤에 시도해 주세요."

MIME_TYPE_APPLICATION_JSON = "application/json"

ITEMS_PER_PAGE = 30

JUSO_API_URL = 'http://www.juso.go.kr/addrlink/addrLinkApi.do'
JUSO_API_KEY = 'U01TX0FVVEgyMDE1MDIxMTE1MzYwNA=='

PROJECT_APP_DIR = os.path.abspath(os.path.dirname(__file__))

ADDR_JIBEON_SET_FILEPATH = os.path.join(PROJECT_APP_DIR, 'services/addr_modules/addr_tree/addr_set_data/GovAddrSet_Jibeon.txt')
ADDR_ROAD_SET_FILEPATH = os.path.join(PROJECT_APP_DIR, 'services/addr_modules/addr_tree/addr_set_data/GovAddrSet_Road.txt')

TRIE_DICT_FOLDERPATH = os.path.join(PROJECT_APP_DIR, 'services/addr_modules/TRIE/data/')
TRIE_GOVDIC_FILEPATH = os.path.join(PROJECT_APP_DIR, 'services/addr_modules/TRIE/data/GovDic.txt')
TRIE_USERDIC_FILEPATH = os.path.join(PROJECT_APP_DIR, 'services/addr_modules/TRIE/data/UserDic.txt')

SHORT_ADDR_SET_FILEPATH = os.path.join(PROJECT_APP_DIR, 'services/addr_modules/ShortAddr.json')
