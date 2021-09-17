a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
op = input('Введите операцию +, -, *, /:')
if op == '+':
    c = a + b
    print(c)
elif op == '-':
    c = a - b
    print(c)
elif op == '*':
    c = a * b
    print(c)
elif op == '/':
    c = a / b
    print(c)
else:
    print("Неизвестная операция")


