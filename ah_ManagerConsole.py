# Main Alberta Health(AH) Management console program.

import ah

# Database Filenames
d_files = {"doctor": "dataFiles/doctors.txt", 
             "facility": "dataFiles/facilities.txt",
             "lab": "dataFiles/laboratories.txt",
             "patient": "dataFiles/patients.txt"}

if __name__ == "__main__":
    ah_Manager = ah.Management(d_files)
    ah_Manager.mainmenu()
