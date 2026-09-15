# objects_class_Sketch.py
# Snikhadha Sinha
# 09/14/2026

class Sketch:
    def __init__(self, title, medium, duration_minutes):
        self.title = title
        self.medium = medium
        self.duration_minutes = duration_minutes

    def describeSketch(self):
        return f"'{self.title}' is created using {self.medium} and took {self.duration_minutes} minutes."

    def estimateDifficulty(self):
        if self.duration_minutes < 30:
            return "Easy"
        elif self.duration_minutes <= 90:
            return "Medium"
        else:
            return "Hard"
