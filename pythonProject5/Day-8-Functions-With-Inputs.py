# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
#name = input("What is your name? ")
# def greet(name):
#     print(f"Hello {name}")
#     print(f"How do you do today {name}")
#     print("Isn't the weather nice today?")
# greet("Angela")

#Functions with more than 1 input With Positional Arguements

# def greet_with(name,location):
#     print(f"Hello {name}.")
#     print(f"How do you do today {name}.")
#     print(f"You are from {location}.")
# greet_with("Alex Klotz", "Germany")

#Functions with more than 1 input with Keyword Arguements

def greet_with(name,location):
    print(f"Hello {name}.")
    print(f"How do you do today {name}.")
    print(f"You are from {location}.")
greet_with(location = "Germany", name = "John Doe")