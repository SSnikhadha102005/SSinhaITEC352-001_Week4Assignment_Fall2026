# objects_class_Sketch.py
# Snikhadha Sinha
# 09/14/2026
# This module defines the Sketch class, which models a simple art sketch
# with attributes and methods demonstrating object-oriented programming.

class Sketch:
    def __init__(self, title, medium, duration_minutes):
        """
        Constructor initializes a new Sketch object.

        Parameters:
        title (str): Name of the sketch
        medium (str): Art medium used (e.g., pencil, watercolor, acrylic)
        duration_minutes (int): Time spent creating the sketch
        """
        self.title = title
        self.medium = medium.lower()  # normalize input for easier comparison
        self.duration_minutes = duration_minutes

    def describeSketch(self):
        """
        Returns a formatted description of the sketch.
        """
        return (f"'{self.title}' uses {self.medium} and took "
                f"{self.duration_minutes} minutes to complete.")

    def estimateDifficulty(self):
        """
        Estimates difficulty based on the medium used.
        Returns a string representing difficulty level.
        """
        if self.medium in ["pencil", "charcoal"]:
            return "Easy"
        elif self.medium in ["acrylic", "gouache"]:
            return "Medium"
        elif self.medium in ["oil", "oil paint"]:
            return "Hard"
        elif self.medium in [["watercolor", "ink"]:
            return "Very Hard"
        else:
            return "Unknown Difficulty"

    def isLongProject(self):
        """
        Determines whether the sketch took a long time to complete.
        Returns True if duration exceeds 60 minutes.
        """
        return self.duration_minutes > 60
