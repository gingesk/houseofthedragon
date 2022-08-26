
def main(): #main menu of the health calculator.
    body_mass_index = 0
    classification = ""
    basal_metabolic_rate = 0
    max_heart_rate = 0
    target_heart_rate = [0,0] #initialises all of the health calculation result variables.
    
    print("Welcome to the health calculator!") #data gathering of preferred units, gender, height, weight, and age begins.
    units = get_string_input("Enter which units you will use throughout this calculator","IMPERIAL","METRIC")
    gender = get_string_input("Enter which gender you are, or would like to use, for calculations","MALE","FEMALE")
    height = get_numerical_input("height in meters or inches",0,120)
    weight = get_numerical_input("weight in kilograms or pounds",0,1200)
    age = get_numerical_input("age",0,120)
    if units == "IMPERIAL":
        height = convert_height(height)
        weight = convert_weight(weight)
    print("\nAll data has been received, the health calculator is ready.") #data gathering from the user is complete.
    
    while True:
        choice = get_string_input("Enter what you would like to calculate and display, or EXIT to exit","BMI","BMR","MHR","THR","EXIT") #gets the user's choice of calculation.
        if choice == "BMI": #calculates and displays BMI (body mass index), as well as the classification of their weight.
            body_mass_index = calculate_bmi(weight,height)
            print(f"\nYour BMI (body mass index) is {body_mass_index}.")
            if body_mass_index < 18.5:
                classification = "underweight"
            elif body_mass_index < 25:
                classification = "normal"
            elif body_mass_index < 30:
                classification = "overweight"
            else:
                classification = "obese"
            print(f"That is '{classification}'.")
            print("\nDisclaimer: BMI’s are only an indicator and do not replace medical advice from a doctor. BMI’s can be inaccurate for some people such as bodybuilders or professional athletes, the elderly, children and teenagers, lactating or pregnant women and for certain ethnicities. Please seek professional medical advice if you require it.")
    
        elif choice == "BMR": #calculates and displays BMR (basal metabolic rate).
            basal_metabolic_rate = calculate_bmr(weight,height,gender,age)
            print(f"\nYour BMR (basal metabolic rate) is {basal_metabolic_rate}.")

        elif choice == "MHR": #calculates and displays MHR (maximum heart rate).
            max_heart_rate = calculate_mhr(age)
            print(f"\nYour MHR (maximum heart rate) is {max_heart_rate}.")

        elif choice == "THR": #calculates and displays THR (target heart rate).
            max_heart_rate = calculate_mhr(age)
            target_heart_rate = calculate_thr(max_heart_rate)
            print(f"\nYour THR (target heart rate) is between {target_heart_rate[0]} and {target_heart_rate[1]}.")
    
        else: #exits the program if the input was 'EXIT', or in the rare event the input is not one of the other available options.
            print("\nNow exiting the health calculator program...")
            break

def calculate_bmi(weight,height): #calculates BMI with weight in kilograms and height in meters.
    bmi = weight/(height*height)
    return bmi

def calculate_bmr(weight,height,gender,age): #calculates BMR with weight in kilograms and height in meters, depending on gender.
    bmr = (10*weight)+(6.25*(height/100))-(5*age)
    if gender == "MALE":
        bmr = bmr+5
    else:
        bmr = bmr-161
    return bmr

def calculate_mhr(age): #calculates MHR based on age.
    if age < 40:
        mhr = 220-age
    else:
        mhr = 208 - (0.75*age)
    return mhr

def calculate_thr(mhr): #calculates THR range with MHR.
    lhr = mhr*0.5
    uhr = mhr*0.85
    thr = [lhr,uhr]
    return thr

def convert_height(inches): #converts height in inches to height in meters.
    meters = inches/39.37
    return meters

def convert_weight(pounds): #converts weight in pounds to weight in kilograms.
    kilograms = pounds/2.205
    return kilograms

def get_numerical_input(value,low,high): #gets a given value from the user and validates it as a float within the low and high limits.
    while True:
        try:
            user_input = int(input(f"\nPlease enter your {value}: "))
            if user_input <= low:
                print(f"Error: Your input was below the minimum value. It must be more than {low}.")
            elif user_input > high:
                print(f"Error: Your input was above the maximum value. It can't be more than {high}.")
            else:
                return user_input
        except ValueError:
            print("Error: Your input was not a real number. Don't include letters for units such as kg, lbs, etc.")

def get_string_input(message,*options): #gets a string input and returns which option it matches.
    while True:
        user_input = input(f"\n{message}: ")
        user_input = user_input.upper()
        if user_input == "HELP":
            print("Your available options are:")
            for option in options:
                print(option)
        else:
            for option in options:
                if user_input == option:
                    return user_input
            print("Error: Your input does not match any of the available options. To see them, enter 'HELP'.")

main()