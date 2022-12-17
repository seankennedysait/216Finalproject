#####
# Sean Kennedy
# December 15 2022
# This program is to view and edit files on the alberta health system.
#
# Version 1.0.0
#####

from tabulate import tabulate

class Laboratory:
    __name:str
    __cost:float

    # constructor 
    def __init__(self, name:str, cost:str):
        assert (cost >= 0)
        self.__name = name
        self.__cost = cost

    def addLabToFile(self, filename:str):
        labFile = open(filename, "a")
        labFile.write(f"{self.formatLabInfo()\n}")
        labFile.close()

    @staticmethod
    def writeListOfLabsToFile(labList:list, filename:str):
        labFile = open(filename, "w")
        labFile.write(labFormatInFile)
        for lab in labList:
            labFile.write(f"{lab.formatLabInfo()}\n")
        labFile.close()

    @staticmethod
    def displayLabsList(labList:list):
        table = []
        for lab in labList:
            table.append(lab.formatLabInfo().split("_"))
        print(tabulate(table, ["Lab", "Cost"], tablefmt="grid"))

    def formatLabInfo(self):
        formattedvalue = f"{self.__name}_{self.__cost:.2f}"
        return formattedvalue

    @classmethod
    def enterLaboratoryInfo(cls):
        labname = input("Enter Laboratory facility:\n")
        labcost = input("Enter Laboratory cost:\n")
        return cls(labname, labcost)

    @classmethod
    def readLaboratoriesFile(cls, filename:str):
        labList = []
        labFile = open(filename, 'r')
        for line in labFile:
            attribs = line.strip().split("_")
            assert (len(attribs) == 2)
            labList.append(cls(attribs[0], float(attribs[1]))
        file.close()
        return labList




class Management:
    __lists = {"doctor": [], "facility": [], "lab": [], "patient": []}
    __filenames = {"doctor": [], "facility": [], "lab": [], "patient": []}

    def __init__(self, filenames:dict):
        for key in filenames:
            self.__filenames[key] = filenames[key]
            if (key == "doctor"):
                self.__lists[key] = Doctor.readDoctorFile(filenames[key])
            elif (key == "facility"):
                self.__lists[key] = Facility.readFacilitiesFile(filenames[key])
            elif (key == "lab"):
                self.__lists[key] = Laboratory.readLabFile(filenames[key])
            elif (key == "patient"):
                self.__lists[key] = Patient.readPatientFile(filenames[key])
            else:
                assert (False)

    def mainmenu():
        menu = int(9)
        while (menu!=0):
            menu = int(input("Welcome to Alberta Hospital (AH) Managment system \n"
                             "Select from the following options, or select 0 to stop:\n"
                             "1 -   Doctors\n"
                             "2 -   Facilities\n"
                             "3 -   Laboratories\n"
                             "4 -   Patients\n\n"))
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

    def doc_menu(self):
        while (True):
            menu = int(input("\nDoctors Menu:\n"
                               "1 - Display Doctors list\n"
                               "2 - Search for doctor by ID\n"
                               "3 - Search for doctor by name\n"
                               "4 - Add doctor\n"
                               "5 - Edit doctor info\n"
                               "6 - Back to the Main Menu\n"
                               "> "))
            if (menu == 1):
                Doctor.displayDoctorsList(self.__lists["doctor"])
            elif (menu == 2):
                ID = int(input("Enter the doctor id: "))
                doc = Doctor.searchDoctorById(ID, self.__lists["doctor"])
                if (doc == None):
                    print("Can't find the doctor with the given ID in the system")
                else:
                    doc.displayDoctorInfo()
            elif (menu == 3):
                name = input("Enter the doctor name: ")
                doc = Doctor.searchDoctorByName(name, self.__list["doctor"])
                if (doc == None):
                    print("Can't find the doctor with the given name in the system")
                else:
                    doc.displayDoctorInfo()
            elif (menu == 4):
                self.__lists["doctor"].append(Doctor.enterDrInfo())
            elif (menu == 5):
                ID = int(input("Enter the id of the Doctor whose information you want to edit: "))
                Doctor.editDoctorInfo(ID, self.__lists["doctor"])
            elif(menu == 6):
                break
            else:
                print("Sorry, invalid option selected. Try again...")

            wait = input("\nPress return to continue...")
            print("Back to the previous menu\n")

    def fac_menu(self):
        while (True):
            menu = int(input("\nFacilities Menu:\n"
                               "1 - Display Facilities list\n"
                               "2 - Add facility\n"
                               "3 - Back to the main menu\n"))
            if (menu == 1):
                Facility.displayFacilities(self.__lists["facility"])
            elif (menu == 2):
                self.__lists["facility"].append(Facility.enterFacilityInfo())
            elif (menu == 3):
                break
            else:
                print("Sorry, invalid option selected. Try again...")

            wait = input("\nPress return to continue...")
            print("Back to the previous menu\n")

    def lab_menu(self):
        while (True):
            menu = int(input("\nLaboratories Menu:\n"
                               "1 - Display laboratories list\n"
                               "2 - Add laboratory\n"
                               "3 - Back to the main menu\n"))
            if (menu == 1):
                Laboratory.displayLabsList(self.__lists["lab"])
            elif (menu == 2):
                self.__lists["lab"].append(Laboratory.enterLabInfo())
            elif (menu == 3):
                break
            else:
                print("Sorry, invalid option selected. Try again...")

            wait = input("\nPress return to continue...")
            print("Back to the previous menu\n")

    def pat_menu(self):
        while (True):
            menu = int(input("\nPatients Menu:\n"
                               "1 - Display patients list\n"
                               "2 - Search for patient by ID\n"
                               "3 - Add patient\n"
                               "4 - Edit patient info\n"
                               "5 - Back to the main menu\n"))
            if (menu == 1):
                Patient.displayPatientsList(self.__lists["patient"])
            elif (menu == 2):
                pid = int(input("Enter the Patient ID: "))
                pat = Patient.searchPatientById(ID, self.__lists["patient"])
                if (pat == None):
                    print("Can't find patient with the given ID in the system")
                else:
                    pat.displayPatientInfo()
            elif (menu == 3):
                self.__lists["patient"].append(Patient.enterPatientInfo())
            elif (menu == 4):
                pid = int(input("Enter the Id of patient whose info you want to edit: "))
                Patient.editPatientInfo(pid, self.__lists["patient"])
            elif (menu == 5):
                break
            else:
                print("Sorry, invalid option selected. Try again...")

            wait = input("\nPress return to continue...")
            print("Back to the previous menu\n")


