from asyncio.constants import ACCEPT_RETRY_DELAY
from multiprocessing.dummy import Array


king = 'King Balon the 6th'
RoomsDynastyKing=17
DynastyKing=6
print(king + ' has ' + str(6 * 17) + ' rooms.')

potomstvo = 6 * 17
print(king + ' has ' + str(potomstvo) + " rooms.")

first_name = 'Joffrey'
greeting = 'Hello'
print(greeting + ", " + first_name + "!")

first_name = 'Joffrey'
greeting = 'Hello'
print(f'{greeting}, {first_name}!')

school = 'Hexlet'
whatIsIt = f'{school} - online courses'
print(whatIsIt) 

"""a='Do you want to eat,'
b="Yes, I'm hungry, mom."
stark = 'Arya'
print(f'''{a} {stark}? 
{b}''')"""

stark = 'Arya'
print(f'''{Do you want to eat,} {stark}? {Yes, Im hungry, mom.}''')

"""Выведите на экран две строки:
 Do you want to eat, <name>? и 
 Yes, I'm hungry, mom.. 
 Где вместо <name> должна использоваться
 переменная stark. 
 Вывод должен получиться таким:

Do you want to eat, Arya?
Yes, I'm hungry, mom."""