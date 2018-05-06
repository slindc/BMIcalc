# import
# Title
print("slindc's BMIcalc")
# set var
inputedAge = float(input("Persons age in years : ") or "21")
inputedFeet = float(input("Hight_Feet : ") or "0")
inputedInches = float(input("Inches : ") or "0")
inputedLbs = float(input("Weight in # : ") or "1")


# def functions
def height2CM(inputedFeet, inputedInches):
    return ((inputedFeet * 12) + inputedInches) * .0254


height = height2CM(inputedFeet, inputedInches)



def weight2Kilo(inputedLbs):
    return inputedLbs/ 2.2046


weight = weight2Kilo(inputedLbs)


def calcBMI(weight, height):

    if (weight == 0 or height == 0): return 1000001

    return round(weight / height ** 2, 1)


bmi = calcBMI(weight, height)

print(bmi)

# list
# L = [["You are underweight!"], ["Congratulations, you are good! "], ["You are overweight! "], ["You are obese! "]]

messages =  ["You are underweight!", 
            "Congratulations, you are good! ", 
            "You are overweight! ", 
            "You are obese! ",
            "Not enough information porvided to make BIM calculations."]

if (inputedAge<= 20):
    input("Plot on graph @ https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/about_childrens_bmi.html")
else:
    if bmi < 18.5:
        input(messages[0])
    elif bmi <= 24.9:
        input(messages[1])
    elif bmi <= 29.9:
        input(messages[2])
    elif bmi <= 1000000:
        input(messages[-2])
    else:
        input(messages[-1])

# GUI