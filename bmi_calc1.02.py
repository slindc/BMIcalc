b=(1/((((((float(input("slindc's ADULT BMI calc\nHight_Feet ") or "0"))*12)+(float(input("Inches ") or "0")))*.0254))**2))*((float(input("Weight in # ") or "1"))/2.2046)
print("BMI="+str(b))
if b<=25: input("Congratulations, you are good!")
elif 25<b<=30: input("You are overweight! ")
else: input("You are obese! ")

