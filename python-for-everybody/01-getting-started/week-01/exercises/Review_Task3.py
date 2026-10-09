#Task 3: Input and processing
#Ask the user for a temperature in Celsius, convert it to Fahrenheit (F = C × 9/5 + 32), and print the result. Test with 100, which should give 212.0.

tempc=input("Enter temperature in Celsius:")
celc=float(tempc)
tempf=float((celc * (9/5)) + 32)
print(tempf)