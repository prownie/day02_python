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

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function to put in uppercase
def ft_toupper(letter):
    return(letter.upper())

print("first test")
print("mine :", ft_map(ft_toupper, alphabets))
test = map(ft_toupper, alphabets)
print("true :", end='')
for i in test:
    print("{} ".format(i),end='')

# list of some numbers
numbers = [2, 3, 4, 5, 6]

# function pow
def ft_pow(number):
    return(number * number)

print("second test")
print("mine :", ft_map(ft_pow, numbers))
test = map(ft_pow, numbers)
print("true :", end='')
for i in test:
    print("{} ".format(i),end='')
