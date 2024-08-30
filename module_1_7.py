grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_=list(sorted(students)) # переводим наш словарь по именам в список
sred_bal= [] # создаем новый список для внесения средних балов
# находим средний бал для нашего списка grades, и записываем их в новый список sred_bal
for x in grades:
  if type(x) is list:
      a=sum(list(x))/len(x)
      sred_bal.append(a)

students_sred_bal = {} # создаем новый словарь для записи полученных данных
for i in range(0, len(sred_bal)):
     students_sred_bal[students_[i]] = sred_bal[i]
print (f"Словарь по среднему балу студентов:{students_sred_bal}")







