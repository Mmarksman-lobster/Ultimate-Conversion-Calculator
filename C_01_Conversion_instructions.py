def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5} ")


def instructions():
    statement_generator("instructions", "-")
    print("""
Instructions here
-select the number for your initial measurement
-select which type of measurement it is 
-select which measurement you want to convert it to
-type "xxx" to end session
    """)

want_instructions = input("press <enter> to see instructions"
                              " or any key to continue")

if want_instructions == "":
    instructions()