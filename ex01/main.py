def what_are_the_vars(*param, **params):
    ret = ObjectC()
    if len(param) == 0 and len(params) == 0:
        setattr(ret, "_", 0)
    else:
        for key, value in params.items():
            setattr(ret, key, value)
        j = 0
        for i in param:
            if "var_{}".format(j) in dir(ret):
                return(None)
            setattr(ret, "var_{}".format(j), i)
            j += 1
    return(ret)


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end\n")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
