# import
# Title
print("slindc's BMIcalc")
# set var
a = float(input("Persons age in years") or "21")
h1 = float(input("Hight_Feet ") or "0")
h2 = float(input("Inches ") or "0")
w1 = float(input("Weight in # ") or "1")


# def functions
def fh(h1, h2):
    return ((h1 * 12) + h2) * .0254


h = fh(h1, h2)


def fw(w1):
    return w1 / 2.2046


w = fw(w1)


def fb(w, h):
    return round(w / h ** 2, 1)


b = fb(w, h)

print(b)

# list
L = [["You are underweight!"], ["Congratulations, you are good! "], ["You are overweight! "], ["You are obese! "]]

if (a <= 20):
    input("Plot on graph @ https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/about_childrens_bmi.html")
else:
    if b < 18.5:
        input(L[0])
    elif b <= 24.9:
        input(L[1])
    elif b <= 29.9:
        input(L[2])
    else:
        input(L[3])

# GUI
