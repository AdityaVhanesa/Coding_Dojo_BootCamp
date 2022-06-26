x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]["last_name"] = "Bryant"

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"

z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30

"============================================================"

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(dict_list):
    for dictionary in dict_list:
        printString = ""
        for key, val in dictionary.items():
            printString += "{} - {}, ".format(key, val)
        print(printString[0: -2])  # --> Remove Comma from the last key pair.


iterateDictionary(students)


def iterateDictionary2(key_name, dict_list):
    for dictionary in dict_list:
        print(dictionary.get(key_name))


iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key, val in some_dict.items():
        print("\n"*2)
        print("{} {}".format(len(val), key.upper()))
        for value in val:
            print(value)


printInfo(dojo)

