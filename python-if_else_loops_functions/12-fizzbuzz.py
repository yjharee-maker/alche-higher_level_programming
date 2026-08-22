#!/usr/bin/python3
for i in range(1, 101):
    result = ""
    if (i // 3) == 0 and (i // 5) == 0:
        result = "FizzBuzz "
    elif (i // 3) == 0:
        result = "Fizz "
    elif (i // 5) == 0:
        result = "Buzz "
    else:
        result = str(i)
    print(result, end="")
