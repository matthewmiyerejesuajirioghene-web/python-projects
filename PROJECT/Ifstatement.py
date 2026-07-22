is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes') 
else:
    print("It's a cold day")
    print('Wear warm clothes')

print("Enjoy your day")


price_house = 1000000
good_credit = input('Do you have good credit? ')

if good_credit:
    print('You need to put down 10%')
    print(1000000/10)
else:
    print('You need to put down 20%')
    print(1000000/20)
print("Thanks for your interest")