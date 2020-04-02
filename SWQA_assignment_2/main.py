# imports here
from bmi import bmi
from retire import retire


def show_menu():
    print("\"bmi\": to calculate BMI and determine if underweight, normal, or overweight.")
    print("\"retire\": calculate retirement age based off current age, annual salary, and percentage saved.")
    print("\"menu\": to see all available options")
    print("\"end\": to close program\n")


def main():
    print("welcome to the main menu")

    # initialize option before using in while loop
    option = "placeholder"

    print("type \"menu\" to see all available options")
    while option != "end":
        option = input("\nWhat would you like to do?: ")

        if option == "menu":
            show_menu()

        if option == "bmi":
            weight = float(input("What is your weight?: "))
            height_f = float(input("What is your height in feet?: "))
            height_in = float(input("What is your height in inches?: "))
            bmi_value, category = bmi(height_f, height_in, weight)
            print("BMI:", bmi_value, "\nCategory:", category)

        if option == "retire":
            age = int(input("What is your current age?: "))
            salary = float(input("What is your annual salary?: "))
            save = float(input("What is your percentage saved?: "))
            desired_save = float(input("What is your desired retirement savings goal?: "))
            retire_age = int(retire(age, salary, save, desired_save))
            if retire_age > 0:
                print("You will retire at", retire_age, ".")
            else:
                print("You will not save enough, increase percentage saved or start getting paid more.")


if __name__ == "__main__":
    main()
