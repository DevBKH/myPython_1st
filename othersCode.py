from random import *
import time, os

class lotto:
    cnt = 0
    def __init__(self):
        lotto.cnt += 1
        self.mylotto = []
        for i in range(int(input('로또를 몇개 구매하시겠습니까?: '))):
            self.mylotto.append(self.__lotto_pop()[:6])
        print('\n- {}회 차 로또 구매 내역 -'.format(lotto.cnt))
        for i in self.mylotto:
            print('\t{:2} {:2} {:2} {:2} {:2} {:2}'.format(*i))
        print()

    def lucky(self):
        self.lucky_number = self.__lotto_pop()
        print('- {}회 차 로또 당첨 번호 -'.format(lotto.cnt))
        print('\t{:2} {:2} {:2} {:2} {:2} {:2}, 보너스 번호: {:2}'.format(*self.lucky_number[:6],self.lucky_number[-1]))
        self.__match_lucky()

    def __match_lucky(self):
        print('\n- {}회 차 로또 당첨 확인 -'.format(lotto.cnt))
        self.rank = [0,0,0,0,0]

        for i in self.mylotto:
            num_match = len(set(i)&set(self.lucky_number[:6]))

            if num_match == 6:
                print('\t{:2} {:2} {:2} {:2} {:2} {:2}'.format(*i[:6]),end=' >>> ')
                print('1등 당첨 축하드립니다. 일생의 운을 다 쓰셨습니다.')
                self.rank[0] += 1
            elif num_match == 5 and self.lucky_number[-1] in i:
                print('\t{:2} {:2} {:2} {:2} {:2} {:2}'.format(*i[:6]),end=' >>> ')
                print('2등 당첨 축하드립니다. 콩라인에 오신걸 환영합니다.')
                self.rank[1] += 1
            elif num_match >= 3:
                print('\t{:2} {:2} {:2} {:2} {:2} {:2}'.format(*i[:6]),end=' >>> ')
                print('{}등 당첨 축하드립니다.'.format(8 - num_match))
                self.rank[8-num_match-1] += 1
        print()
        if self.rank == [0]*5: print('\t모두 꽝입니다. 호갱님')
        for i in range(5):
            if self.rank[i] != 0: print('\t{}등 당첨: {}개'.format(i+1,self.rank[i]))

    @staticmethod
    def __lotto_pop():
        return sample(range(1,46),7)

if __name__ == '__main__':
    while 1:
        os.system('cls')

        buy_lotto = lotto()
        for i in reversed(range(3)):
            print('.'*(i+1),'{}'.format(i+1))
            time.sleep(1)
        print()
        buy_lotto.lucky()
        if input('\n계속하시겠습니까? y/n: ') == 'n': break
