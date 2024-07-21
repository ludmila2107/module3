
def send_email(message, recipient, sender = "university.help@gmail.com"):
    variants = ('.com', '.ru', '.net')
    if ("@" not in recipient) or not recipient.endswith(variants):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")




# send_email('s', 'uiversity.help@gmail.com')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')