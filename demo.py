import os
import hashlib

def insecure_file_read(file_path):
    # Security Hotspot: Insecure file access
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def weak_hashing(password):
    # Security Hotspot: Using a weak hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()

def insecure_input():
    # Security Hotspot: Unsanitized user input
    user_input = input("Enter your name: ")
    print("Hello, " + user_input + "!")

def command_injection(command):
    # Security Hotspot: Command injection vulnerability
    os.system(command)

def insecure_random():
    # Security Hotspot: Using a predictable random number generator
    return os.urandom(16)

def main():
    # Example of using the insecure functions
    file_content = insecure_file_read('example.txt')
    print(file_content)

    hashed_password = weak_hashing('mysecretpassword')
    print("Hashed password:", hashed_password)

    insecure_input()

    command_injection("ls -la")  # This could be dangerous if user input is used

    random_bytes = insecure_random()
    print("Random bytes:", random_bytes)

if __name__ == "__main__":
    main()
