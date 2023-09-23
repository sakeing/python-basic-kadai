num1 = 3
num2 = 5
num3 = num1 * num2
var = 1

while var < 50:
    if 0 == var % num3:
        print('FizzBuzz')
    elif 0 == var % num1:
        print('Fizz')
    elif 0 == var % num2:
        print('Bizz')
    else:
        print(str(var))
    var += 1
