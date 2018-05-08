#!/usr/bin/python

import webbrowser
from tkinter import *

window = Tk()

messageText = StringVar()
bmiText = StringVar()  # this is the initial declaration of the label targeting varible used below
ageText = StringVar()
weightText = StringVar()
heightFText = StringVar()
heightIText = StringVar()

validAge = False  # these used to make sure everything is ready to calculate
validFeet = False
validInches = False
validWeight = False
isMinor = False

age = -1
feet = -1
inches = -1
weight = -1

def isfloat(value):  #this function is used to retun a float if string is valid number or -1 if not
  try:
    t = float(value)
    return t
  except ValueError:
    return -1

def height2M(inputedFeet, inputedInches):
    return ((inputedFeet * 12) + inputedInches) * .0254

def weight2Kilo(inputedLbs):
    return inputedLbs/ 2.2046

def calcBMI(weight, height):
    if (weight == 0 or height == 0): return 1000001
    return round(weight / height ** 2, 1)

def makeBMICalc():
    if (validAge and validFeet and validInches and validWeight):  # checks first that everything is ready
        messageText.set("Made it!")
        height = height2M(feet, inches)
        kelo = weight2Kilo(weight)
        bmi = calcBMI(kelo, height)
        bmiText.set(bmi)
        messages =  ["You are underweight! ",
                    "Congratulations, you are good! ",
                    "You are overweight! ",
                    "You are obese! ",
                    "Not enough information provided to make BIM calculations."]

        if bmi < 18.5:
            messageText.set(messages[0])
        elif bmi <= 24.9:
            messageText.set(messages[1])
        elif bmi <= 29.9:
            messageText.set(messages[2])
        elif bmi <= 1000000:
            messageText.set(messages[-2])
        else:
            messageText.set(messages[-1])
    else:
        messageText.set("")
    return True


def callbackAge():   #  This is the function that the remed callback below runs
    temp = isfloat(ageText.get())
    global isMinor
    if (temp > 20):
        global age 
        age = temp
        global validAge 
        validAge = True
        makeBMICalc()
        isMinor = False
    elif (temp > -1):
        messageText.set("Plot on graph @ https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/about_childrens_bmi.html")
        isMinor = True
    return True


def clickFunction(self):  # function called when lable is clicked only allows if isMinor is true
    if (isMinor):
        messageText.set("Opening page in default browser!")
        webpage = 'https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/about_childrens_bmi.html'
        webbrowser.open_new_tab(webpage)
    return True


def callbackFeet():
    temp = isfloat(heightFText.get())
    if (temp > -1):
        global feet 
        feet = temp
        global validFeet 
        validFeet = True
        makeBMICalc()
    return True


def callbackInches():
    temp = isfloat(heightIText.get())
    if (temp > -1):
        global inches 
        inches = temp
        global validInches 
        validInches = True
        makeBMICalc()
    return True

def callbackWeight():
    temp = isfloat(weightText.get())
    if (temp > -1):
        global weight 
        weight = temp
        global validWeight 
        validWeight = True
        makeBMICalc()
    return True



window.title("gwc's BMI calculator ")

window.geometry('410x200')


#Age
lbl1 = Label(window, text="Age in years: ")
lbl1.place(x=20, y=10)   
                                                    # this sais to validate on leaving
txt1 = Entry(window, width=10, textvariable=ageText, validate="focusout", validatecommand=callbackAge)
txt1.place(x=120, y=10)                                                     # this is the function it calls
txt1.focus()

#Feet
lbl2 = Label(window, text="Hight in feet: ")
lbl2.place(x=20, y=40)

txt2 = Entry(window, width=10, textvariable=heightFText, validate="focusout", validatecommand=callbackFeet)
txt2.place(x=120, y=40)

#Inches
lbl3 = Label(window, text="Inches: ")
lbl3.place(x=235, y=40)

txt3 = Entry(window, width=10, textvariable=heightIText, validate="focusout", validatecommand=callbackInches)
txt3.place(x=300, y=40)

#Weight
lbl4 = Label(window, text="Weight in lbs: ")
lbl4.place(x=20, y=70)

txt4 = Entry(window, width=10, textvariable=weightText, validate="focusout", validatecommand=callbackWeight)
txt4.place(x=120, y=70)

#BMI Display
lbl5 = Label(window, text="Calculated BMI : ")
lbl5.place(x=140, y=110)
                            # this textvariable is how the lable is targeted
BMI_field = Label(window, textvariable=bmiText, bg="dark grey")
bmiText.set(" ??? ")  # this is how it is targeted
BMI_field.place(x=250, y=110)

#Message
message_field = Label(window, textvariable=messageText, wraplength=350, bg="dark grey")
message_field.place(x=20, y=140, height=50, width=370)
message_field.bind("<Button-1>", clickFunction) # this binds a "button click" to the label

window.mainloop()










