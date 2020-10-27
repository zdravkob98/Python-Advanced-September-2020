import errors

line = input()

while line != 'End':
    domains = '.com, .bg, .org, .net'
    name = line.split('@')[0]

    if len(name) <= 4:
        raise errors.NameTooShortError('NameTooShortError - "Name must be more than 4 characters')

    if '@' not in line:
        raise errors.MustContainAtSymbolError('MustContainAtSymbolError - "Email must contain @')

    domain = line.split('.')[1]
    if domain not in domains:
        raise errors.InvalidDomainError('InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net')



    print('Email is valid')
    line = input()