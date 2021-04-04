def ft_filter(function_to_apply, list_of_inputs):
    new_list = []
    for item in list_of_inputs:
        if function_to_apply(item) == True:
            new_list.append(item)
    return (new_list)


def lenns(element):
    if len(element) > 10:
        return True
    else:
        return False

l = ['fjdslffdsfjkd', 'fds', 'fdfdsfksjahfkjd', 'fddsffdsf', 'ffadsfdsfdsfd']

ll = ft_filter(lenns, l)
print(ll)
