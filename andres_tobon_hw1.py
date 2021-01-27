"""
Note: This is not very effective syntactically, but it is
meant to follow the flowchart to show understanding of the design.

To run the script, use the following command:

    python3 andres_tobon_hw1.py
"""

def main():
    year = int(input("Input a year: "))
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