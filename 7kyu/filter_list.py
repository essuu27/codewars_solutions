def filter_list(l):
    return [x for x in l if str(x).isnumeric() and not isinstance(x,str)]