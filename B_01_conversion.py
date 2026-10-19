from C_02_Conversion_numberchecker import num_check


def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5} ")


def instructions():
    statement_generator("instructions", "-")
    print("""
here are you instructions my 
-select the number for your initial measurement
-select which type of measurement it is 
-select which measurement you want to convert it to
-type "xxx" to end session
    """)

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

distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": 0.001
}

time_dict = {
    "second": 1/3600,
    "minute": 1/60,
    "hour": 1,
    "day": 1/24
}




# main routine goes here
statement_generator ( "the ultimate conversion calculator","=")


want_instructions = input("press <enter> to see instructions"
                              " or any key to continue")

if want_instructions == "":
    instructions()

print()
#loop
while True:


    #gain number and measurement info
    print()
    print()
    dict_check = input("which conversion are you doing, distance, time, mass, volume")
    original_measurement = num_check("what is your number?")
    original_unit = input("your unit for the number is?")
    new_unit = input("what unit do you want it do be converted to?")
    print(f"your measurement is {original_measurement}{original_unit} and it goes to {new_unit}")



