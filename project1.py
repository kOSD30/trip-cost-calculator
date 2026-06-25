print('=== Расход топлива калькулятор ===');

distance = float(input('Введите количество километров: '));
rashod = float(input('Введите расход топлива(л/100): '));
cena = float(input('Введите цену топлива за литр($): '));

litry = (distance * rashod) /100;
result = litry * cena;

print(f"\nБудет израсходовано: {litry:.2f} л")
print(f"Стоимость поездки: {result:.2f} €")