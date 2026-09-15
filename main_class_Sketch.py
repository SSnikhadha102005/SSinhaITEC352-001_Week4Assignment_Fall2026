# main.py
# Snikhadha Sinha
# 09/14/2026

from objects_class_Sketch import Sketch

def main():
    # Create objects
    sketch1 = Sketch("Sunset Glow", "Watercolors", 45)
    sketch2 = Sketch("City Lines", "Pencil", 20)
    sketch3 = Sketch("Forest Depth", "Acrylic", 120)

    # Demonstrate functionality
    print(sketch1.describeSketch())
    print("Difficulty:", sketch1.estimateDifficulty())
    print()

    print(sketch2.describeSketch())
    print("Difficulty:", sketch2.estimateDifficulty())
    print()

    print(sketch3.describeSketch())
    print("Difficulty:", sketch3.estimateDifficulty())

if __name__ == "__main__":
    main()
