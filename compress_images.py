from PIL import Image
import os
import sys

# List of supported image file extensions
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']

def is_image(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() in IMAGE_EXTENSIONS

def compress_images(input_folder, output_folder, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        if os.path.isfile(input_path) and is_image(input_path):
            with Image.open(input_path) as img:
                img.save(output_path, quality=quality)

            # Delete the original image file
            os.remove(input_path)



if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"

    # Check if input and output folder paths are provided as command-line arguments
    if len(sys.argv) > 2:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
    else:
        print("Usage: python compress_images.py <input_folder> <output_folder>")
        sys.exit(1)

    compression_quality = 85  # Adjust this value as needed (0-100)

    compress_images(input_folder, output_folder, quality=compression_quality)
    print("Image compression completed.")
