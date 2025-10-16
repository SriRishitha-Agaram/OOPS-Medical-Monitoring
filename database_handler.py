class DatabaseHandler:
    def __init__(self):
        self.data = {}  # dictionary {patient_id: Patient object}

    def save_patient(self, patient):
        """Save or update patient in storage"""
        self.data[patient.patient_id] = patient
        return patient

    def get_patient(self, patient_id: str):
        """Retrieve patient by ID"""
        return self.data.get(patient_id)

    def list_all_patients(self):
        """Return all patients"""
        return list(self.data.values())
