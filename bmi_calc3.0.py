#import

from tkinter import *

#gui

window = Tk()

window.title("slindc's BMI calculator ")

window.geometry('410x190')







lbl1 = Label(window, text="Age in years: ")

# lbl1.grid(column=0, row=0)

# .place() move the lable around.
lbl1.place(x=20, y=10)   


txt1 = Entry(window, width=10)

txt1.place(x=120, y=10)
# txt1.grid(column=1, row=0)

txt1.focus()
txt1.bind('<Return>')


lbl2 = Label(window, text="Hight in feet: ")
lbl2.place(x=20, y=40)
# lbl2.grid(column=0, row=3)



txt2 = Entry(window, width=10)
txt2.place(x=120, y=40)
# txt2.grid(column=1, row=3)


lbl3 = Label(window, text="Inches: ")
lbl3.place(x=235, y=40)
# lbl3.grid(column=2, row=3)

txt3 = Entry(window, width=10)
txt3.place(x=300, y=40)

# txt3.grid(column=3, row=3)

lbl4 = Label(window, text="Weight in lbs: ")
lbl4.place(x=20, y=70)
# lbl4.grid(column=0, row=4)

txt4 = Entry(window, width=10)
txt4.place(x=120, y=70)

# txt4.grid(column=1, row=4)

lbl5 = Label(window, text="Calculated BMI : ")
lbl5.place(x=140, y=110)
# lbl5.grid(column=1, row=6, pady=(10, 10))

# set variables

inputedAge = float(txt1.get())
inputedFeet = float(txt2.get())
inputedInches = float(txt3.get())
inputedLbs = float(txt4.get())

BMI_field = Label(window, text=" ??? ", bg="dark grey")
BMI_field.place(x=250, y=110)
# BMI_field.grid(column=2, row=6, pady=(10, 10))

message_field = Label(window, text="", bg="dark grey")

# message_field = Text(window) #, state=DISABLED)
# message_field.insert(INSERT, "Fish are the gill-bearing aquatic craniate animals that lack limbs with digits. They form a sister group to the tunicates, together forming the olfactores. Included in this definition are the living hagfish, lampreys, and cartilaginous and bony fish as well as various extinct related groups. Tetrapods ")
message_field.place(x=25, y=140, height=40, width=360)

# lists

messages =  ["You are underweight! ",
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

# #manipulate data

height = height2M(inputedFeet, inputedInches)
weight = weight2Kilo(inputedLbs)
bmi = calcBMI(weight, height)



# #results

BMI_field.insert(INSERT, bmi)

if (inputedAge<= 20):
     message_field.insert(END,("Plot on graph @ https://www.cdc.gov/healthyweight/assessing/bmi/childrens_bmi/about_childrens_bmi.html"))
else:
     if bmi < 18.5:
         message_field.insert(END, (messages[0]))
     elif bmi <= 24.9:
         message_field.insert(END, (messages[1]))
     elif bmi <= 29.9:
         message_field.insert(END, (messages[2]))
     elif bmi <= 1000000:
         message_field.insert(END, (messages[-2]))
     else:
         message_field.insert(END, (messages[-1]))


# message_field.grid(columnspan=9, row=8, pady=(10, 10), padx=(10, 100))

window.mainloop()












