immutable_var = tuple([[1,3],4,["Было два",3],True])
print("Immutable tuple:",immutable_var)
immutable_var[1] = 20 # не можем поменять значение элемента кортежа по причине того что значения записанные в кортеж не изменяемые.

# Однако если в кортеже записан список из значений, то данные значения в списке мы можем поменять.
# immutable_var[0][1]= 6
# immutable_var[2][0] = "Стало три"
# print ("Изменние в списках входящем в кортеж:",immutable_var)

mutable_list = [1,2,"Было два",True]
mutable_list[2] = "Стало три"
print("Mutable_list:",mutable_list)