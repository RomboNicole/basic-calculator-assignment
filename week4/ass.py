# Program: File Read and Write with Error Handling
# Description:
# This program reads a file, modifies its content based on user's choice (uppercase or reverse lines),
# and writes the modified content into a new file. It also handles errors like file not found or unreadable files.

def modify_content(content, choice):
    if choice == '1':
        # Make all text uppercase
        return content.upper()
    elif choice == '2':
        # Reverse the lines
        lines = content.splitlines()
        reversed_lines = lines[::-1]
        return '\n'.join(reversed_lines)
    else:
        return content

def read_and_modify_file(input_filename, output_filename, choice):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        modified_content = modify_content(content, choice)

        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read or write the file.")

def main():
    print("Welcome to the File Modifier Program!")

    while True:
        input_filename = input("Enter the name of the file to read: ")
        try:
            with open(input_filename, 'r') as f:
                break  # File exists, move on
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' was not found. Please try again.\n")

    output_filename = input("Enter the name of the new file to create: ")
    
    print("\nChoose how you want to modify the file:")
    print("1. Convert all text to UPPERCASE")
    print("2. Reverse the order of lines")
    choice = input("Enter your choice (1 or 2): ")

    if choice not in ('1', '2'):
        print("Invalid choice. Exiting the program.")
        return

    read_and_modify_file(input_filename, output_filename, choice)
    
    print("\nThank you for using the File Modifier Program! Goodbye! 👋")

if __name__ == "__main__":
    main()


