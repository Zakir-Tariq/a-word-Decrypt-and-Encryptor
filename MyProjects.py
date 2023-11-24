from cryptography.fernet import Fernet

# Encryption key
encryption_key = "HTte_y2T_GHFYlKohPIe9-6g9H87iZ2XdZKig0x-NlQ="
cipher_suite = Fernet(encryption_key.encode())

# Function to encrypt a value
def encrypt(value):
    return cipher_suite.encrypt(value.encode())

# Function to decrypt a value
def decrypt(encrypted_value):
    return cipher_suite.decrypt(encrypted_value).decode()

# Function to handle decryption attempts
def decrypt_with_attempts(encrypted_values):
    attempts = 3
    while attempts > 0:
        key = input("Enter the decryption key: ")
        cipher_suite_attempt = Fernet(key.encode())
        
        try:
            # Attempt to decrypt values
            decrypted_values = [decrypt(value) for value in encrypted_values]
            
            # Write decrypted values to a file
            with open("decrypted_values.txt", "w") as decrypted_file:
                for decrypted_value in decrypted_values:
                    decrypted_file.write(f"{decrypted_value}\n")

            print("Decryption successful. Decrypted values written to 'decrypted_values.txt'")
            break
        except:
            attempts -= 1
            print(f"Invalid decryption key. {attempts} attempts remaining.")

# Main program
def main():
    # List to store encrypted values
    encrypted_values = []

    while True:
        # User input for the word
        word = input("Enter a word to encrypt (or type 'exit' to quit): ")

        if word.lower() == 'exit':
            break

        # Encrypt the word and append to the list
        encrypted_word = encrypt(word)
        encrypted_values.append(encrypted_word)

        print("Word encrypted and added to the list.")

    # Ask the user if they want to decrypt
    decrypt_option = input("Do you want to decrypt? (yes/no): ").lower()

    if decrypt_option == 'yes':
        # Attempt to decrypt with a limit of 3 attempts
        decrypt_with_attempts(encrypted_values)

if __name__ == "__main__":
    main()