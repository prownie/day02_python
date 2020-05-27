def ft_map(function_to_apply, list_of_inputs):
    new = []
    if isinstance(list_of_inputs, dict):
        for keys in list_of_inputs.key():
            new.append(function_to_apply(keys))
    else:
        try:
            for i in list_of_inputs:
                new.append(function_to_apply(i))
        except NotImplementedError:
            print("Wrong attribute")
        except TypeError:
            print("Cant iterate")
    return(new)


# function to put in uppercase
def ft_toupper(letter):
    return(letter.upper())


# function pow
def ft_pow(number):
    return(number * number)


# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

print("first test")
print("mine :", ft_map(ft_toupper, alphabets))
test = map(ft_toupper, alphabets)
print("true :", end='')
for i in test:
    print("{} ".format(i), end='')

numbers = [2, 3, 4, 5, 6]

print("second test")
print("mine :", ft_map(ft_pow, numbers))
test = map(ft_pow, numbers)
print("true :", end='')
for i in test:
    print("{} ".format(i), end='')
