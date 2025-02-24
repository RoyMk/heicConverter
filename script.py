import os
from PIL import Image
from pillow_heif import register_heif_opener

def convert_heic(input_folder, output_folder, output_format='jpg'):
    # Register the HEIF opener
    register_heif_opener()

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.heic'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + f'.{output_format}')

            # Open the HEIC image and convert to RGB
            with Image.open(input_path) as img:
                img = img.convert('RGB')
                # Save as specified format
                img.save(output_path, output_format.upper())

            print(f"Converted {filename} to {output_format.upper()}")

# Example usage
input_folder = input("Input folder: ").strip('"')
output_format = input("Output format (jpg, png, bmp, etc.): ").lower()
output_folder = os.path.join(input_folder, f"converted_{output_format}")

convert_heic(input_folder, output_folder, output_format)
