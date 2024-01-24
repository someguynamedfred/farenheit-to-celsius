# Fahrenheit to Celsius converter
def f_to_c(farenheit):
    celsius = (5/9*(int(farenheit))-32)
    return(celsius)

farenheit=input("What is the f? ")

#I want this in the function above but the function isn't working
celsius = (5/9*(int(farenheit))-32)

#this should print the function
print(int(celsius))

#this isn't working
print(f_to_c(celsius))
