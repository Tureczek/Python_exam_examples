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


def printOriginalDataStructures():
    print("\033[1m" + "Original Data Structures" + "\033[0m")
    myOriginalList = [1, True, "name", ["name1", "name2"]]
    myOriginalTuple = (1, 2, 3, 4)
    myOriginalSet = {1, 2, 3, 4, "banana"}
    myOriginalDictionary = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print("\33[31m", f"myList: {myOriginalList}", "\33[32m", "\n", f"myTuple: {myOriginalTuple}", "\33[35m", "\n", f"mySet: {myOriginalSet}", "\33[34m" "\n",
          f"Dictionarie: {myOriginalDictionary}", "\n" "\033[0m")


def data_Structures_Access_Item():
    print("\033[1m" + "Access Items" + "\033[0m")
    printOriginalDataStructures()

    print(" Accessing data from " + "\33[31m" + "myList:" + "\033[0m", f"{myList[0]}")
    print(" Accessing data from " + "\33[32m" + "myTuple:" + "\033[0m", f"{myTuple[0]}")
    print(" Accessing data from " + "\33[35m" + "mySet:" + "\033[0m", {x for x in mySet})
    print(" Accessing data from " + "\33[34m" + "Dictionary:" + "\033[0m", f"{myDictionary.get('model')}" + "\n")
    print("__________________________________________________________")


def data_Structures_Change_Item():
    print("\033[1m" + "Change Item" + "\033[0m")
    printOriginalDataStructures()

    myList[0] = "Changed Item"
    myList[1:2] = ["Splitted changed item", "New Item"]  # Explanation ->
    # This method does 2 things.
    #   1. "[1:" will take item at List[1] and replace with "Splitted changed item".
    #   2. ":2]" will ass a new item at List[2] and shift right the rest of the array. | Note that List[2] item will not be replaced.

    '''
     - Tuples are unchangeable
     
     Tuples are unchangeable/immutable , meaning that you cannot change, add, or remove items once the tuple is created.
     If you want to change a tuple for some apparent reason you need to do the following:
     
     myTuple = ("dog", "cat", "sheep")
     myTempList = list(myTuple)
     myTempList[1] = "tiger"
     myTuple = tuple(myTempList)

     print(myTuple)
    '''

    '''
        - Set items are unordered, unchangeable, and do not allow duplicate values.
    '''

    # Print for dict
    myDictionary.update({"year": "2021"})
    print("\33[31m" + " myList: " + "\033[0m" + f"{myList}", "\n", "\33[34m" + "Dictionary: " + "\033[0m" + f"{myDictionary}", "\n")
    print("__________________________________________________________")


def data_Structures_Add():
    print("\033[1m" + "Add" + "\033[0m")
    printOriginalDataStructures()

    myList.append("appended item")
    myList.insert(2, "inserted Item")
    myList.extend(["Extended", "myList"])

    '''
        - Tuples are unchangeable/immutable
    '''
    mySet.add("Added item")
    tempMySet = {"temp1", "temp2"}
    mySet.update(tempMySet)  # To add items from another mySet into the current mySet

    myDictionary["color"] = "Added Color"
    myDictionary.update({"updateColor": "Updated Color"})  # You can use update to add eventhough its not its intended use

    print("\33[31m", f"myList: \033[0m {myList}", "\33[35m", "\n", f"mySet: \033[0m {mySet}", "\33[34m" "\n", f"Dictionarie: \033[0m {myDictionary}", "\n" "\033[0m")
    print("__________________________________________________________")




def data_Structures_Loop_Through():

    print("\033[1m" + "Loop Through" + "\033[0m")
    printOriginalDataStructures()

    print("\033[1m" + "\nLoop Through List" + "\033[0m")

    for i in myList:
        print("Data from \33[31m List: \033[0m", i)

    print("-")

    for i in range(len(myList)):
        print("Data from \33[31m List: \033[0m using index:", myList[i])

    # ----------------------------------------------------

    print("\033[1m" + "\nLoop Through Tuple" + "\033[0m")

    for i in myTuple:
        print("Data from \33[32m Tuple: \033[0m", i)

    print("-")

    for i in range(len(myTuple)):
        print("Data from \33[32m Tuple: \033[0m using index:", myTuple[i])

    # ----------------------------------------------------

    print("\033[1m" + "\nLoop Through Set" + "\033[0m")
    for i in mySet:
        print("Data from \33[35m Set: \033[0m:", i)

    # ----------------------------------------------------

    print("\033[1m" + "\nLoop Through Dictionary" + "\033[0m")

    # Print all key names in the dictionary, one by one:
    for i in myDictionary:
        print("Data from\33[34m Dictionary: \033[0m:", i)

    print("-")

    # Print all values in the dictionary, one by one:
    for i in myDictionary:
        print("Data from\33[34m Dictionary: \033[0m: using index:", myDictionary[i])

    print("-")

    # You can also use the values() method to return values of a dictionary:
    for x in myDictionary.values():
        print("Data from\33[34m Dictionary: \033[0m: using .values: ", (x))

    print("-")

    # You can use the keys() method to return the keys of a dictionary:
    for i in myDictionary.keys():
        print("Data from\33[34m Dictionary: \033[0m: using .keys():", i)

    print("-")

    # Loop through both keys and values, by using the items() method:
    for i, j in myDictionary.items():
        print("Key and Value from\33[34m Dictionary: \033[0m:", i, j)
    print("__________________________________________________________")


data_Structures_Access_Item()
data_Structures_Add()
data_Structures_Change_Item()
data_Structures_Loop_Through()

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

