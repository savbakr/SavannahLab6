def encode(password):
    encoded = ""
    for digit in password:
        encoded += str((int(digit) + 3) % 10)
    return encoded


def decode(encoded_password):
    decoded = ""
    for digit in encoded_password:
        decoded += str((int(digit) - 3) % 10)
    return decoded


def main():
    encoded_password = ""

    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            if len(password) != 8 or not password.isdigit():
                print("Invalid password. Please enter an 8-digit password containing only integers.")
            else:
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")

        elif option == '2':
            if encoded_password:
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("Please encode a password first.")

        elif option == '3':
            print("Thank you for using the encoder/decoder program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()