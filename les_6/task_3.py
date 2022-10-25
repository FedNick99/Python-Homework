# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы

def list_of_personal (persons:list) -> dict:
    keys = [persons[i][0] for i in range(len(persons))]
    dict_of_personal = {}.fromkeys(keys, [])
    for k in keys:
        new_list = []
        for j in persons:
            if j[0] == k:
                new_list.append(j)
        dict_of_personal[k]=new_list
    return dict_of_personal
persons = input("Enter names of personal (Use spacebar) ").split(' ')
print(list_of_personal(persons))