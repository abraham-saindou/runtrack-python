def number():
    i = 0
    while i < 100:
        i = i + 1

        if i % 15 == 0:
            print(i, "is a FizzBuzz")
        if i % 3 == 0:
            print(i, "is a Fizz")
            continue
        if i % 5 == 0:
            print(i, "is a Buzz")
number()