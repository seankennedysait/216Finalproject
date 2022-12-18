#################################################################################################
# Main Alberta Health(AH) Management console program.
# Authors: (Sukhjinder Kahlon) (Sean Kennedy) (Micheal Liu)
# Last Modified: 17 Dec 2022
# Version : 1.0.2
#
# This is the main program for accessing the Alberta Health(AH) management system. It uses the 
# "ah" python module to do all its tasks and provides a console UI to interact with the system.
#################################################################################################

import ah

# Database Filenames
d_files = {"doctor": "dataFiles/doctors.txt", 
             "facility": "dataFiles/facilities.txt",
             "lab": "dataFiles/laboratories.txt",
             "patient": "dataFiles/patients.txt"}

if __name__ == "__main__":
    ah_Manager = ah.Management(d_files)
    ah_Manager.main_menu()
