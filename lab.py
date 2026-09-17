def pwd_check(pwd):
    errors = []
    if len(pwd) < 8: errors.append("Длина пароля меньше 8 символов")
    if not any(char.isupper() for char in pwd): errors.append("Отсутствуют заглавные буквы")
    if not any(char.islower() for char in pwd): errors.append("Отсутствуют строчные буквы")
    if not any(char.isdigit() for char in pwd): errors.append("Отсутствуют цифры")

    if not errors:
        print("Пароль надёжный")
    else:
        print("Пароль ненадёжный")
        for error in errors:
            print(error)

def calc(a, b, op):
    match op:
        case "+":   print(f"Значение выражения a+b вычислено при a={a}, b={b}\nРезультат равен {a+b}")
        case "-":   print(f"Значение выражения a-b вычислено при a={a}, b={b}\nРезультат равен {a-b}")
        case "*":   print(f"Значение выражения a*b вычислено при a={a}, b={b}\nРезультат равен {round(a*b, 1)}")
        case "/":   print(f"Значение выражения a/b вычислено при a={a}, b={b}\nРезультат равен {round(a/b, 1)}")

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
