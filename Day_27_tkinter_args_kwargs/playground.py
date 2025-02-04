def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 4))


def calculate(n, **kwargs):
    n += kwargs.get('add', 1)
    n *= kwargs['multiply']
    print(n)


calculate(2, multiply=5)
