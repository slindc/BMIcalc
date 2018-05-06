
# coding: utf-8

# In[53]:


print("slindc's ADULT BMI calc" )
h1=float(input("Hight_Feet ") or "0");
# h1=float(h1)

h2=float(input("Inches ") or "0")
# h2=float(h2)

h=((h1*12)+h2)*.0254
w1=float(input("Weight in # ") or "1")
# w1=float(w1)

w=w1/2.2046
# w=float(w)

b=w/h**2
# b=float(b)

print("BMI="+str(b))
if b<=25:
  input("Congratulations, you are good! ")
elif 25<b<=30:
  input("You are overweight! ")
else:
  input("You are obese! ")

# x=input("")
