import os
import sys
import datetime

def new_trip():
    print('=== Расход топлива калькулятор ===');

    distance = float(input('Введите количество километров: '));
    while distance < 0:
        print('Ошибка!')
        distance = float(input('Введите количество километров еще раз: '))

    rashod = float(input('Введите расход топлива(л/100): '));
    while rashod < 0:
        print('Ошибка!')
        rashod = float(input('Введите расход топлива еще раз(л/100): '))
        
    toplivo = input('Какое у вас топливо бензин или дизель?')
    cena = float(input('Введите цену топлива за литр($): '));

    litry = (distance * rashod) /100;
    result = litry * cena;

    dateTime = datetime.datetime.now()

    print()
    print(dateTime.strftime("%x"))
    print(dateTime.strftime("%X"))
    print(f'Дистанция поездки: {distance:.2f}')
    print(f'Расход топлива: {rashod:.2f} (л/100)')
    print(f'Вид топлива: {toplivo}')
    print(f'Цена топлива за литр: {cena:.2f} $')
    print(f"Будет израсходовано: {litry:.2f} л")
    print(f"Стоимость поездки: {result:.2f} €")

    text = f"""
        === Результат ===
        Дата: {dateTime.strftime("%x")}
        Время: {dateTime.strftime("%X")}
        Дистанция поездки: {distance:.2f}
        Расход топлива: {rashod:.2f}
        Вид топлива: {toplivo}
        Цена топлива: {cena:.2f} $
        Будет израсходовано: {litry:.2f} л
        Стоимость поездки: {result:.2f} €
        ===========================
        """

    f = open('historyTrip.txt', 'a', encoding='utf-8')
    f.write(text)
    f.close()

while True:
    print('======== Trip Cost ========')
    print('1. Новая поездка')
    print('2. История поездок')
    print('3. Выход')

    menu = input('Выберите пункт: ')

    if menu == '1':
        new_trip()
        print()

    elif menu == '2':
        os.system('historyTrip.txt')
        print()

    elif menu == '3':
        print('До новых встреч!!')
        sys.exit()
        print()
        break
        
    else:
        print('Неверный пункт меню')
        print()


