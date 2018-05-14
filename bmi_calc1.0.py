
# coding: utf-8

# In[53]:

print("slindc's ADULT BMI calc" )
h1=input("Hight_Feet ")
h1=float(h1)
h2=input("Inches ")
h2=float(h2)
h=((h1*12)+h2)*.0254
w1=input("Weight in # ")
w1=float(w1)
w=w1/2.2046
w=float(w)
b=w/h**2
b=float(b)
print("BMI="+str(b))
if b<=25:
  print("congratulations, you are good!")
elif 25<b<=30:
  print("you are overweight")
else:
  print("you are obese")

x=input("")
