def age_assignment (*args , **kwargs):
    return {el : kwargs[el[0]] for el in args}
    # dict = {}
    # for el in args:
    #     dict[el] = kwargs[el[0]]
    # return dict






print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
