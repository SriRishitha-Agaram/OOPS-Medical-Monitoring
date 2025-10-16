from patient_management import Patient, PatientManagement
from vital_signs import VitalSigns
from monitoring_service import MonitoringService
from alert_system import AlertSystem
from report_generation import ReportGeneration
from database_handler import DatabaseHandler

def main():
    db = DatabaseHandler()
    patient_manager = PatientManagement()
    monitor = MonitoringService()
    alerts = AlertSystem()

    while True:
        print("\n--- Medical Monitoring System ---")
        print("1. Add Patient")
        print("2. List Patients")
        print("3. Record Vital Signs")
        print("4. View Patient Report")
        print("5. View System Report")
        print("6. View Alerts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            try:
                pid = input("Patient ID: ").strip()
                name = input("Name: ").strip()
                age = int(input("Age: ").strip())
                gender = input("Gender: ").strip()
                patient = Patient(pid, name, age, gender)
                patient_manager.add_patient(patient)
                db.save_patient(patient)
                print("Patient added.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            patients = patient_manager.list_patients()
            if not patients:
                print("No patients found.")
            else:
                for p in patients:
                    print(p)

        elif choice == "3":
            pid = input("Patient ID: ").strip()
            patient = db.get_patient(pid)
            if not patient:
                print("Patient not found.")
                continue
            try:
                hr = int(input("Heart Rate (bpm): ").strip())
                bp = input("Blood Pressure (e.g., 120/80): ").strip()
                temp = float(input("Temperature (°C): ").strip())
                vitals = VitalSigns(hr, bp, temp)
                patient.add_vital_record(vitals)
                db.save_patient(patient)
                triggered = monitor.check_vitals(vitals)
                for msg in triggered:
                    alerts.raise_alert(pid, msg)
                if triggered:
                    print("Alerts:", ", ".join(triggered))
                else:
                    print("Vitals recorded. No alerts.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            pid = input("Patient ID: ").strip()
            patient = db.get_patient(pid)
            if not patient:
                print("Patient not found.")
            else:
                print(ReportGeneration.patient_report(patient))

        elif choice == "5":
            print(ReportGeneration.system_report(db.list_all_patients()))

        elif choice == "6":
            all_alerts = alerts.get_alerts()
            if not all_alerts:
                print("No alerts.")
            else:
                for pid, msg in all_alerts:
                    print(f"{pid}: {msg}")
            clr = input("Clear alerts? (y/N): ").strip().lower()
            if clr == "y":
                alerts.clear_alerts()
                print("Alerts cleared.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
