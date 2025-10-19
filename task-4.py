def parse_input(user_input):
    """
    Parses user input into command and arguments.
    Args:
        user_input (str): Raw input from user  
    Returns:
        tuple: (command, *args) where command is lowercase string and args is list
    """
    # empty input
    if not user_input.strip():
        return "invalid", []
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Adds a new contact to the contacts dictionary.
    
    Args:
        args (list): List containing [name, phone]
        contacts (dict): Dictionary of contacts
        
    Returns:
        str: Confirmation message
    """
    if len(args) != 2:
        return "Error: Please provide name and phone number."
    
    name, phone = args
    
    #phone number format - digits only
    if not phone.isdigit():
        return "Error: Phone number should contain only digits."
    
    # if contact already exists
    if name in contacts:
        return f"Error: Contact '{name}' already exists. Use 'change' command to update."
    
    contacts[name] = phone
    return "Contact added successfully."


def change_contact(args, contacts):
    """
    Changes the phone number of an existing contact.
    
    Args:
        args (list): List containing [name, new_phone]
        contacts (dict): Dictionary of contacts
        
    Returns:
        str: Confirmation message or error
    """
    if len(args) != 2:
        return "Error: Please provide name and new phone number."
    
    name, phone = args
    
    # phone number format
    if not phone.isdigit():
        return "Error: Phone number should contain only digits."
    
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    
    contacts[name] = phone
    return f"Contact '{name}' updated successfully."


def show_phone(args, contacts):
    """
    Shows the phone number of a specific contact.
    
    Args:
        args (list): List containing [name]
        contacts (dict): Dictionary of contacts
        
    Returns:
        str: Phone number or error message
    """
    if len(args) != 1:
        return "Error: Please provide a contact name."
    
    name = args[0]
    
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    
    return f"{name}: {contacts[name]}"


def show_all(contacts):
    """
    Shows all saved contacts with phone numbers.
    
    Args:
        contacts (dict): Dictionary of contacts
        
    Returns:
        str: All contacts or message if no contacts exist
    """
    if not contacts:
        return "No contacts saved yet."
    
    result = "\nAll contacts:"
    for name, phone in sorted(contacts.items()):  # Sort contacts by name
        result += f"\n{name}: {phone}"
    return result


def main():
    """
    Main function that manages the command processing loop.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        try:
            user_input = input("\nEnter a command (Help - to see available) ): ").strip()
            command, *args = parse_input(user_input)
            
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            
            elif command == "hello":
                print("How can I help you?")
            
            elif command == "add":
                print(add_contact(args, contacts))
            
            elif command == "change":
                print(change_contact(args, contacts))
            
            elif command == "phone":
                print(show_phone(args, contacts))
            
            elif command == "all":
                print(show_all(contacts))
            
            elif command == "help":
                print("\nAvailable commands:")
                print("  - hello: Get a greeting")
                print("  - add [name] [phone]: Add a new contact")
                print("  - change [name] [phone]: Update existing contact")
                print("  - phone [name]: Show phone number for a contact")
                print("  - all: Show all contacts")
                print("  - help: Show this help message")
                print("  - exit or close: Exit the program")
            
            else:
                print("Invalid command. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\nGood bye!")
            break
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()