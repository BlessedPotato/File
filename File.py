# Задание 1

recipes = []

with open (r'C:\Users\maxik\Desktop\ДЗ №7\recipes.txt', 'rt+', encoding = 'UTF-8') as file:
    for dish in file:
        dish_name = dish.strip()
        cook_book = {dish_name: []}
        ingr_count = file.readline()

        print('\n')

        for item in range(int(ingr_count)):
            measure_mod = file.readline()
            ingredient_name, count, measure = measure_mod.strip().split(' | ')
            cook_book[dish_name].append({'ingredient_name': ingredient_name, 'count': count, 'measure': measure})

        white_line = file.readline()
        recipes.append(cook_book)
        print(cook_book)

# Задание 2

print("\n")

def get_shop_list_by_dishes(dishes, person_count):

    for dish in dishes:
        shop_list = {}

        if dish in cook_book and dish in dishes:
            dict_list = {}
            for i in cook_book[dish][1:]:
                if i['ingredient_name'] in dict_list:
                    dict_list = {i['ingredient_name']: {'measure': i['measure'], 'count': i['count']}}

                else:
                    person = int(i['count']) * person_count
                    dict_list = {i['ingredient_name']:{'measure':i['measure'], 'count': person}}
                    shop_list.update(dict_list)

        return shop_list

    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


# Задание 3

print('\n')

outputfile = 'output.txt'

file_1 = r"C:\Users\maxik\Desktop\File\1.txt"
file_2 = r"C:\Users\maxik\Desktop\File\2.txt"
file_3 = r"C:\Users\maxik\Desktop\File\3.txt"

myfile = open(outputfile, 'w', encoding = 'UTF-8')

def num_of_lines(*files):
    count = {}

    for file in files:
        with open(file, 'r', encoding = 'UTF-8') as f:
            count.update({file[-5:]: (len(f.readlines()))})
    files2 = {}

    for i in sorted(count, key=count.get, reverse=True):
        files2[i] = count[i]
    print(files2)

    for key, value in files2.items():
        myfile.write(f'Даны следующие файлы: {key} \n')
        myfile.write(f'Количество строк: {value}, номер файла: {key}\n')

    return

num_of_lines(file_1, file_2, file_3)





