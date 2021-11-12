def grades(*num, sit=False):
    """
    => function to analise grades and situation of several students.
    :param num: one or more grades of students
    :param sit: optional, show o not the situation
    :return: return a dictionary with information form several students
    """
    dic = {}
    dic['total'] = len(num)
    dic['higher'] = max(num)
    dic['lower'] = min(num)
    average = sum(num) / len(num)
    dic['average'] = average
    if sit:
        if average < 5:
            dic['situation'] = 'BAD'
        elif 5 < average < 7:
            dic['situation'] = 'GOOD'
        elif average >= 7:
            dic['situation'] = 'GREAT'
    return dic


r = grades(4.9, 5, 8, 10, sit=True)
print(r)
