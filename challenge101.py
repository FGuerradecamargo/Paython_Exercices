def vote():
    from datetime import date
    birth = int(input('Enter your year of birth: '))
    age = date.today().year - birth
    if age < 16:
        return f'You are {age} years old. You do not vote yet.'
    elif 18 <= age <= 65:
        return f'You are {age} years old. You have to vote!'
    else:
        return f'You are {age} years old. Your vote is optional!'


print(vote())
