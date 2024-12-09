class Car():
    """
    Car class
    Author : jo
    Date : 2024.12.02
    """
    car_count = 0
    
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('color')))

# self의 의미
car1 = Car('Ferrai', {'color' : 'white', 'horsepower' : 400})
car2 = Car('BMW', {'color' : 'black', 'horsepower' : 270})
car3 = Car('Audi', {'color' : 'silver', 'horsepower' : 300})

# id 확인
print(id(car1))
print(id(car2))
print(id(car3))

# dir & __dict__ 확인
print(dir(car1))

# Doctring
print(Car.__doc__)

Car.detail_info(car1)

