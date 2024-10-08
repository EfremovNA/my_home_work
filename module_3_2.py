# Задача "Рассылка писем":

# Пункты задачи:
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.


#Создаем функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель)
# и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
def send_email (message, recipient, *, sender = 'university.help@gmail.com'):
    while 1>0:
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')): # проверка окончания строки
            if "@" not in recipient or "@" not in sender: # проверка на вхождение символа "@" в строки recipient и sender
                print (f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
                break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break
        if recipient == sender: # проверка совпадение отправителя и получателя
            print (f'Нельзя отправить письмо самому себе!')
            break
        elif sender == 'university.help@gmail.com': # проверка на совпадение отправителя с заданным
            print (f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            break
        elif sender != "university.help@gmail.com": # проверка на совпадение отправителя с заданным
            print (f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
            break

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email("Напоминаю самому себе о вебинаре", 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')




