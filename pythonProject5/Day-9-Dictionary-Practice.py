programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
#Adding new Items
programming_dictionary ["Loop"] = "The action of doing something over and over again."

#Re-assigning Keys in a dictionary
programming_dictionary ["Bug"] = "This is a re-assignment"

#Deleting Whole dictionarys
#programming_dictionary = {}

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


