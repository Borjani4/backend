dollars_count = 50 * 1.25
print(dollars_count)  # => 62.5

"""Запишем стоимость доллара в рублях, 
как отдельную переменную. 
Вычислим цену 50 евро в долларах, умножив их на 1.25. 
Допустим, что 1 доллар — 60 рублей:"""

rubles_per_dollar = 60
dollars_count = 50 * 1.25  # 62.5
rubles_count = dollars_count * rubles_per_dollar  # 3750.0
print(rubles_count)

"""А теперь давайте добавим к выводу текст с помощью конкатенации:"""
rubles_per_dollar = 60
dollars_count = 50 * 1.25  # 62.5
rubles_count = dollars_count * rubles_per_dollar  # 3750.0

print('The price is ' + str(rubles_count) + ' rubles')
# => The price is 3750.0 rubles



"""what='Kings'+ 'road'
print(what)

first="Kings"
what=first+'road'
print(what)

first="kings"
last='road'
what=first+last
print(what)"""

rubles_per_dollar = 60
euros_count = 100*1.25
rubles_count=euros_count*rubles_per_dollar
print(euros_count)
print(rubles_count)
