class ReportGeneration:
    @staticmethod
    def patient_report(patient):
        """Generate a report for a single patient"""
        lines = [str(patient)]
        if not patient.history:
            lines.append("No vitals recorded.")
        else:
            for idx, vitals in enumerate(patient.history, start=1):
                lines.append(f"{idx}. {vitals}")
        return "\n".join(lines)

    @staticmethod
    def system_report(patients):
        """Generate summary report for all patients"""
        total_patients = len(patients)
        num_records = 0
        sum_hr = 0
        sum_temp = 0.0
        # Skip BP averaging due to string format
        for patient in patients:
            for vitals in getattr(patient, "history", []):
                num_records += 1
                sum_hr += getattr(vitals, "heart_rate", 0)
                sum_temp += getattr(vitals, "temperature", 0.0)
        avg_hr = (sum_hr / num_records) if num_records else 0
        avg_temp = (sum_temp / num_records) if num_records else 0.0
        return (
            f"Total Patients: {total_patients}\n"
            f"Total Vital Records: {num_records}\n"
            f"Average Heart Rate: {avg_hr:.1f} bpm\n"
            f"Average Temperature: {avg_temp:.1f}°C"
        )
