from time import sleep
c= ('\033[m',           # 0 - no color
    '\033[0;30;41m',    # 1 - white/ red
    '\033[0;30;42m',    # 2 - white/ green
    '\033[0;30;43m'     # 3 - white/ blue
    '\033[0;30;44m',    # 4 - white/ purple
    '\033[0;30;45m',    # 5 - white/ black
    '\033[7;30m'       # 6 - white/ white
    );

def title(msg, color=0):
    print(c[color], end='')
    print('=' * (len(msg) + 4))
    print(f'  {msg}')
    print('=' * (len(msg) + 4))
    print(c[0], end='')


def sys_help():
    while True:
        sleep(1)
        title('PyHelp HELP SYSTEM', 4)
        msg = ' '
        msg = str(input('\033[mFunction from the library > ')).strip().lower()
        if msg == 'end':
            break
        else:
            title(f"Accessing {msg}'s manual...", 3)
            sleep(1)
            print(c[2], end='')
            help(f'{msg}')
            print(c[0], end='')
    sleep(0.5)
    title('Program finished!', 1)


sys_help()
