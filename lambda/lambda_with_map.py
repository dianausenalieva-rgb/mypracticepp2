#1 map — удваивает элементы
doubled = list(map(lambda x: x * 2, numbers)
)
print(doubled)

#2 map — увеличивает на 1
plus_one = list(map(lambda x: x + 1, numbers))
print(plus_one)

#3 map — делает строки из чисел
as_strings = list(map(lambda x: str(x), numbers))
print(as_strings)

#4 map — квадраты
squares = list(map(lambda x: x * x, numbers))
print(squares)

#5 
neg = list(map(lambda x: -x, numbers))
print(neg)