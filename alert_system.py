
class AlertSystem:
    def __init__(self):
        self.alerts = [] 

    def raise_alert(self, patient_id, message):
        """Store alert for a patient"""
        self.alerts.append((patient_id, message))

    def get_alerts(self):
        """Return all alerts"""
        return self.alerts

    def clear_alerts(self):
        """Clear stored alerts"""
        self.alerts.clear()


