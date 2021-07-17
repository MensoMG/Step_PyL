age = int(input())
height = float(input())
weight = float(input())

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:    
    print("Ошибочные входные данные")
else:
    bmi = weight / height ** 2  
    bmi = round(bmi, 2)
#Если возраст < 45
    if age < 45:
        if bmi < 18.5:
            description = "недостаточной массой тела."            
        elif bmi < 25:
            description = "нормальной массой тела."            
        elif bmi < 30:
            description = "избыточной массой тела."  
        else:          
            description = "ожирением."
#Если возраст >= 45
    if age >= 45:
        if bmi < 22:
            description = "недостаточной массой тела."            
        elif bmi < 26.99:
            description = "нормальной массой тела."            
        elif bmi < 31.99:
            description = "избыточной массой тела."  
        else:          
            description = "ожирением."

    print("bmi=", bmi, "Вы относитесь к группе людей с", description)
