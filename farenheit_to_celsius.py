# Fahrenheit to Celsius converter
def f_to_c(temperature):
    celsius = (5 / 9 * ((int(temperature)) - 32))
    return(int(celsius))
    
def c_to_f(temperature):
    farenheit = ((int(temperature) * 1.8) + 32)
    return(int(farenheit))

#temperature = input("What is the f? ")
#celsius = (5/9*(int(farenheit))-32)
#print("That converts to " + str(f_to_c(temperature)) + " degrees Celsius.")

temperature, farenheit_or_celsius = input("What is the temperature number and unit you want to convert from? (eg. 150 C) ") .split()
if farenheit_or_celsius == "c":
    print(c_to_f(temperature))
if farenheit_or_celsius == "f":
    print(f_to_c(temperature))
