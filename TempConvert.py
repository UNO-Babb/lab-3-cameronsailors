#TempConvert.py
#Name: Cameron Sailors
#Date: 2/5/2025
#Assignment: Temperature Conversion


def main():
  #Prompt the user for a Fahrenheit temperature
  fahrenheit = input("Enter temperature in Fahrenheit: ")
  fahrenheit = int(fahrenheit)
  #Convert that temperature to celsius, rounding to 1 decimal percision
  celsius = (fahrenheit - 32) * 5 / 9
  #Output converted temperature.
  print("Temperature in Celsius: " + str(round(celsius,1)))

if __name__ == '__main__':
  main()
