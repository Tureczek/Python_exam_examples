# _________________________Data Structures__________________________#
# Data Structures:
#       List = [val, val, val, val]
#       Tuple = (val, val, val, val)
#       Set = {val, val, val, val} | A set is a collection which is both unordered and unindexed
#       Dictionaries = {
#                       "key": "value",
#                       "key": "value",
#                       "key": "value"
#       }


def Example_1_List():
    List = [1, True, "name", ["name1", "name2"]]
    Tuple = (1, 2, 3, 4)
    Set = {1, 2, 3, 4, "banana"}
    Dictionaries = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print("\033[1m" + "Original Data Structures" + "\033[0m")
    print(f" List: {List}", "\n", f"Tuple: {Tuple}", "\n", f"Set: {Set}", "\n", f"Dictionarie: {Dictionaries}", "\n")


    # Access Items
    print("\033[1m" + "Access Items" + "\033[0m")
    print(f" Accessing data from List: {List[0]}")
    print(f" Accessing data from Tuple: {Tuple[0]}")
    print(f" Accessing data from Set:", {x for x in Set})
    print(f" Accessing data from Dictinarie: {Dictionaries.get('model')}")

    # Change item
    print("\033[1m" + "Change Item" + "\033[0m")
    List[0] = "Changed Item"
    List[1:2] = ["Changed item", "New Item"]

    # Tuples are unchangeable, or immutable

    # Sets unordered, unchangeable, and do not allow duplicate values

    Dictionaries.update({"year": "2021"})
    print(f" List: {List}", "\n", f"Dictionarie: {Dictionaries}", "\n")


    # Add item
    print("\033[1m" + "Add" + "\033[0m")
    List.append("appended item")
    List.insert(2, "inserted Item")
    List.extend(["E", "x", "t", "e", "n", "d"])

    # Tuples cannot be change because

    Set.add("Added item")
    tempSet = {"temp1", "temp2"}
    Set.update(tempSet)  # To add items from another set into the current set

    Dictionaries["color"] = "Added Color"
    Dictionaries.update({"updateColor": "Updated Color"})
    print(f" List: {List}", "\n", f"Set: {Set}", "\n", f"Dictionarie: {Dictionaries}", "\n")


    # Loop Through
    print("\033[1m" + "Loop Through" + "\033[0m")

    # List
    for x in List:
        print(x)

    for i in range(len(List)):
        print(List[i])

    # Tuple
    for x in Tuple:
        print(x)

    for i in range(len(Tuple)):
        print(Tuple[i])

    # Dictionary

    # Print all key names in the dictionary, one by one:
    for x in Dictionaries:
        print(x)

    # Print all values in the dictionary, one by one:
    for x in Dictionaries:
        print(Dictionaries[x])

    # You can also use the values() method to return values of a dictionary:
    for x in Dictionaries.values():
        print(x)

    # You can use the keys() method to return the keys of a dictionary:
    for x in Dictionaries.keys():
        print(x)

    # Loop through both keys and values, by using the items() method:
    for x, y in Dictionaries.items():
        print(x, y)

Example_1_List()




# _____________________List comprehensions__________________________#
# List Comprehensions:
#       [ expression for val in collection ]
#       [ expression for val in collection if <statement> ]
#       [ expression for val in collection if <statement_1> and <statement_2> ]
#       [ expression for value1 in collection_1 and value2 in val in collection_2 ]


# Example_1 | Showing [ expression for val in collection ] | This example shows how you list comprehensions work vs normal
def Example_1_List_Comprehension():
    list1 = []

    for i in range(1, 101):
        list1.append(i)
    print(list1)

    # ---------------------------------------------------------------------------------------------------------

    # OR print([i for i in range(1, 101)])
    list2 = [i for i in range(1, 101)]
    print(list2)


# Example_2 | Showing [ expression for val in collection if <statement> ] | How to sort movies using comprehension with if statement
def Example_2_List_Comprehension():
    movies1 = ["Avatar", "Babe watch", "Ghostbusters", "Amandas Vacation", "Gattaca", "Star wars", "Gandhi"]
    foundMovies1 = []

    for title in movies1:
        if title.startswith("G"):
            foundMovies1.append(title)
    print(foundMovies1)

    # ---------------------------------------------------------------------------------------------------------

    movies2 = ["Avatar", "Babe watch", "Ghostbusters", "Amandas Vacation", "Gattaca", "Star wars", "Gandhi"]
    foundMovies = [title for title in movies2 if title.startswith("A")]

    print(foundMovies)


# Each element in the forloop is a tuple, then we check if the year is under 2000 and print only the title
def Example_3_List_Comprehension():
    movies1 = [("Avatar", 1942), ("Babe watch", 1999), ("Ghostbusters", 2122), ("Amandas Vacation", 208),
               ("Gattaca", 1818), ("Star wars", 1922), ("Gandhi", 2011)]

    foundMoviesByYear = [title for (title, year) in movies1 if year < 2000]
    # foundMoviesByYear = [(title, year) for (title, year) in movies1 if year < 2000]

    print(foundMoviesByYear)


def Example_4_List_Comprehension():
    list1 = [2, -5, 8]
    print(f"List * 4 {list1 * 4}")

    list2 = [4 * x for x in list1]
    print(f"List2 with comprehension {list2}")
