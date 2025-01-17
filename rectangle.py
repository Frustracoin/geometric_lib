def area(a, b):
    '''
    Принимает числа a и b, где
	a - длина стороны прямоугольника.
	b - длина стороны прямоугольника не совпадающей со стороной a и не лежащей напротив неё.
	Возвращает площадь равную произведению этих сторон
	Examples:
	1.  input : 3 2
        output : 6
    2.  input : 4 3
        output : 12
    3.  input : 5 4
        output : 20
    4.  input : 6 5
        output : 30
    '''

    return a * b

def perimeter(a, b):
    '''
    Принимает числа a и b, где
	a - длина стороны прямоугольника.
	b - длина стороны прямоугольника не совпадающей со стороной a и не лежащей напротив неё.
	Возвращает периметр прямоугольника равный удвоенной сумме сторон
	Examples:
	1.  input : 3 2
        output : 10
    2.  input : 4 3
        output : 14
    3.  input : 5 4
        output : 18
    4.  input : 6 5
        output : 22
    '''

    return (a + b) * 2

