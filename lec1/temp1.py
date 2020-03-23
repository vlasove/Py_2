def perimeter(*args):
    if len(args) == 1:
        return 2 * 3.14 * args[0]
    elif len(args) == 2:
        return 2 * (args[0] + args[1])
    else:
        return sum(args[0:])