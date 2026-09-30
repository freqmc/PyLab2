from lab import *

shop_dict = {}
while True:
    try:
        print("Меню\n"
              "1) Проверка пароля\n"
              "2) Калькулятор\n"
              "3) Вывести числа, кратные 7 в диапазоне от 0 до 500\n"
              "4) Модифицированная версия п.3\n"
              "5) Текст из скобок\n"
              "6) Подсчёт точек и запятых\n"
              "7) Подсчёт слов, разделённых пробелами\n"
              "8) Замена пробелов на =\n"
              "9) Товары\n"
              "10) Работа с двумя массивами\n"
              "11) Замена нулями нечётных элементов\n"
              "12) Матрица\n"
              "13) Работа с файлами \n"
              "0) Выход\n")
        choice = int(input("Выберите: "))
        match choice:
            case 1: pwd_check(pwd=input("Введите пароль: "))
            case 2: calc(a=float(input("Введите значение а: ")), b=float(input("Введите значение b: ")), op=input("Выберите операцию (+, -, *, /): "))
            case 3: print7()
            case 4: print7_mod()
            case 5: hooks(text=input("Введите текст: "))
            case 6: comma_count(text=input("Введите текст: "))
            case 7: space_a_count(text=input("Введите текст: "))
            case 8: equal_to_space(text=input("Введите текст: "))
            case 9:
                while True:
                    print("Товары\n"
                          "1) Показать все товары\n"
                          "2) Добавить товар\n"
                          "3) Удалить товар\n"
                          "4) Найти стоимость товара\n"
                          "5) Количество товаров\n"
                          "6) Мин/Макс стоимость\n"
                          "7) Найти товары дороже указанной цены\n"
                          "8) Средняя цена\n"
                          "0) Назад в главное меню\n")
                    ch = input("Выбор: ")
                    match ch:
                        case '1': product_menu(shop_dict)
                        case '2': add_product(shop_dict, product_name=input("Название: "), cost=float(input("Цена: ")))
                        case '3': del_product(shop_dict, product_name=input("Название для удаления: "))
                        case '4': get_cost(shop_dict, product_name=input("Название для поиска: "))
                        case '5': product_count(shop_dict)
                        case '6': product_minmax(shop_dict)
                        case '7': find_product(shop_dict, price=float(input("Цена порога: ")))
                        case '8': mid_price(shop_dict)
                        case '0': break
                        case _: print("Неверный пункт меню")
            case 10:
                n1 = int(input("Размер массива a: "))
                n2 = int(input("Размер массива b: "))
                a = [int(input("Введите элемент а:")) for i in range(n1)]
                b = [int(input("Введите элемент b:")) for i in range(n2)]
                while True:
                    print("Массивы:\n"
                              "1) Добавить элемент в конец массива а\n"
                              "2) Вставить элемент в массив а между 2 и 3 местом\n"
                              "3) Удалить последний элемент из массива b и отсортировать его\n"
                              "4) Создать копию массива b\n"
                              "5) Найти максимальный элемент массива а и его сумму\n"
                              "6) Создать массив из 1 и 3 элемента массива а и из 2 и 4 массива b\n"
                              "0) Выход\n")
                    vibor=int(input("Выберите: "))
                    match vibor:
                        case 1: arrs_work_1(arr_a=a)
                        case 2: arrs_work_2(arr_a=a)
                        case 3: arrs_work_3(arr_b=b)
                        case 4: arrs_work_4(arr_b=b)
                        case 5: arrs_work_5(arr_a=a)
                        case 6: arrs_work_6(arr_a=a, arr_b=b)
                        case 0: break
                        case _: print("Неверный пункт меню")

            case 11: list_1(num=int(input("Введите размер массива: ")))
            case 12: matrix(l=int(input("Длина матрицы: ")), w=int(input("Ширина матрицы: ")))
            case 13: file_work(input_filename=input("Введите имя файла, где лежат пароли (c .txt): "), output_filename=input("Введите имя файла отчёта о паролях (с .txt): "))
            case 0:
                print("Выход из программы.")
                break
            case _: print("Неверный пункт меню")
    except:
        print("Неверный ввод данных")