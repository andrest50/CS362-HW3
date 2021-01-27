"""
This is an updated version of the file from homework 1, except
there is now some error handling.

To run the script, use the following command:

    python3 andres_tobon_hw3.py
"""

def main():
    valid = False

    while(valid == False):
        yearString = input("Input a year: ")
        try:
            year = int(yearString)
            if(year < 1):
                raise ValueError
            valid = True
        except ValueError:
            print("Invalid year. Input a positive integer number.")

    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print("{} is a leap year.".format(year))
            else:
                print("{} is not a leap year.".format(year))
        else:
            print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))

main()