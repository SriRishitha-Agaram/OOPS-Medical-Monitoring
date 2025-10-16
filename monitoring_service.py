
class MonitoringService:
    def __init__(self):

        self.thresholds = {
            "heart_rate": (60, 100),
            "blood_pressure": (90, 140),
            "temperature": (36.1, 37.8)
        }

    def check_vitals(self, patient_id, vitals):
        """Check vitals and return list of alerts if abnormal"""
        alerts = []

        if not (self.thresholds["heart_rate"][0] <= vitals.heart_rate <= self.thresholds["heart_rate"][1]):
            alerts.append(f"⚠️ Abnormal heart rate ({vitals.heart_rate} bpm) for Patient {patient_id}")

        if not (self.thresholds["blood_pressure"][0] <= vitals.blood_pressure <= self.thresholds["blood_pressure"][1]):
            alerts.append(f"⚠️ Abnormal blood pressure ({vitals.blood_pressure} mmHg) for Patient {patient_id}")

        if not (self.thresholds["temperature"][0] <= vitals.temperature <= self.thresholds["temperature"][1]):
            alerts.append(f"⚠️ Abnormal temperature ({vitals.temperature}°C) for Patient {patient_id}")

        return alerts

