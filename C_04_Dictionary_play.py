my_dict = {
    "blue": "sky",
    "red" :"apple",
    "yellow":"bannana",
    "green":"grass"
}

to_find = input("what are you looking for?")

#check if its a key
if to_find in my_dict:

    #get the value
    coloured_object = my_dict[to_find
    ]
    print(f"the {coloured_object} is {to_find}")

elif to_find in my_dict.values():
    print(f"{to_find} is a value in the dictionary")

else:
    print("sorry item not found")