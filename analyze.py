# ===========================================================================
# -*- coding: utf-8 -*-
# lottery_3.py에서 엑셀파일에서 read 하는 부분은 삭제하고
# 인터넷에서 역대 엑셀 당첨번호 파일을 다운받아 그 파일을 read하는 것으로 개발
# read 한 값을 mysql에 저장하도록 개발.
# 또는 인터넷에서 회차별 당처번호를 웹크롤링 하도록 개발 --> 이건 추후
# 이제 db와 tensorflow를 활용하여 분석하고 추천번호를 생성하도록 개발
# import MySQLdb --> 전부 소문자여야함. 
# ===========================================================================
# 2021.12.5 : ModuleNotFoundError: No module named 'PyMySQL' 문제 해결. 소문자 이슈
#             db connect 문제 해결 : markb.의 비밀번호 변경함
# 2021.12.6 : 맥 local의 mariadb에 t_test 테이블을 생성하고 
#             여기에 6개의 랜덤번호를 insert하는 기능을 개발해 보기로 함
# 

import random
import pymysql as pymysql

db = pymysql.connect(host="localhost",user="markb.",passwd="Kcs@1756!",db="test")
curs = db.cursor()

myRandom = random
myList = []
chkVal = 0

for i in range(0,6) :
    if i == 0 :
        myList.append(1)
    myList.append(myRandom.randint(0,45))

sql = "insert into t_test(lot_no, 1st_no, 2nd_no, 3rd_no, 4th_no, 5th_no, 6th_no) values (%s,%s,%s,%s,%s,%s,%s)"

print(myList)
print (sql)

curs.execute(sql, myList)
db.commit()

select_sql = "select * from t_test"
curs.execute(select_sql)
result = curs.fetchall()
print(result)