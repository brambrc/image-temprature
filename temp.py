from PIL import Image, ImageEnhance
import sys
import os

def is_jpeg(filename):
    # Check the file extension and return True if it's a JPEG
    file_ext = os.path.splitext(filename)[1].lower()
    return file_ext in ['.jpg', '.jpeg']

def adjust_temperature(image_path, output_path, temp_value):
    try:
        # Check if both input and output files are JPEGs
        if not is_jpeg(image_path):
            raise ValueError("Input file must be a JPEG image.")
        if not is_jpeg(output_path):
            raise ValueError("Output file must be a JPEG image.")

        # Open an image file
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Apply color balance enhancement
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1 + temp_value / 100)

            # Save the modified image
            img.save(output_path, 'JPEG')
            print(f"Image successfully saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Get input parameters from the command line
if len(sys.argv) != 4:
    print("Usage: python script.py input_path output_path temperature_value")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]
try:
    temperature_value = float(sys.argv[3])  # Expecting a float value
except ValueError:
    print("Temperature value must be a number.")
    sys.exit(1)

# Call the function
adjust_temperature(input_path, output_path, temperature_value)
