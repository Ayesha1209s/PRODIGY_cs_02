from PIL import Image
import os

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()
    width, height = img.size

    for x in range(width):#XOR operation
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)
    print(f"[+] Encrypted image saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    encrypt_image(image_path, key, output_path)

def main():
    print("Image Encryption & Decryption Tool *Using Pixel Manipulation*")
    choice = input("Enter E = Encrypt or D = Decrypt: ").strip().lower()

    image_path = input("Enter the path to the image: ").strip()
    key = int(input("Enter numeric key bteween (0–255): "))

    if key < 0 or key > 255:
        print("Key must be between (0-255)")
        return

    if not os.path.exists(image_path):
        print("Image path not found,please check!")
        return

    if choice == 'e':
        output_path = input("Enter the encrypted image output path: ").strip()
        encrypt_image(image_path, key, output_path)
    elif choice == 'd':
        output_path = input("Enter the decrypted image output path: ").strip()
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()
