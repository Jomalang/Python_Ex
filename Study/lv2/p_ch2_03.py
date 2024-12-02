class Car():
    """
    Car class
    Author : jo
    Date : 2024.12.02
    Desrciption : Class, Static, Instance Method
    """
    #클래스 변수(모든 인스턴스가 공유함.)
    price_per_raise = 1.1

    #인스턴스 메서드
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
    
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    def get_price_calc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
    def set_price(self, price):
        self._details['price'] = price

    #클래스 메서드
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased.')
    
    #스태틱 메서드
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return 'OK! This car is BMW.'
        return 'Sorry. This car is not BMW.'


# self의 의미
car1 = Car('Ferrai', {'color' : 'white', 'horsepower' : 400, 'price': 8000})
car2 = Car('BMW', {'color' : 'black', 'horsepower' : 270, 'price': 5000})   

# 게터와 세터
print(car1.get_price())
print(car1.get_price_calc())

# 클래스 메서드 사용
Car.raise_price(1.6)
print(car1.get_price_calc())