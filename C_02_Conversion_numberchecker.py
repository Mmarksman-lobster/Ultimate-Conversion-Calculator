#ask user for width and loop
# until they enter a number more than 0
def num_check(question):

    error = "please enter a number that is more than 0\n"
    while True:

        try:
    #ask user for number
             response = float(input(question))

             #check number is more than 0
             if response > 0:
                return response
             else:
                 print(error)
        except ValueError:
            print (error)