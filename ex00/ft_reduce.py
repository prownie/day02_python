import functools
import operator


def ft_reduce(function_to_apply, list_of_inputs):
    if isinstance(list_of_inputs, dict):
        keys = list(list_of_inputs.keys())
        print(keys)
        res = keys[0]
        for i in keys[1:]:
            res = function_to_apply(res, i)
    else:
        try:
            res = list_of_inputs[0]
            for i in list_of_inputs[1:]:
                res = function_to_apply(res, i)
        except ValueError:
            print("Wrong value")
        except TypeError:
            print("Wrong type")
        except NameError:
            print("Wrong name")
        except AttributeError:
            print("Wrong attribute")
    return(res)


def ft_upper(text1, text2):
    if text1 == text2:
        return(text2)
    else:
        return(text1)


test = {'sandwichd': 'pain',
        'sandwiche': 'viande',
        'sandwichd': 'salad',
        'cake': 'fromage'}

true = functools.reduce(operator.mul, [2.0, 3.0, 20])
mine = ft_reduce(operator.mul, [2.0, 3.0, 20])
print(true)
print(mine)


true = functools.reduce(ft_upper, test)
mine = ft_reduce(ft_upper, test)
print("true=", true)
print("mine=", mine)
