#CPRG216 Project Classes: Patient
#Michael Liu
#ID: 900310
#Dec 16th, 2022
#Version 3
######################################################


class Patient:
    def __init__(self, pid, name, disease, gender, age):            #Initializing Function 
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
    
    def __str__(self):                                                                             #Converts class to string
        string = str(f"{self.pid},{self.name},{self.disease},{self.gender},{self.age}")
        return string

    
    def readPatientsFile():                                                     #Opens patient.txt and converts it into a list
        patientList = []
        openFile = open("patients.txt","r")
        patientFile = openFile.readlines()
        for x in patientFile:
            patientList.append(x.strip().split("_"))                                #strips and turns _ into commas/its own element
        openFile.close()
        return patientList                                                      #returns a list of patients
    
    @classmethod
    def enterPatientInfo(self):                                                 #asks user to enter new user
        self.pid = str(input("Please enter Patient ID:\n"))
        self.name = str(input("Please enter Patient name:\n"))
        self.disease = str(input("Please enter Patient disease:\n"))
        self.gender = str(input("Please enter Patient gender:\n"))
        self.age = str(input("Please enter Patient age:\n"))
        return self(self.pid, self.name, self.disease, self.gender, self.age)       #returns a class

    @classmethod
    def formatPatientInfo(self):                                            #converts user input from enterPatientInfo() into a string
        patientData = Patient.enterPatientInfo()
        patientData = patientData.__str__()
        patientData = patientData.replace(",","_")                          #converts commas into _ to enter back into patients.txt file
        return patientData

    def displayPatientInfo(self):                                                   #displays user class
        print(f"ID: {self.pid}\n Name: {self.name}\n Disease: {self.disease}\n Gender: {self.gender}\n Age: {self.age}")


    def displayPatientList():                                                       #displays a table of patients currently saved in patients.txt
        patientList = Patient.readPatientsFile()
        for x in range(len(patientList)):
            print(f'\t    '.join(patientList[x]))                                     #formats into a table
        
        return

    def searchPatientByID():                                                        #searches patient by ID
        y = bool(0)                                
        patientID = str(input("Enter the Patients ID: "))
        patientList = Patient.readPatientsFile()                                    #opens list of patients
        for x in range(len(patientList)):
            if patientList[x][0] == patientID:                                      #looks for patient ID
                print(f'\t    '.join(patientList[0]))                               #prints the headers 
                print(f'\t    '.join(patientList[x],))                              #prints the searched ID
                y = bool(1)                            
        if y == bool(0):
            print("Can't Find the Patient with the same ID on the system\n")
        return
 

    def editPatientInfo():                                                                          #edits patient info based on entered ID
        patientID = str(input("Enter the ID of the Patient you want to edit their information: "))          #asks user for patient ID and new info                                             
        newName = str(input("Enter new Name: "))
        newDisease = str(input("Enter new Disease: "))
        newGender = str(input("Enter new Gender: "))
        newAge = str(input("Enter new Age: "))

        file = open("patients.txt","r")
        newFile = file.readlines()                                              #opens and saves patient file
        for x in range(len(newFile)):    
            if newFile[x].startswith(patientID):                                        #if patient file starts with ID entered
                patient = Patient(patientID,newName,newDisease,newGender,newAge)
                patient = patient.__str__()
                patient = patient.replace(",","_") + "\n"                               #format new info and replace
                newFile[x] = patient

        file = open("patients.txt", "w")
        file.writelines(newFile)                                                       #saves new patient file
        file.close()
        return 

    def addPatientToFile():                                                             #adds new patient into the file, formats first
        patientInfo = Patient.formatPatientInfo()
        file = open("patients.txt","a")
        file.write("\n")
        file.write(patientInfo)
        file.close()
        return

    def writeListOfPatientsToFile():                                                        #asks user how many patients and repeats add patient that many times
        numOfEntries = int(input("Enter how many patients you would like to add: "))
        for x in range(numOfEntries):
            Patient.addPatientToFile()
        return


choice = -1
while choice != 0:
    choice = int(input(f"Doctors Menu:\n"                                           #If statements for menu selections
        "1 - Display Patients List\n"
        "2 - Search for Patient by ID\n"
        "3 - Add Patient\n"
        "4 - Edit Patient info\n"
        "5 - Back to the Main Menu\n"))

    if choice == 1:
        Patient.displayPatientList()
        exit
    if choice == 2:
        Patient.searchPatientByID()
        exit
    if choice == 3:
        Patient.addPatientToFile()
        exit
    if choice == 4:
        Patient.editPatientInfo()
        exit
    if choice == 5:
        choice = 0
        exit
    print("Back to the previous menu\n")


