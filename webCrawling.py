# -*- coding: utf-8 -*-
# web crawling 테스트
# 아래 url이 유효하지 않음.

import requests
from bs4 import BeautifulSoup

def main() :
    basic_url = "https://www.nlotto.co.kr/lotto645Confirm.do?method=byWin&drwNo="
    for i in range(1, 707) :
        resp = requests.get(basic_url+str(i))
        soup = BeautifulSoup(resp.text, "lxml")
        line = str(soup.find("meta", {"id" : "desc", "name" : "description"})['content'])
        print(line)

if __name__ == "__main__" :
    main()
