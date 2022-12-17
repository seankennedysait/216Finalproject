#####
# Sean Kennedy
# December 15 2022
# This program is to view and edit files on the alberta health system.
#
# Version 1.0.0
#####
#Program start
selection = int
import math
#from projectclasses_laboratory.py import laboratory
class laboratory:
    def __init__(self):
        pass
    lab_list = []
    # constructor 
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    def labmenu ():
        lab_selection = int(9)
        while (lab_selection!=3):
            lab_selection = int(input(f"Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n"))
            if (lab_selection == 1):
                laboratory.readLaboratoriesFile()
                laboratory.displayLabsList()
            if (lab_selection == 2):
                laboratory.readLaboratoriesFile()
                laboratory.addLabToFile()
                laboratory.writeListOfLabsToFile()
            if (lab_selection == 3):
                pass
    def addLabToFile ():
        laboratory.lab_list.append(laboratory.enterLaboratoryInfo())
    def writeListOfLabsToFile ():
        f = open("laboratories.txt", "w")
        f.truncate(0)
        for c in range(len(laboratory.lab_list)):
            f.write(f"{laboratory.formatLabInfo(c)}\n")
        f.close()
        laboratory.lab_list.clear
    def displayLabsList ():
        for a in range(len(laboratory.lab_list)):
            print(f"{laboratory.lab_list[a][0]}\t            {laboratory.lab_list[a][1]}\n")
        print("Back to the prevoius Menu")
        return
    def formatLabInfo (c):
        formattedvalue = str(f"{laboratory.lab_list[c][0]}_{laboratory.lab_list[c][1]}")
        return formattedvalue
    def enterLaboratoryInfo ():
        labname = str(input("Enter Laboratory facility:\n"))
        labcost = str(input("Enter Laboratory cost:\n"))
        return (labname, labcost)
    def readLaboratoriesFile ():
        list = []
        file = open("laboratories.txt", 'r')
        read = file.readlines()
        for line in read:
            list.append(line.strip())
        for x in range(len(list)):
            laboratory.lab_list.append(list[x].split("_"))
        file.close()
        return




class managment:
    def __init__(self):
        pass
    def mainmenu ():
        menu = int(9)
        while (menu!=0):
            menu = int(input(f"Welcome to Alberta Hospital (AH) Managment system \nSelect from the following options, or select 0 to stop:\n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n\n"))
            if (menu == 1):
                print ("Doctors")
            if (menu == 2):
                print("Facilities")
            if (menu == 3):
                laboratory.labmenu()
            if (menu == 4):
                print("Patients")
            if (menu == 0):
                exit

managment.mainmenu()
