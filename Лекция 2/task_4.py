# Можно также реализовать через list comprehension
from datetime import datetime

dateFormatter = "%d.%m.%Y"

id = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
length = (65, 209, 43, 24, 58, 145, 87, 90, 52, 100)
person = (
    'И.И.Иванов', 'А.А.Петров', 'О.Е.Сидорова', 'Л.Б.Симонов', 'И.П.Никитина', 'У.А.Даль', 'А.И.Петрова',
    'О.Е.Сидорова',
    'А.М.Огнёв', 'И.П.Никитина')
call_date = (
    '15.02.2019', '23.02.2019', '10.03.2019', '09.10.2017', '15.07.2018', '06.02.2016', '02.09.2016', '25.12.2019',
    '10.08.2017', '24.11.2018')

usermart_calls = list(zip(id, length, person, call_date))

for i in range(len(usermart_calls)):
    a = usermart_calls[i]
    if datetime.strptime(a[3], dateFormatter) > datetime.strptime('14.07.2018', dateFormatter):
        print(a)
