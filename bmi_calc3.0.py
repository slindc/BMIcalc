#import

from tkinter import *

#gui

window = Tk()

window.title("slindc's BMI calculator ")

window.geometry('350x200')

#inputedAge = float(input("Persons age in years : ") or "21")
#inputedFeet = float(input("Hight_Feet : ") or "0")
#inputedInches = float(input("Inches : ") or "0")
#inputedLbs = float(input("Weight in # : ") or "1")

# lists

messages =  ["You are underweight! ",
            "Congratulations, you are good! ",
            "You are overweight! ",
            "You are obese! ",
            "Not enough information provided to make BIM calculations."]


# def functions

#def height2M(inputedFeet, inputedInches):
#    return ((inputedFeet * 12) + inputedInches) * .0254

#def weight2Kilo(inputedLbs):
#    return inputedLbs/ 2.2046

#def calcBMI(weight, height):
#    if (weight == 0 or height == 0): return 1000001
 #   return round(weight / height ** 2, 1)

#manipulate data

#height = height2M(inputedFeet, inputedInches)
#weight = weight2Kilo(inputedLbs)
#bmi = calcBMI(weight, height)



#results

#print(bmi)

#if (inputedAge<= 20):
#    input("Plot on graph @ https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/about_childrens_bmi.html")
#else:
#    if bmi < 18.5:
#        input(messages[0])
 #   elif bmi <= 24.9:
 #       input(messages[1])
 #   elif bmi <= 29.9:
 #       input(messages[2])
 #   elif bmi <= 1000000:
 #       input(messages[-2])
 #   else:
 #       input(messages[-1])


lbl1 = Label(window, text="Age in years: ")

lbl1.grid(column=0, row=0)

txt1 = Entry(window, width=10)

txt1.grid(column=1, row=0)

txt1.focus()

lbl2 = Label(window, text="Hight in feet: ")

lbl2.grid(column=0, row=3)

txt2 = Entry(window, width=10)

txt2.grid(column=1, row=3)

lbl3 = Label(window, text="Inches: ")

lbl3.grid(column=2, row=3)

txt3 = Entry(window, width=10)

txt3.grid(column=3, row=3)

lbl4 = Label(window, text="Weight in lbs: ")

lbl4.grid(column=0, row=4)

txt4 = Entry(window, width=10)

txt4.grid(column=1, row=4)

lbl5 = Label(window, text="BMI")

lbl5.grid(column=1, row=6, pady=(10, 10))

BMI_field = Text(window, height=1, width=6)

BMI_field.grid(column=2, row=6, pady=(10, 10))

message_field = Text(window, height=2, width=40)

message_field.grid(columnspan=9, row=8, pady=(10, 10), padx=(10, 100))

#message_field.insert(END, )

window.mainloop()


# title

# set variables











