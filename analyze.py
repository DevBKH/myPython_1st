# lottery_3.py에서 엑셀파일에서 read 하는 부분은 삭제하고
# 인터넷에서 역대 엑셀 당첨번호 파일을 다운받아 그 파일을 read하는 것으로 개발
# read 한 값을 mysql에 저장하도록 개발.
# 또는 인터넷에서 회차별 당처번호를 웹크롤링 하도록 개발 --> 이건 추후
# 이제 db와 tensorflow를 활용하여 분석하고 추천번호를 생성하도록 개발

import MySQLdb

db = MySQLdb.connect(host="localhost",user="bkh",passwd="1234!",db="mydb")
#db = MySQLdb.connect(host="localhost",user="bkh",passwd="1234!",db="mydb")


aaa
