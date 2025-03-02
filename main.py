from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    encrypted_array = (img_array + key) % 256  # Apply pixel transformation
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    decrypted_array = (img_array - key) % 256  # Reverse pixel transformation
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    while True:
        print("\nImage Encryption Tool")
        choice = input("Do you want to encrypt or decrypt an image? (e/d): ").strip().lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        
        image_path = input("Enter the image file path: ").strip()
        try:
            key = int(input("Enter an encryption key (integer): "))
        except ValueError:
            print("Invalid key. Please enter an integer.")
            continue
        
        output_path = input("Enter the output file path: ").strip()
        
        if choice == 'e':
            encrypt_image(image_path, key, output_path)
        else:
            decrypt_image(image_path, key, output_path)
        
        another = input("Do you want to process another image? (y/n): ").strip().lower()
        if another != 'y':
            print("Goodbye!")
            break
