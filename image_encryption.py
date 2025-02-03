from PIL import image

def encrypt_image(image_path):
    """
    Encrypts an image by swapping the pixel values of each pair of pixels.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The path to the encrypted image file.
    """

    # Open the image
    with Image.open(image_path) as image:
        # Get the pixel data
        pixels = image.load()

        # Get the image dimensions
        width, height = image.size

        # Swap the pixel values of each pair of pixels
        for x in range(0, width, 2):
            for y in range(0, height, 2):
                # Get the pixel values
                pixel1 = pixels[x, y]
                pixel2 = pixels[x + 1, y]
                pixel3 = pixels[x, y + 1]
                pixel4 = pixels[x + 1, y + 1]

                # Swap the pixel values
                pixels[x, y] = pixel2
                pixels[x + 1, y] = pixel1
                pixels[x, y + 1] = pixel4
                pixels[x + 1, y + 1] = pixel3

        # Save the encrypted image
        encrypted_image_path = "encrypted_" + image_path
        image.save(encrypted_image_path)

    return encrypted_image_path

def decrypt_image(image_path):
    """
    Decrypts an image by swapping the pixel values of each pair of pixels.

    Args:
        image_path (str): The path to the encrypted image file.

    Returns:
        str: The path to the decrypted image file.
    """

    # Open the image
    with Image.open(image_path) as image:
        # Get the pixel data
        pixels = image.load()

        # Get the image dimensions
        width, height = image.size

        # Swap the pixel values of each pair of pixels
        for x in range(0, width, 2):
            for y in range(0, height, 2):
                # Get the pixel values
                pixel1 = pixels[x, y]
                pixel2 = pixels[x + 1, y]
                pixel3 = pixels[x, y + 1]
                pixel4 = pixels[x + 1, y + 1]

                # Swap the pixel values
                pixels[x, y] = pixel2
                pixels[x + 1, y] = pixel1
                pixels[x, y + 1] = pixel4
                pixels[x + 1, y + 1] = pixel3

        # Save the decrypted image
        decrypted_image_path = "decrypted_" + image_path
        image.save(decrypted_image_path)

    return decrypted_image_path

def main():
    while True:
        print("\nImage Encryption Tool")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            image_path = input("Enter the path to the image file: ")
            encrypted_image_path = encrypt_image(image_path)
            print(f"Encrypted image saved to {encrypted_image_path}")

        elif choice == '2':
            image_path = input("Enter the path to the encrypted image file: ")
            decrypted_image_path = decrypt_image(image_path)
            print(f"Decrypted image saved to {decrypted_image_path}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

