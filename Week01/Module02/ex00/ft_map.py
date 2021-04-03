def ft_map(function_to_apply, list_of_inputs):
    for i in range(len(list_of_inputs)):
        list_of_inputs[i] = function_to_apply(list_of_inputs[i])
    return (list_of_inputs)


l = ['sat', 'bat', 'cat', 'mat']
ll = ft_map(tuple, l)
print(ll)
