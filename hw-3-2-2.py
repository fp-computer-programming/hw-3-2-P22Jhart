height=float(input("what is your weight in metres"))
weight=float(input("what is your height in kilograms"))
bmi =weight/(height**2)

if   bmi < 19:
    print("underweight")
elif bmi < 25:
    print("healthy")
elif bmi <30:
    print("overweight")
elif bmi < 40:
    print("obese")
