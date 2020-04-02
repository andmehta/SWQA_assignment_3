def convert_to_meters(feet, inches):
    if feet <= 0 or inches < 0:
        print("Invalid height")
        raise SystemExit
    return (feet*12 + inches)*0.025


def convert_to_kg(weight):
    if weight <= 0:
        print("Invalid weight")
        raise SystemExit
    return weight*.45


def category_check(value):
    if value <= 0:
        print("Invalid BMI value")
        raise SystemExit

    if 0 < value < 18.5:
        return "Underweight"

    if 18.5 <= value < 25:
        return "Normal"

    if 25 <= value < 30:
        return "Overweight"

    if value >= 30:
        return "Obese"


# bmi is kg/(m)^2
def bmi(height_f, height_i, weight):
    height_m = convert_to_meters(height_f, height_i)
    kg = convert_to_kg(weight)
    bmi_value = round(kg/height_m**2, 1)
    category = category_check(bmi_value)

    return bmi_value, category
