#1
x = [ [5,2,3], [10,8,9] ] 
# Change val 10 in x to 15. Output should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

z = [ {'x': 10, 'y': 20} ]
# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}


# Change last_name of first student from 'Jordan' to 'Bryant'
sports_directory['basketball'][1] = 'Bryant'
print(sports_directory)


# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)



#2 Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list 
# prints each key and the associated value. 

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterate_dictionary(dict):
    for i in range(0, len(dict)):
        bucket = ""
        for key, val in dict[i].items():
            bucket += f"{key} - {val} \n"
        print(bucket)
iterate_dictionary(students)
    

#3 Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. For example, 
# iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
def iterate_dictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        bucket = ""
        for key, val in dict[i].items:
            bucket += f"{val} \n"
        print(bucket)
iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)



4#Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):

print(f"{key[0]} {size}LOCATIONS {val}, {key[1]} {size}INSTRUCTORS {val})

# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
