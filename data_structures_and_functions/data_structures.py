from generators_decorators_context_manager.decorators import timer
# _________________________Data Structures__________________________#
# Data Structures:
#       myList = [val, val, val, val] | myList items are ordered, changeable, and allow duplicate values and can be accessed by index.
#       myTuple = (val, val, val, val) | A myTuple is a collection which is ordered and unchangeable.
#       mySet = {val, val, val, val} | A mySet is a collection which is both unordered and unindexed and cannot have duplicate
#       myDictionary = {
#                       "key": "value",
#                       "key": "value",
#                       "key": "value"
#       }

myList = [1, True, "name", ["name1", "name2"]]
myTuple = (1, 2, 3, 4)
mySet = {1, 2, 3, 4, "banana"}
myDictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

def resetDataStructures():
    myList = [1, True, "name", ["name1", "name2"]]
    myTuple = (1, 2, 3, 4)
    mySet = {1, 2, 3, 4, "banana"}
    myDictionary = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

def Example_1_myList():

    print("\033[1m" + "Original Data Structures" + "\033[0m")
    print(f" myList: {myList}", "\n", f"myTuple: {myTuple}", "\n", f"mySet: {mySet}", "\n", f"Dictionarie: {myDictionary}", "\n")

    
    # Access Items
    print("\033[1m" + "Access Items" + "\033[0m")
    print(f" Accessing data from myList: {myList[0]}")
    print(f" Accessing data from myTuple: {myTuple[0]}")
    print(" Accessing data from mySet: ", {x for x in mySet})
    print(f" Accessing data from Dictinarie: {myDictionary.get('model')} \n")

    # Change item
    print("\033[1m" + "Change Item" + "\033[0m")
    myList[0] = "Changed Item"
    myList[1:2] = ["Second Changed item", "New Item"] #Tilføj Note

    # myTuples are unchangeable, or immutable

    # mySets unordered, unchangeable, and do not allow duplicate values

    myDictionary.update({"year": "2021"})
    print(f" myList: {myList}", "\n", f"Dictionary: {myDictionary}", "\n")
    resetDataStructures()

    # Add item
    print("\033[1m" + "Add" + "\033[0m")
    myList.append("appended item")
    myList.insert(2, "inserted Item")
    myList.extend(["Extended", "myList"])


    # myTuples cannot be change because immutable

    mySet.add("Added item")
    tempMySet = {"temp1", "temp2"}
    mySet.update(tempMySet)  # To add items from another mySet into the current mySet

    myDictionary["color"] = "Added Color"
    myDictionary.update({"updateColor": "Updated Color"})
    print(f" myList: {myList}", "\n", f"mySet: {mySet}", "\n", f"myDictionary: {myDictionary}", "\n")
    resetDataStructures()

    # Loop Through
    print("\033[1m" + "Loop Through" + "\033[0m")

    # myList
    for i in myList:
        print(i)

    for i in range(len(myList)):
        print(myList[i])

    # myTuple
    for x in myTuple:
        print(x)

    for i in range(len(myTuple)):
        print(myTuple[i])

    # Set

    # Dictionary

    # Print all key names in the dictionary, one by one:
    for x in myDictionary:
        print(x)

    # Print all values in the dictionary, one by one:
    for x in myDictionary:
        print(myDictionary[x])

    # You can also use the values() method to return values of a dictionary:
    for x in myDictionary.values():
        print(x)

    # You can use the keys() method to return the keys of a dictionary:
    for x in myDictionary.keys():
        print(x)

    # Loop through both keys and values, by using the items() method:
    print("\u001b[31m"
          "Using mydictionary.items():"
          "\u001b[0m")
    for x, y in myDictionary.items():
        print("Key and value", x, y)



# _____________________myList comprehensions__________________________#
# myList Comprehensions:
#       [ expression for val in collection ]
#       [ expression for val in collection if <statement> ]
#       [ expression for val in collection if <statement_1> and <statement_2> ]
#       [ expression for value1 in collection_1 and value2 in val in collection_2 ]


# Example_1 | Showing [ expression for val in collection ] | This example shows how you myList comprehensions work vs a normal forloop

def Example_1_myList_Comprehension():
    myList1 = []

    for i in range(1, 101):
        myList1.append(i)
    print(myList1)

    # ---------------------------------------------------------------------------------------------------------

    # OR print([i for i in range(1, 101)])
    myList2 = [i for i in range(1, 101)]
    print(myList2)


# Example_2 | Showing [ expression for val in collection if <statement> ] | How to sort movies using comprehension with if statement
def Example_2_myList_Comprehension():
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


# Each element in the forloop is a myTuple, then we check if the year is under 2000 and print only the title
def Example_3_myList_Comprehension():
    movies1 = [("Avatar", 1942), ("Babe watch", 1999), ("Ghostbusters", 2122), ("Amandas Vacation", 208),
               ("Gattaca", 1818), ("Star wars", 1922), ("Gandhi", 2011)]

    foundMoviesByYear = [title for (title, year) in movies1 if year < 2000]
    # foundMoviesByYear = [(title, year) for (title, year) in movies1 if year < 2000]

    print(foundMoviesByYear)


def Example_4_myList_Comprehension():
    myList1 = [2, -5, 8]
    print(f"myList * 4 {myList1 * 4}")


    myList2 = [4 * x for x in myList1]
    print(f"myList2 with comprehension {myList2}")

Example_4_myList_Comprehension()