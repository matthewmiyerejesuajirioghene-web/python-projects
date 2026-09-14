try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
    print(risk)

except ZeroDivisionError:
    print('Invalid age')
except ValueError:
    print('Invalid Value')