class VitalSigns:
    def __init__(self, heart_rate: int, blood_pressure: str, temperature: float):
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.temperature = temperature

    def __str__(self):
        """Return formatted vital signs"""
        return f"HR: {self.heart_rate} bpm, BP: {self.blood_pressure}, Temp: {self.temperature}°C"