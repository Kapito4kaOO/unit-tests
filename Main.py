
#1.Задание «Голосование»
def vote(votes):
    count = []
    for i in votes:
        count.append(votes.count(i))
    max_times = max(count)
    n = count.index(max_times)
    return votes[n]

#2.Задание «Приложение для финансового планирования»
def finance(salary, percent_mortgage, percent_life):
    a = (salary * percent_mortgage)/100
    mortgage = a*12
    savings = (percent_life*salary/100 - a)*12
    return savings

#3.Задание «Периметр прямоугольника»
def perimeter(a, b):
    perimeter = (a + b) * 2
    return perimeter

def test_function(func, expected, *args, **kwargs):
    result = func(*args, **kwargs)
    try:
        assert result == expected
        print(f'Тест функции {func} успешен')
    except AssertionError:
        print(f'Тест функции {func} не успешен. Ожидалось {expected}, получилось {result}')



test_function(vote, 1, [1,1,1,2,3]) #success
test_function(vote, 3, [1,2,3,2,2]) #failure
test_function(finance, 240_000, 100_000, 30, 50) #success
test_function(finance, 500_000, 200_000,30,45) #failure
test_function(perimeter, 18, 7,2) #success
test_function(perimeter, 24, 3,4) #failure