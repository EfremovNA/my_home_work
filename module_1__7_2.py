grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_=list(sorted(students)) # переводим наш словарь по именам в список

sred_bal= [] # создаем новый список для внесения средних балов

# находим среднее значение нашего списка grades
a=grades.pop(0)
b=sum(a)/len(a)
sred_bal.append(b)
#
a=grades.pop(0)
b=sum(a)/len(a)
sred_bal.append(b)
#
a=grades.pop(0)
b=sum(a)/len(a)
sred_bal.append(b)
#
a=grades.pop(0)
b=sum(a)/len(a)
sred_bal.append(b)
#
a=grades.pop(0)
b=sum(a)/len(a)
sred_bal.append(b)

students_sred_bal2=dict(zip(students_, sred_bal)) # соединяем наши два списка в один словарь
print (f"Словарь по среднему балу студентов:{students_sred_bal2}")