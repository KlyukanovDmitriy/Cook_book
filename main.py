import pprint

class Ingridient:
    name = 'ingridient_name'
    quantity = 'quantity'
    measure = 'measure'

def dictionary_of_recipes(file):
    dish_title_line = 0
    ingridients_count_line = 1
    ingridient_lines_range = range(2, 3)
    cook_book = {}
    with open(file, 'r', encoding = 'utf-8') as file:
        line_list = file.readlines()
        counter = 0
        for line in line_list:
            line=line.strip()
            if line == '':
                counter = 0  # обновление счетчика строки
                continue
            elif counter == dish_title_line:
                counter += 1
                dish_title = line
                cook_book[dish_title] = []
            elif counter == ingridients_count_line:
                counter += 1
                ingridient_lines_range = range(counter, counter + int(line))
            elif counter in ingridient_lines_range:
                counter += 1
                list = [x.strip() for x in line.split('|')]
                dict_ingridient = {Ingridient.name: list[0], Ingridient.quantity: int(list[1]), Ingridient.measure: list[2]}
                cook_book[dish_title].append(dict_ingridient)
    pprint.pp(cook_book)
    return cook_book



def get_shop_list_by_dishes(dishes, person_count):
    cook_book = dictionary_of_recipes('recipes.txt')
    ingridients_to_prepare = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f'Ошибка ввода. Блюдо "{dish}" не найдено в книге рецептов, доступные блюда: {list(cook_book.keys())}')
            continue
        for ingridient in cook_book[dish]:
            ingridient_to_prepare = ingridients_to_prepare.setdefault(
                ingridient[Ingridient.name],
                {Ingridient.measure: ingridient[Ingridient.measure], Ingridient.quantity: 0})
            ingridient_to_prepare[Ingridient.quantity] += ingridient[Ingridient.quantity] * person_count
    pprint.pp(ingridients_to_prepare)


get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Борщ'], 3)


file_list = ['1.txt', '2.txt', '3.txt']
def merging_files(list):
    file_dict = {}
    for file in list:
        with open(file, 'r', encoding='utf-8') as f:
            file_dict[file] = len(f.readlines())
    file_dict_sort = sorted(file_dict.items(), key = lambda item: item[1])
    with open('result.txt', 'w', encoding = 'utf-8') as fr:
        for key, value in file_dict_sort:
            with open(key, 'r', encoding = 'utf-8') as f:
                text = f.readlines()
                fr.write(key + '\n')
                fr.write(str(value) + '\n')
                fr.writelines(text)
                fr.write('\n')
merging_files(file_list)




