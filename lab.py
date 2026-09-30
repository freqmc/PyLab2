def pwd_check(pwd):
    errors = []
    if len(pwd) < 8: errors.append("Длина пароля меньше 8 символов")
    if not any(char.isupper() for char in pwd): errors.append("Отсутствуют заглавные буквы")
    if not any(char.islower() for char in pwd): errors.append("Отсутствуют строчные буквы")
    if not any(char.isdigit() for char in pwd): errors.append("Отсутствуют цифры")

    if not errors: print("Пароль надёжный")
    else: print("Пароль ненадёжный")
    for error in errors:
        print(error)

def calc(a, b, op):
    try:
        match op:
            case "+": print(f"Значение выражения a+b вычислено при a={a}, b={b}\nРезультат равен {a+b}")
            case "-": print(f"Значение выражения a-b вычислено при a={a}, b={b}\nРезультат равен {a - b}")
            case "*": print(f"Значение выражения a*b вычислено при a={a}, b={b}\nРезультат равен {round(a * b, 1)}")
            case "/":
                try:
                    print(f"Значение выражения a/b вычислено при a={a}, b={b}\nРезультат равен {round(a / b, 1)}")
                except ZeroDivisionError:
                    print("Деление на ноль невозможно")
            case _: print("Неизвестная операция")
    except ValueError:
        print("Введены некорректные данные")

def print7():
    for i in range(0, 501, 7):
        print(i)

def print7_mod():
    for i in range(0, 501, 7):
        if i > 300:
            break
        if i % 14 == 0:
            continue
        print(i)

def hooks(text):
    print(f"Текст из скобок:{text[text.find("(")+1:text.find(")")]}")

def comma_count(text):
    print(f"Количество точек={text.count(".")}\nКоличество запятых={text.count(",")}")

def space_a_count(text):
    count = 0
    for word in text.split():
        if word.lower().startswith("а"):
            count+=1
    print(f"Всего слов, начинающихся с а {count}")

def equal_to_space(text):
    print(f"{text.replace(" ", "=")}\nВсего {text.count(" ")} замен\nДлина строки={len(text)}")

def get_cost(dict, product_name):
    if product_name in dict:
        print(dict[product_name])
    else:
        print("Не найдено")

def add_product(dict, product_name, cost):
    dict[product_name] = cost
    print(f"Товар {product_name} добавлен со стоимостью {cost} руб.")

def del_product(dict, product_name):
    if product_name in dict:
        del dict[product_name]
        print(f"Товар {product_name} удалён")
    else: print("Нет такого товара.")

def product_count(dict):
    print(f"Всего {len(dict)} товаров")

def product_menu(dict):
     for k in dict.items():
        print(k)

def product_minmax(dict):
    print(f"Минимальная стоимость={min(dict, key=dict.get)} у товара {dict[min(dict, key=dict.get)]}\nМаксимальная стоимость={max(dict, key=dict.get)} у товара {dict[max(dict, key=dict.get)]}")

def find_product(dict, price):
    for k, v in dict.items():
        if v>price:
            print(k)

def mid_price(dict):
    print(f"Средняя цена товара={sum(dict.values())/len(dict)} руб.")

def arrs_work_1(arr_a):
    arr_a.append(int(input("Введите число, добавляемое в конец массива а: ")))
    print(arr_a)

def arrs_work_2(arr_a):
    arr_a.insert(2, int(input("Введите число, добавляемое между 2 и 3 местом массива а: ")))
    print(arr_a)

def arrs_work_3(arr_b):
    arr_b.pop()
    arr_b.sort()
    print(arr_b)

def arrs_work_4(arr_b):
    arr_b_temp = arr_b.copy()
    print(f"{arr_b}\n{arr_b_temp}")

def arrs_work_5(arr_a):
    print(f"Максимальный элемент массива а={max(arr_a)}\nСумма элементов массива а={sum(arr_a)}")

def arrs_work_6(arr_a, arr_b):
    arr_c = arr_a[0:3] + arr_b[1:4]
    print(f"Массив с: {arr_c}")

def list_1(num):
    count = 0
    arr = [int(input("Введите элемент: ")) for i in range(num)]
    print(arr)
    for i in range(num):
        if arr[i] % 2 == 1:
            arr[i]=0
            count += 1
    print(arr)
    print(count)

def matrix(l, w):
    m = [[int(input("Введите элемент матрицы: ")) for j in range(w)] for i in range(l)]
    print("Исходная матрица:")
    for row in m:
        print(row)
    for i in range(l):
        row = m[i]
        max_idx = row.index(max(row))
        min_idx = row.index(min(row))
        row[max_idx], row[min_idx] = row[min_idx], row[max_idx]
    print("Измененная матрица:")
    for row in m:
        print(row)

def file_work(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as f_in, \
                open(output_filename, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                pwd = line.strip()
                if not pwd: continue
                errors = []
                if len(pwd) < 8: errors.append("Длина пароля меньше 8 символов")
                if not any(char.isupper() for char in pwd): errors.append("Отсутствуют заглавные буквы")
                if not any(char.islower() for char in pwd): errors.append("Отсутствуют строчные буквы")
                if not any(char.isdigit() for char in pwd): errors.append("Отсутствуют цифры")
                if not errors: result = f"Пароль '{pwd}': надёжный\n"
                else: result = f"Пароль '{pwd}': ненадёжный\nПричины:\n"
                for error in errors:
                    result += f"- {error}\n"
                f_out.write(result)
        print(f"Результаты сохранены в {output_filename}")

    except FileNotFoundError:
        print(f"Файл {input_filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
