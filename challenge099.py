def higher(* numbers):
    from time import sleep
    print('-=' * 25)
    if len(numbers) > 0:

        sleep(0.8)
        for n in numbers:
            print(f'{n}', end=' ')
            sleep(0.7)
        print('Analysing the numbers entered...')
        sleep(1)
        print(f'was entered! {len(numbers)} number in total.')
        sleep(1)
        print(f'The higher number enter is {max(numbers)}')
    else:
        print('Analysing the numbers entered...')
        sleep(1)
        print('Was entered 0 numbers in total.')
        sleep(1)
        print('The higher number entered is 0')
    sleep(0.8)


higher(2, 9, 4, 5, 7, 1)
higher(4, 7, 0)
higher()
