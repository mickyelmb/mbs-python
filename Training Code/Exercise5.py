temperatures = [10,- 20, -289, 100]

def celsius_to_fahrenheit(degrees_celsius):
    fahrenheit = (9/5 * float(degrees_celsius) + 32)
    return fahrenheit

for temp in temperatures:
    if temp < -273.15:
        print("Sorry -273.15 is the lowest temperature that physical matter can reach. ")
    else:
        with open("DegreesFahrenheit.txt", "a+") as file:
             file.write( str(temp) + "\n")

