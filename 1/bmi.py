def bmi():

    try:
        height=float(input("Please Enter height in meter:\n"))
        weight=float(input("Please Enter weight in Kilogram:\n"))
        if weight>=0 and height>=0:
            BMI=weight/(height**2)
            if 0<=BMI<18.5:
                print("Underweight")
            elif 18.5<=BMI<=24.9:
                print("Normal weight")
            elif 25<=BMI<=29.9:
                print("Overweight")
            elif 30<=BMI<=34.9:
                print("Obesity")
            elif 35<=BMI<=39.9:
                print("extreme Obesity")
        else:
            print("height and weight could not be negative")
    except:
        print("input is not a number.")



bmi()