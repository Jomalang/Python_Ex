# ch02-01
# OOP -> 코드 재사용, 코드 중복 방지

car_company_list = ["현대", "기아", "삼성", "벤츠"]
del car_company_list[2]
print(car_company_list)

# 딕셔너리
car_dicts = [
    {'car_company' : '현대', 'car_detail' : {'color' : 'white', 'horsepower' : 400}},
    {'car_company' : '기아', 'car_detail' : {'color' : 'black', 'horsepower' : 300}},
    {'car_company' : '벤츠', 'car_detail' : {'color' : 'silver', 'horsepower' : 500}}
]
# print(car_dicts[0].get('car_detail').get('horsepower'))
# print(car_dicts[0].get('car_detail').get('color'))
# print(car_dicts[0].get('car_company'))

#클래스 구조
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # def __str__(self):
    #     return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('Ferrai', {'color' : 'white', 'horsepower' : 400})
print(car1.__dict__.get('_details').get('color'))

print(dir(car1))