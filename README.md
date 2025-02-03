# PRODIGY_CS_02
#Overview
This project is a simple image encryption tool that utilizes pixel manipulation techniques to encrypt and decrypt images. The tool allows users to perform operations such as swapping pixel values and applying basic mathematical operations to each pixel. The goal is to provide a straightforward way to understand image encryption concepts through hands-on experience.

##Features
Encrypt images using pixel manipulation techniques.
Decrypt images back to their original form.
Support for basic operations like pixel value swapping and mathematical transformations.
User-friendly command-line interface.

##Requirements
To run this project, you will need:

Python 3.x
Required libraries:
Pillow for image processing
numpy for numerical operations (optional, depending on implementation)
You can install the required libraries using pip:

bash

Verify
Run
Copy code
pip install Pillow numpy

##Installation
Clone the repository:

bash

Verify
Run
Copy code
git clone https://github.com/yourusername/image-encryption-tool.git
cd image-encryption-tool
Install the required libraries (if not already installed):

bash

Verify
Run
Copy code
pip install -r requirements.txt
Usage
Encrypting an Image
To encrypt an image, run the following command:

bash

Verify
Run
Copy code
python encrypt.py <input_image_path> <output_image_path>
<input_image_path>: Path to the image you want to encrypt.
<output_image_path>: Path where the encrypted image will be saved.
Decrypting an Image
To decrypt an image, run the following command:

bash

Verify
Run
Copy code
python decrypt.py <input_image_path> <output_image_path>
<input_image_path>: Path to the encrypted image.
<output_image_path>: Path where the decrypted image will be saved.
Example
bash

Verify
Run
Copy code
python encrypt.py input.jpg encrypted.png
python decrypt.py encrypted.png decrypted.jpg
Implementation Details
Encryption Process
Load the Image: Use the Pillow library to load the image.
Pixel Manipulation:
Swap pixel values: Randomly select pairs of pixels and swap their values.
Apply mathematical operations: For example, add a constant value to each pixel's RGB values.
Save the Encrypted Image: Save the manipulated pixel data back to an image file.
Decryption Process
Load the Encrypted Image: Use the Pillow library to load the encrypted image.
Reverse Pixel Manipulation:
Reverse the swapping of pixel values.
Apply the inverse of the mathematical operations used during encryption.
Save the Decrypted Image: Save the restored pixel data back to an image file.

For any questions or feedback, please reach out to [vaishnavii540@gmail.com].



