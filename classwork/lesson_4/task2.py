#todo: Задан массив
surname = ['Электроник','Сыроежкин', 'Чижиков', 'Кукушкина']

# Код на выходе должен выдавать выпадающий список следующего вида.
"""
<select>
	<option>Электроник</option>
	<option>Сыроежкин</option>
	<option>Чижиков</option>
	<option>Кукушкина</option>
</select>
"""

select_1 = '<select>'
option_1 = '<option>'
select_2 = '</select>'
option_2 = '</option>'
print(select_1)
for i in surname:
    print('\t', option_1 + i + option_2)
print(select_2)