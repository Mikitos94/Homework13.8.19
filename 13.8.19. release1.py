import os

from colorama import init

init(autoreset=True)
from colorama import Fore, Back, Style

all_price = []  # создали список, в который добавляются все суммы заказов
one_person_price = []  # создали временный список, куда будет добавляться один заказ
x = 1  # создали переменную, для того чтобы цикл выполнялся бесконечно
while x > 0:  # хочу чтобы цикл выполлнялся бесконечно, тем самым постоянно добавлялась сумма в all_price
    try:
        billet = (int(input('Сколько билетов Вы хотите приобрести?:\n')))
        print()
    except:
        print(Fore.RED + 'Введите цифру!!!')
        continue
    p = 1
    while p <= billet:
        try:
            age = (int(input('Введи возраст посетителя ' + (str(p)) + ': ')))
            if age < 18:
                one_person_price.append(0)
            elif 18 <= age < 25:
                one_person_price.append(990)
            elif age >= 25:
                one_person_price.append(1390)
            p = p + 1
        except:
            print(Fore.RED + 'Введите возраст в цифрах!!!')
            continue
    if p - 1 >= 3:  # так как переменная из предыдущей строки приплюсовывает 1, здесь мы вычитаем этот 1
        one_person_price_sale = (int(sum(one_person_price))) * 90 // 100
        all_price.append(one_person_price_sale)
        print('Ваша итоговая сумма с учетом 10% скидки равна: ' + (str(int(one_person_price_sale))))
        del one_person_price_sale
    elif p - 1 < 3:
        all_price.append(sum(one_person_price))
        print('Ваша итоговая сумма равна: ' + (str(sum(one_person_price))))
    one_person_price.clear()
    print(Back.GREEN + 'Общая сумма всех билетов равна: ' + (str(sum(all_price))))
    input('Для продолжения нажми Enter')
    os.system('cls||clear')
