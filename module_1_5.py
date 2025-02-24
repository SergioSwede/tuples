immutable_var = (True, 1, 'string')                                         #Зададим Кортеж
print('Кортеж стостоит из следующих элементов: ', immutable_var)            #Вывод данного кортежа
#immutable_var[0] = False                                                   #Элементы кортежа не являющиеся списком, не могут быть изменены
immutable_var = immutable_var + ([1, 2], False)                             #добавим в котреж 2 элемента с помощью конкатенации, один из которых - список
print('Кортеж стостоит из следующих элементов: ', immutable_var)            #Вывод на экран получившегося
immutable_var[3][1] = True                                                  #Изменим элемент списка в кортеже
print('Кортеж стостоит из следующих элементов: ', immutable_var)            #Вывод на экран получившегося

mutable_list = [True, 1, 'string']                                          #Зададим список
print('Список стостоит из следующих элементов: ', mutable_list)             #Вывод данного списка на экран
mutable_list[0] = False                                                     #Изменим первый элемент в списке
print('Список стостоит из следующих элементов: ', mutable_list)             #Вывод измененного списка на экран
mutable_list.append('123')                                                  #Используя функции изменим список
mutable_list.extend('123')
mutable_list.remove(False)
print('Список стостоит из следующих элементов: ', mutable_list)             #Вывод измененного списка на экран