#카페 만들기

import time

#변수 설정
total_sales = 0
wallet = 10000 #잔액
menu_names = ["에스프레소", "아메리카노", "카페라떼  ", "바닐라라떼"] #메뉴
menu_prices = [2000, 2000, 3000, 3500] #가격
menu_stocks = [10, 10, 10, 10] #재고

#함수 설계
def show_menu():
    print("="*30)
    print(" "*10+"안녕 커피"+" "*10)
    print("="*30)
    for i in range(len(menu_names)):
        print(f"{i+1}. {menu_names[i]} - {menu_prices[i]}원 (재고: {menu_stocks[i]})")
    print("="*30)

def order():
    global wallet, total_sales
    while True:
        try:
            choice = int(input("메뉴 번호(취소는 0): "))
        except ValueError:
            print("(1~4)의 숫자를 입력해주세요")
            continue
        if choice == 0: break
        if not (1 <= choice <= len(menu_names)):
            print("해당 번호의 메뉴가 없습니다.")
            continue

        amount = int(input("수량: "))
        idx = choice - 1
        choice_name = menu_names[idx]
        choice_price = menu_prices[idx]
        choice_stock = menu_stocks[idx]
        total_price = choice_price * amount

        if amount > choice_stock:
            print(f"재고가 부족합니다. (현재 재고: {choice_stock})")
            continue
        if total_price > wallet:
            print(f"잔액이 부족합니다. (필요 금액: {total_price}원 / 현재 잔액: {wallet}원)")
            continue
        else:
            brew_coffee(choice_name, amount)
            wallet -= total_price        
            menu_stocks[idx] -= amount
            total_sales += total_price
            break

def brew_coffee(name, count):
    print(f"\n{name} {count}잔 주문 성공!")
    print("제조 중...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(0.5)
    print("\n음료가 나왔습니다!")

def charge_wallet():
    global wallet
    print("\n" + "="*30)
    money = int(input("충전할 금액을 입력하세요: "))

    if money > 0:
        wallet += money
        print(f"{money}원이 충전되었습니다.")
        print(f"현재 잔액: {wallet}원")
    else:
        print("0원보다 큰 금액을 입력해주세요.")
    print("="*30)

def fill_stock():
    print("\n관리자 모드: 모든 재고를 10개로 초기화합니다.")
    for i in range(len(menu_stocks)):
        menu_stocks[i] = 10
    print("모든 메뉴의 재고가 충전되었습니다.")

#메인 실행부
while True:
    print(f"\n[현재 내 잔액: {wallet}원]")
    print("1. 메뉴보기/주문 | 2. 잔액충전 | 3. 재고채우기(관리자) | 4. 종료")
    menu_choice = input("원하는 서비스 번호를 입력하세요: ")

    if menu_choice == '1':
        show_menu()
        order()
    elif menu_choice == '2':
        charge_wallet()
    elif menu_choice == '3':
        fill_stock()
    elif menu_choice == '4':
        print(f"프로그램을 종료합니다. 오늘 카페 총 매출은 [{total_sales}]원 입니다!")
        time.sleep(2)
        break
    else:
        print("잘못된 번호입니다. 다시 선택해주세요")

