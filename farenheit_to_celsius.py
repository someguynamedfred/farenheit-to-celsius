# Fahrenheit to Celsius converter
def f_to_c(temperature):
    celsius = (5 / 9 * ((int(temperature)) - 32))
    return(int(celsius))
#for the sake of learning, here is a simpler code
#def f_to_c(temperature):
#    return (((temperature) - 32)*5/9)
    
def c_to_f(temperature):
    farenheit = ((int(temperature) * 1.8) + 32)
    return(int(farenheit))

#temperature = input("What is the f? ")
#celsius = (5/9*(int(farenheit))-32)
#print("That converts to " + str(f_to_c(temperature)) + " degrees Celsius.")

temperature, farenheit_or_celsius = input("What is the temperature number and unit you want to convert from? (eg. 150 C) ") .split()
if farenheit_or_celsius == "c":
    print(str(temperature) + " degrees Celsius is equal to " + str(c_to_f(temperature)) + " degrees Farenheit.")
if farenheit_or_celsius == "f":
    print(str(temperature) + " degrees Farenheit is equal to " + str(f_to_c(temperature)) + " degrees Celsius.")
