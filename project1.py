print('Расход топлива калькулятор');
km = float(input('Сколько километров: '));
rashod = float(input('Какой расход топлива: '));
cena = float(input('Цена топлива за литр: '));
result = (km * rashod) /100 * cena;
print(f'Стоимость поездки будет: {result:.2f} $');