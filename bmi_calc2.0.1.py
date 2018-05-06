# import
# title
print("slindc's BMIcalc")
# set variables
inputedAge = float(input("Persons age in years : ") or "21")
inputedFeet = float(input("Hight_Feet : ") or "0")
inputedInches = float(input("Inches : ") or "0")
inputedLbs = float(input("Weight in # : ") or "1")

# lists

messages =  ["You are underweight!",
            "Congratulations, you are good! ",
            "You are overweight! ",
            "You are obese! ",
            "Not enough information provided to make BIM calculations."]


# def functions

def height2M(inputedFeet, inputedInches):
    return ((inputedFeet * 12) + inputedInches) * .0254

def weight2Kilo(inputedLbs):
    return inputedLbs/ 2.2046

def calcBMI(weight, height):
    if (weight == 0 or height == 0): return 1000001
    return round(weight / height ** 2, 1)

#manipulate data

height = height2M(inputedFeet, inputedInches)
weight = weight2Kilo(inputedLbs)
bmi = calcBMI(weight, height)



#results

print(bmi)

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

# gui