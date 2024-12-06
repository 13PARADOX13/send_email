
def send_email(message: str, recipient: str, *, sender):
    if (symbol not in recipient or symbol not in sender)\
        or (recipient.endswith(symbol_set) == False or sender.endswith(symbol_set) == False):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

message = input('Введите текст письма: ')
recipient = input('Введите e-mail получателя: ')
sender = "university.help@gmail.com"
symbol = '@'
symbol_set = ('.com', '.ru', '.net')
send_email(message, recipient, sender = "university.help@gmail.com")
