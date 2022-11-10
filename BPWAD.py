########################################################################################################################
# ABlood pressure Early Warning And Detection Root file
########################################################################################################################
# Authors
#   Richard Johnston 
#   Jyothi Cameron
#   Austin Strand
#
# Created Date
#   2022-11-06
#
# Description
#   Calculate blood pressure information
#
########################################################################################################################
# BEGIN WORKING DOCUMENT
########################################################################################################################

# import custom module from BPEWAD_Modules Package
from posixpath import split
#import BPEWAD_Modules.bp_math as bpm
import sqlite3

# define the class
class Root():
    # define the scope of the project
    def __init__(self):
        super(Root, self).__init__()
        # call the app
        self.app()

    def create_patient(self):
        patient_name = str(input("What is your name? "))
        patient_address = str(input("What is your address? "))
        patient_phone = int(input("What is your Phone number? "))
        patient_allergies = str(input("Tell us what you are allegic to "))
        patient_doctor_name = str(input("What is the name of your doctor? "))
        patient_doctor_phone = int(input("What is your doctor's phone number? "))

    def wellness_check(self, diastolic, sistolic):
        if 120 > diastolic or diastolic > 149 or 70 > sistolic or sistolic > 89:
            Ok = input("Are you feeling ok (y/N)? ")
            print(Ok)
            if Ok == 'y' or Ok == 'Y':
                pass
            else:
                emt = input("Do you need emergency services (y/N)? ")
                if emt == "y" or emt == "Y":
                    print("Emergency Services called")
        else:
            pass
    def app(self):
        # since the calculations and printing is handled by the 
        # "bp_math" module in the "BPEWAD_MOdules" package, this will do nothing. 
        # the calculations are completed simply by importing the module. 
        # for reference, this is bad practice so it should be changed.
        self.create_patient()
        self.wellness_check(140, 80)



def main():
    # call Root(), which wiill call app()
    Root()


if __name__ == "__main__":
    # call main(), which will call Root(), which wiill call app(). This technique
    # is called a "main guard" and defines the "entry point" into the program.
    # allows you to both run code in the module directly and also use classes from other modules
    main()