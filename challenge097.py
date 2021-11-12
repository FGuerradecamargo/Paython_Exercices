def msg(test):
    print('-' * (len(test) + 4))
    print(f'  {test}')
    print('-' * (len(test) + 4))


title = str(input('Enter the title: ')).strip()
msg(title)
