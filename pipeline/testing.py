import re


def split_semicolon_values(valuetosplit):
    """Takes a semicolon-separated string, cleans it up and splits it"""
    splitvalues = str(valuetosplit).split(';')
    splitandcleanedvalues = []
    for item in splitvalues:
        splitandcleanedvalues.append(re.sub(r'\([^)]*\)', '', item.strip()))

    return splitandcleanedvalues


for item in split_semicolon_values('Straw Hat Pirates;Vinsmoke Family(former);Baratie(resigned)'):
    print(item.replace(" ", "_"))

# print(split_semicolon_values(
#     'Straw Hat Pirates;Vinsmoke Family(former);Baratie(resigned)'))
