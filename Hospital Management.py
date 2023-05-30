# This program uses 5 classes to create doctor and patient information, as well as management
# Both doctor and patient management allow both viewing and altering stored information
# The main management class acts as a selection menu for the user
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
#
# Begin Doctor class properties and methods

class Doctor:
    # constructor
    def __init__(self, id, name, specialization, times, qualifications, room):
        self.__id = id
        self.__name = name
        self.__specialization = specialization
        self.__times = times
        self.__qualifications = qualifications
        self.__room = room
    
    # accessors
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_specialization(self):
        return self.__specialization
    
    def get_times(self):
        return self.__times
    
    def get_qualifications(self):
        return self.__qualifications
    
    def get_room(self):
        return self.__room

    # mutators
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name
    
    def set_specialization(self, specialization):
        self.__specialization = specialization
    
    def set_times(self, times):
        self.__times = times
    
    def set_qualifications(self, qualifications):
        self.__qualifications = qualifications
    
    def set_room(self, room):
        self.__room = room



class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    # Turns formatted, hidden information into a string
    def format_dr_info(self, doctor):
        return f'{doctor.get_id()}_{doctor.get_name()}_{doctor.get_specialization()}_{doctor.get_times()}_{doctor.get_qualifications()}_{doctor.get_room()}'

    # Returns appropriately formatted information for use as a variable
    def enter_dr_info(self):
        id = input('\nEnter doctor ID: ')
        name = input('Enter doctor name: ')
        specialization = input('Enter doctor specialization: ')
        times = input('Enter doctor times (e.g., 7am-10pm): ')
        qualifications = input('Enter doctor qualifications: ')
        room = input('Enter doctor room number: ')
        return Doctor(id, name, specialization, times, qualifications, room)

    # Takes data out of the doctors.txt file and creates a list
    def read_doctors_file(self):
        with open('Project Data/doctors.txt') as file_content:
            # Skips over first line, which declares categories, in favor of better formatting
            next(file_content)
            for line in file_content:
                doctor_fields = line.strip('\n').split('_')
                doctor = Doctor(doctor_fields[0], doctor_fields[1], doctor_fields[2], doctor_fields[3], doctor_fields[4], doctor_fields[5])
                self.doctors.append(doctor)

    # Displays found doctor using a legible formatting
    def search_doctor_by_id(self):
        found = False
        id = input('\nEnter the doctor\'s ID: ')
        for doctor in self.doctors:
            if doctor.get_id() == id:
                found = True
                print('{:<5}{:<30}{:<15}{:<15}{:<15}{}'.format('ID', 'Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'))
                self.display_doctor_info(doctor)
                break
        if not found:
            print('Can\'t find the doctor with the same ID on the system')

    # Formats names during searches to remove any doctor references, making it function with either simply their name or including their title
    def format_name(self, name):
        name = name.lower()
        return name.replace('dr. ', '').replace('dr.', '')

    # Displays found doctor using a legible formatting
    # Since more than one doctor can have the same name, compared to ID numbers, will search entire list and will only print list title once
    def search_doctor_by_name(self):
        found = False
        name = input('\nEnter the doctor\'s name: ')
        formatted_name = self.format_name(name)
        for doctor in self.doctors:
            once = False
            if self.format_name(doctor.get_name()) == formatted_name:
                found = True
                # Creates title of table only once
                if not once:
                    once = True
                    print('{:<5}{:<30}{:<15}{:<15}{:<15}{}'.format('ID', 'Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'))
                    self.display_doctor_info(doctor)
        if not found:
            print('Can\'t find the doctor with the same name on the system')

    # Displays found doctor using a legible formatting
    def display_doctor_info(self, doctor):
        print('-' * 90)
        print('{:<5}{:<30}{:<15}{:<15}{:<15}{}'.format(doctor.get_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_times(), doctor.get_qualifications(), doctor.get_room()))

    # Functions similar to search_doctor_by_id, but instead asks user for new inputs, excluding ID, if it is found
    def edit_doctor_info(self):
        found = False
        id = input('\nEnter the doctor\'s ID: ')
        for doctor in self.doctors:
            if doctor.get_id() == id:
                found = True
                doctor.set_name(input('Enter new name: '))
                doctor.set_specialization(input('Enter new specialization: '))
                doctor.set_times(input('Enter new times (e.g., 7am-10pm): '))
                doctor.set_qualifications(input('Enter new qualifications: '))
                doctor.set_room(input('Enter new room number: '))
                self.write_list_of_doctors_to_file()
                print(f'\nDoctor whose ID is {id} has been edited')
                break
        if not found:
            print('Can\'t find the doctor with the same ID on the system')

    # Displays doctor list using a legible formatting
    def display_doctors_list(self):
        print('{:<5}{:<30}{:<15}{:<15}{:<15}{}'.format('Id', 'Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'))
        print('-' * 90)
        for doctor in self.doctors:
            print('{:<5}{:<30}{:<15}{:<15}{:<15}{}'.format(doctor.get_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_times(), doctor.get_qualifications(), doctor.get_room()))
            print('-' * 90)

    # Overwrites the source document doctors.txt with whatever information has been added/edited/changed in this program
    def write_list_of_doctors_to_file(self):
        with open('Project Data/doctors.txt', 'w') as file_content:
            file_content.write('id_name_specilist_timing_qualification_roomNb\n')
            for line in self.doctors:
                file_content.write(self.format_dr_info(line) + '\n')

    # Appends to the source document doctors.txt with a new addition with all relevant information
    def add_dr_to_file(self):
        doctor = self.enter_dr_info()
        self.doctors.append(doctor)
        print(f'\nDoctor whose ID is {doctor.get_id()} has been added')
        with open('Project Data/doctors.txt', 'a') as file_content:
            file_content.write(self.format_dr_info(doctor) + '\n')
        # print(f'The following information has been added to the file:\n' + self.format_dr_info(doctor))

# End Doctor class properties and methods
# 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# 
# Begin Patient class properties and methods


class Patient:
    # constructor
    def __init__(self, id, name, disease, gender, age):
        self.__id = id
        self.__name = name
        self.__disease = disease
        self.__gender = gender
        self.__age = age

    # accessors
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_disease(self):
        return self.__disease
    
    def get_gender(self):
        return self.__gender
    
    def get_age(self):
        return self.__age

    # mutators
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name
    
    def set_disease(self, disease):
        self.__disease = disease
    
    def set_gender(self, gender):
        self.__gender = gender
    
    def set_age(self, age):
        self.__age = age



class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    # Turns formatted, hidden information into a string
    def format_patient_info_for_file(self, patient):
        return f'{patient.get_id()}_{patient.get_name()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}'

    # Returns appropriately formatted information for use as a variable
    def enter_patient_info(self):
        id = input('\nEnter patient ID: ')
        name = input('Enter patient name: ')
        disease = input('Enter patient disease: ')
        gender = input('Enter patient gender: ')
        age = input('Enter patient age: ')
        return Patient(id, name, disease, gender, age)

    # Takes data out of the patients.txt file and creates a list
    def read_patients_file(self):
        with open('Project Data/patients.txt') as file_content:
            # Skips over first line, which declares categories, in favor of better formatting
            next(file_content)
            for line in file_content:
                patient_fields = line.strip('\n').split('_')
                patient = Patient(patient_fields[0], patient_fields[1], patient_fields[2], patient_fields[3], patient_fields[4])
                self.patients.append(patient)

    # Displays found patient using a legible formatting
    def search_patient_by_id(self):
        found = False
        id = input('\nEnter the patient\'s ID: ')
        for patient in self.patients:
            if patient.get_id() == id:
                found = True
                print('{:<5}{:<30}{:<20}{:<10}{}'.format('ID', 'Name', 'Disease', 'Gender', 'Age'))
                self.display_patient_info(patient)
                break
        if not found:
            print('Can\'t find the patient with the same ID on the system')

    # Displays found patient using a legible formatting
    def display_patient_info(self, patient):
        print('-' * 70)
        print('{:<5}{:<30}{:<20}{:<10}{}'.format(patient.get_id(), patient.get_name(), patient.get_disease(), patient.get_gender(), patient.get_age()))

    # Functions similar to search_patient_by_id, but instead asks user for new inputs, excluding ID, if it is found
    def edit_patient_info_by_id(self):
        found = False
        id = input('\nEnter the patient\'s ID: ')
        for patient in self.patients:
            if patient.get_id() == id:
                found = True
                patient.set_name(input('Enter new name: '))
                patient.set_disease(input('Enter new disease: '))
                patient.set_gender(input('Enter new gender: '))
                patient.set_age(input('Enter new age: '))
                self.write_list_of_patients_to_file()
                print(f'\nPatient whose ID is {id} has been edited')
                break
        if not found:
            print('Can\'t find the patient with the same ID on the system')

    # Displays patient list using a legible formatting
    def display_patients_list(self):
        print('{:<5}{:<30}{:<20}{:<10}{}'.format('ID', 'Name', 'Disease', 'Gender', 'Age'))
        print('-' * 70)
        for patient in self.patients:
            print('{:<5}{:<30}{:<20}{:<10}{}'.format(patient.get_id(), patient.get_name(), patient.get_disease(), patient.get_gender(), patient.get_age()))
            print('-' * 70)

    # Overwrites the source document patients.txt with whatever information has been added/edited/changed in this program
    def write_list_of_patients_to_file(self):
        with open('Project Data/patients.txt', 'w') as file_content:
            file_content.write('id_Name_Disease_Gender_Age\n')
            for line in self.patients:
                file_content.write(self.format_patient_info_for_file(line) + '\n')

    # Appends to the source document patients.txt with a new addition with all relevant information
    def add_patient_to_file(self):
        patient = self.enter_patient_info()
        self.patients.append(patient)
        print(f'\nPatient whose ID is {patient.get_id()} has been added')
        with open('Project Data/patients.txt', 'a') as file_content:
            file_content.write(self.format_patient_info_for_file(patient) + '\n')
        # print(f'The following information has been added to the file:\n' + self.format_patient_info_for_file(patient))

# End Patient class properties and methods
# 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# 
# Begin Managment class properties and methods

class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()
        self.__display_menu()

    def __display_menu(self):
        option = 0
        while (option != 3):
            print('\nWelcome to Alberta Hospital (AH) Management system')
            print('Select from the following options or select 3 to stop:')
            print('1 - \t Doctors')
            print('2 - \t Patients')
            print('3 - Exit Program')
            option = int(input('>>> '))
            if option == 1:
                option = 0
                while (option != 6):
                    print('\nDoctors Menu:')
                    print('1 - Display list of doctors')
                    print('2 - Search for doctor by ID')
                    print('3 - Search for doctor by name')
                    print('4 - Add doctor')
                    print('5 - Edit doctor info')
                    print('6 - Back to the Main Menu')
                    option = input('>>> ')
                    match option:
                        case '1':
                            self.doctor_manager.display_doctors_list()
                        case '2':
                            self.doctor_manager.search_doctor_by_id()
                        case '3':
                            self.doctor_manager.search_doctor_by_name()
                        case '4':
                            self.doctor_manager.add_dr_to_file()
                        case '5':
                            self.doctor_manager.edit_doctor_info()
                        case '6':
                            break
                        case _:
                            print('Invalid option, please try again \n')
            elif option == 2:
                option = 0
                while (option != 5):
                    print('\nPatients Menu:')
                    print('1 - Display patients list')
                    print('2 - Search for patient by ID')
                    print('3 - Add patient')
                    print('4 - Edit patient info')
                    print('5 - Back to the Main Menu')
                    option = input('>>> ')
                    match option:
                        case '1':
                            self.patient_manager.display_patients_list()
                        case '2':
                            self.patient_manager.search_patient_by_id()
                        case '3':
                            self.patient_manager.add_patient_to_file()
                        case '4':
                            self.patient_manager.edit_patient_info_by_id()
                        case '5':
                            break
                        case _:
                            print('Invalid option, please try again \n')
            elif option == 3:
                print('Thanks for using the program. Bye!')
                break
            else:
                print('Invalid option, please try again \n')

# End class definitions
# 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# 
# Program initialization

Management()
