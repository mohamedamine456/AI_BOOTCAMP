def ft_reduce(function_to_apply, list_of_inputs):
    new_list = iter(list_of_inputs)
    value = next(new_list)
    for element in new_list:
        value = function_to_apply(element)
    return (value)
