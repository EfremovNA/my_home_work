first = int(input("Введите целое число first:"))
second = int(input("Введите целое число second:"))
third = int(input("Введите целое число third:"))

if first == second and second == third:
    print ("3")
elif first == second or second == third or first==third:
    print ("2")
else:
    print ("0")