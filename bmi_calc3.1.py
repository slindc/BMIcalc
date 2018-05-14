#import

from tkinter import *

#gui

window = Tk()
window.configure(bg="#FFA500")
window.title("slindc's BMI calculator ")


window.geometry('410x190')

ageLabel = Label(window, bg="#FFA500", text="Age in years: ")

ageLabel.place(x=20, y=10)

ageText = Entry(window, width=10)
ageText.place(x=120, y=10)
ageText.focus()
ageText.bind('<Return>')

hightFlabel = Label(window, bg="#FFA500", text="Hight in feet: ")
hightFlabel.place(x=20, y=40)

hightFtext = Entry(window, width=10)
hightFtext.place(x=120, y=40)

hightIlabel = Label(window,bg="#FFA500", text="Inches: ")
hightIlabel.place(x=235, y=40)

hightItext = Entry(window, width=10)
hightItext.place(x=300, y=40)

weightLabel = Label(window, bg="#FFA500", text="Weight in lbs: ")
weightLabel.place(x=20, y=70)

weightText = Entry(window, width=10)
weightText.place(x=120, y=70)

bmiLabel = Label(window, bg="#FFA500", text="Calculated BMI : ")
bmiLabel.place(x=140, y=110)

# set variables

#inputedAge = float(txt1.get())
#inputedFeet = float(txt2.get())
#inputedInches = float(txt3.get())
#inputedLbs = float(txt4.get())

# def functions

def height2M(inputedFeet, inputedInches):
     return ((inputedFeet * 12) + inputedInches) * .0254

def weight2Kilo(inputedLbs):
     return inputedLbs/ 2.2046

def calcBMI(weight, height):
     if (weight == 0 or height == 0): return 1000001
     return round(weight / height ** 2, 1)


bmiField = Label(window, bg="#FFA500")
#bmiField.configure(text=bmi)
#bmiField.insert(INSERT, bmi)
bmiField.place(x=250, y=110)

messageField = Label(window, bg="#FFA500" )

# message_field = Text(window) #, state=DISABLED)
#messageField.insert(INSERT, "Fish are the gill-bearing aquatic craniate animals that lack limbs with digits. They form a sister group to the tunicates, together forming the olfactores. Included in this definition are the living hagfish, lampreys, and cartilaginous and bony fish as well as various extinct related groups. Tetrapods ")
messageField.place(x=25, y=140, height=40, width=360)

# lists

messages =  ["You are underweight! ",
             "Congratulations, you are good! ",
             "You are overweight! ",
             "You are obese! ",
             "Not enough information provided to make BIM calculations."]


# #manipulate data

#height = height2M(inputedFeet, inputedInches)
#weight = weight2Kilo(inputedLbs)
#bmi = calcBMI(weight, height)

# #results



#if (inputedAge<= 20):
     #messageField.insert(END,("Plot on graph @ https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/about_childrens_bmi.html"))
#else:
     #if bmi < 18.5:
         #messageField.insert(END, (messages[0]))
     #elif bmi <= 24.9:
         #messageField.insert(END, (messages[1]))
     #elif bmi <= 29.9:
         #messageField.insert(END, (messages[2]))
     #elif bmi <= 1000000:
         #messageField.insert(END, (messages[-2]))
     #else:
         #messageField.insert(END, (messages[-1]))

window.mainloop()











