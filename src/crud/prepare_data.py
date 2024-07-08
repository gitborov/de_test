class PrepareForQuery:
    '''Обрабатывает вложенный словарь типа
	{'users':
		{'gender': 'male',
		'name': 'John',
		'age': 30
		}}
	 ключ - название таблицы а знвачение - словарь с данными для вставки'''

    def __init__(self, value: dict):
        #добавил атрибут name, чтобы получить название таблицы
        #и затем в методах использовать его, чтобы получать данные из вложенного словаря
        self.value = value
        self.name = str(tuple(self.value.keys())[0])

    def get_columns(self):
        #получаем названия столбцов
        columns = str(tuple(self.value[self.name].keys())).replace("'", "")
        return columns

    def get_s_string(self):
        #получаем строку типа %s,%s,%s, где длина строки = количеству столбцов
        s_string = ('%s,' * len(self.value[self.name]))[:-1]
        return s_string

    def get_values(self):
        #получаем значения для вставки
        values = tuple(self.value[self.name].values())
        return values
