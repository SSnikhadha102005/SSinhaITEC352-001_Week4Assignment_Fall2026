# main.py
# This script demonstrates the functionality of the Sketch class
# by creating multiple Sketch objects and displaying their details.
# Snikhadha Sinha
# 09/14/2026

from objects_class_Sketch import Sketch

d # Create several Sketch objects with different mediums and durations
    sketch1 = Sketch("Sunset Glow", "Watercolor", 45)
    sketch2 = Sketch("City Lines", "Pencil", 20)
    sketch3 = Sketch("Forest Depth", "Acrylic", 120)
    sketch4 = Sketch("Portrait Study", "Oil Paint", 180)

    # Loop through each sketch and display its information
    for s in [sketch1, sketch2, sketch3, sketch4]:
        print(s.describeSketch())            # Print description
        print("Difficulty:", s.estimateDifficulty())  # Print difficulty
        print("Long Project:", s.isLongProject())     # Print long project status
        print()  # Blank line for readability
if __name__ == "__main__":
    main()
