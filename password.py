import random
import string

def generate_password(length):
   
    if length < 4: 
        return "Number is must be at least 4 and more than 4"
    

    
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]

    
    password += random.choices(all_characters, k=length - 4)

    
    random.shuffle(password)

   
    return ''.join(password)

def main():
   
    print("Generator your password")
    while True:
        try:
            length = int(input("Enter the password length: "))
            break
        except ValueError:
            print("Please enter the number")

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
