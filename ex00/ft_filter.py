def ft_filter(function_to_apply, list_of_inputs):
    new = []
    if isinstance(list_of_inputs, dict):
        for i in list_of_inputs.keyes():
            if function_to_apply(i):
                new.append(i)
    else:
        try:
            for i in list_of_inputs:
                if function_to_apply(i):
                    new.append(i)
        except ValueError:
            print("Wrong value")
        except TypeError:
            print("Wrong type")
        except NameError:
            print("Wrong name")
        except AttributeError:
            print("Wrong attribute")
    return(new)


# get some vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    else:
        return False


alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
filteredVowels = ft_filter(filterVowels, alphabets)
print('The filtered vowels are:i')
print("mine :", filteredVowels)
test = filter(filterVowels, alphabets)
print("true :", end='')
for i in test:
    print("{} ".format(i), end='')
