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
    List = [1, 2, 3, 4]

def Example_1_Tuple():
    Tuple = (1, 2, 3, 4)

def Example_1_Sets():
    Set = {1, 2, 3, 4}
    print(Set)

    # Add
    Set.add("Apple")
    Set.add("Orange")
    Set.add("Squash")

    # Show by running code multiple times
    print(f"The set's order is random: {Set}")

def Example_1_Dict():

    Dictionaries = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    # Dictionary items are unordered, changeable, and does not allow duplicates.


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
