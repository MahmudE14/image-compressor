# Image Compression Script

## Introduction
A Python script using the Pillow library to compress image files and delete the original images after compression. This script is designed to save storage space by automating the compression process and removing the uncompressed files. Easily configurable with command-line arguments for input and output folders, making it convenient for batch processing. Dependencies are managed with the provided requirements.txt file.


## Usage
The script takes input and output folder paths as optional command-line arguments. If the arguments are not provided, it defaults to using the paths specified in the script. If

## Dependencies Installation
Before running the script, make sure to install the required dependencies using the following command:

```bash
pip install Pillow
```

## Command-line Usage
```bash
python compress_images.py <input_folder> <output_folder>
```

If input and output folder locations are not provided, it defaults to `input_images` and `output_images` directory in the present directory where the script is located.

## Note
Compression quality is set to 85 by default. Feel free to change `compression_quality` value under `if __name__ == "__main__":` block.
