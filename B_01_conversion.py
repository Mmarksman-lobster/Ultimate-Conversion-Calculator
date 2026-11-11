

def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5} ")


def instructions():
    statement_generator("instructions", "-")
    print("""
here are your instructions 
-select the type of conversion your doing(e.g. distance)
-select the base measurement (e.g. meters)
-select which measurement you want to convert it to (e.g. km)
-type "xxx" to end session
- please only use the names it recommends you. example. if it tells you to type "days" dont put "d" it wont work
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



def convert_distance():

    print("\n--- Distance Converter ---")
    print("Available units: mm, cm, m, km")

    # Define conversion rates to base measurement (Meter)
    to_meters = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0}

    from_choice = input("Enter starting unit: ").strip().lower()
    to_choice = input("Enter target unit: ").strip().lower()

    if from_choice not in to_meters or to_choice not in to_meters:
        print(" Invalid unit entered. Returning to main menu.")
        return

    val = num_check(f"Enter the amount of {from_choice} to convert: ",)

    # Convert from starting unit to meters, then meters to target unit
    value_in_meters = val * to_meters[from_choice]
    converted_value = value_in_meters / to_meters[to_choice]

    print(f" {val} {from_choice} = {converted_value} {to_choice}")

def convert_mass():

    print("\n--- Mass Converter ---")
    print("Available units: g, kg, tonne")

    # Define conversion rates to the base unit (Grams)
    to_grams = {'g': 1.0, 'kg': 1000.0, 'tonne': 1000000.0}

    from_choice = input("Enter starting unit: ").strip().lower()
    to_choice = input("Enter target unit: ").strip().lower()

    if from_choice not in to_grams or to_choice not in to_grams:
        print(" Invalid unit entered. Returning to main menu.")
        return

    val = num_check(f"Enter the amount of {from_choice} to convert: ",)

    # Convert from starting unit to grams, then grams to target unit
    value_in_grams = val * to_grams[from_choice]
    converted_value = value_in_grams / to_grams[to_choice]

    print(f" {val} {from_choice} = {converted_value} {to_choice}")

def convert_time():

        print("\n--- Time Converter ---")
        print("Available units: s, min, hour, day ---")

        # Define conversion rates to the base unit (Seconds)
        to_seconds = {'s': 1.0, 'min': 60.0, 'hour': 3600.0, 'day': 86400.0}

        from_choice = input("Enter starting unit: ").strip().lower()
        to_choice = input("Enter target unit: ").strip().lower()

        if from_choice not in to_seconds or to_choice not in to_seconds:
            print(" Invalid unit entered. Returning to main menu.")
            return

        val = num_check(f"Enter the amount of {from_choice} to convert: ")

        # Convert from starting unit to seconds, then seconds to target unit
        value_in_seconds = val * to_seconds[from_choice]
        converted_value = value_in_seconds / to_seconds[to_choice]

        print(f" {val} {from_choice} = {converted_value} {to_choice}")
# main routine goes here
statement_generator ( "the ultimate conversion calculator","=")


want_instructions = input("press <enter> to see instructions"
                              " or any key to continue")

if want_instructions == "":
    instructions()

print()
#loop
def menu():
    while True:
        print()
        print("Type: 'distance', 'time', or 'mass'")
        print("Type: 'xxx' to quit")
        print()
        menu_choice = input("Select a category: ").strip().lower()

        if menu_choice == 'distance':
            convert_distance()
        elif menu_choice == 'time':
            convert_time()
        elif menu_choice == 'mass':
            convert_mass()
        elif menu_choice in ['xxx']:
            print("\nThank you for using my ultimate conversion calculator"
                  "\n Goodbye")
            break
        else:
            print(" Invalid selection. Please type distance, time, mass, or xxx.")

if __name__ == "__main__":
    menu()