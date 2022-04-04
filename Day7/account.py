"""
- 속성
    ano: 문자열 6글자, '123456'
    owner: 문자열
    balance: 잔액, 비공개 속성 

- Method
    생성자
    deposit(amount) 잔액이 1000만원 이상이면 입금할 수 없음
    withdraw(amount) 잔액이 0원 미만이면 출금할 수 없음
    출력 가능하게(__str__)
"""
class Account:
    def __init__(self, ano, owner, balance):
        self.ano = ano
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount + self.__balance >= 10000000:
            print('천만원 이상은 잔액으로 가져갈 수 없습니다.')
            return
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print('잔액이 부족합니다.')
            return
        self.__balance -= amount

    def __str__(self):
        return f'계좌번호: {self.ano}, 소유주: {self.owner}, 잔액: {self.__balance:9,d}'

acc_list = []    
def check_duplicate(ano):
    for acc in acc_list:
        if ano == acc.ano:
            return True
    return False

# 사용자로부터 필요한 정보를 입력 받아서 계좌를 생성함
def create_account():
    while True:
        s = input('계좌번호 성명 금액> ').split()
        ano, owner = s[0], s[1]
        amount = int(s[2])
        if not check_duplicate(ano):
            break
    acc = Account(ano, owner, amount)
    acc_list.append(acc)

# 사용자로부터 필요한 정보를 입력 받아서 계좌에 돈을 입금함
def deposit_account():
    s = input('계좌번호 금액> ').split()
    ano, amount = s[0], int(s[1])
    for acc in acc_list:
        if acc.ano == ano:
            acc.deposit(amount)
            return

# 사용자로부터 필요한 정보를 입력 받아서 계좌에서 돈을 출금함
def withdraw_account():
    s = input('계좌번호 금액> ').split()
    ano, amount = s[0], int(s[1])
    for acc in acc_list:
        if acc.ano == ano:
            acc.withdraw(amount)
            return

while True:
    menu = int(input('1:계좌생성, 2:계좌목록, 3:입금, 4:출금, 5:종료> '))
    if menu == 5:
        break
    if menu == 1:
        create_account()
    elif menu == 2:
        for account in acc_list:
            print(account)
    elif menu == 3:
        deposit_account()
    elif menu == 4:
        withdraw_account()
    else:
        print('잘못된 명령어입니다.')

    print()