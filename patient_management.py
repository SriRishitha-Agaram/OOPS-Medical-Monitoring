class Patient:
    def __init__(self, patient_id: str, name: str, age: int, gender: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.history = [] 

    def add_vital_record(self, vitals):
        """Add a vital sign record to history"""
        self.history.append(vitals)

    def __str__(self):
        """Readable representation of patient"""
        return f"{self.patient_id} - {self.name} ({self.age}, {self.gender})"


class PatientManagement:
    def __init__(self):
        self.patients = {}  

    def add_patient(self, patient: Patient):
        """Register a new patient"""
        if patient.patient_id in self.patients:
            print(f"Patient ID {patient.patient_id} already exists!")
        else:
            self.patients[patient.patient_id] = patient
            print(f"Patient {patient.name} added successfully.")

    def update_patient(self, patient_id: str, **kwargs):
        """Update existing patient details"""
        if patient_id not in self.patients:
            print("Patient not found!")
            return
        patient = self.patients[patient_id]
        for key, value in kwargs.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
        print(f"Patient {patient_id} updated successfully.")

    def list_patients(self):
        """Display all patients"""
        if not self.patients:
            print("No patients available.")
        else:
            print("\nList of Patients:")
            for patient in self.patients.values():
                print(patient)
