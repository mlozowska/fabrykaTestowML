def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Wybierz operację.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    choice = input("Wybierz operację(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):

        num_1 = float(input("Podaj pierwszą liczbę: "))
        num_2 = float(input("Podaj drugą liczbę: "))

        if choice == '1':
            print(f'{num_1} + {num_2} =',
                  add(num_1, num_2))
        elif choice == '2':
            print(f'{num_1} - {num_2} =',
                  subtract(num_1, num_2))
        elif choice == '3':
            print(f'{num_1} * {num_2} =',
                  multiply(num_1, num_2))
        elif choice == '4':
            print(f'{num_1} / {num_2} =',
                  divide(num_1, num_2))
        break
    else:
        print("Błędna wartość, podaj poprawną")
