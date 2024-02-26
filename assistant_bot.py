"""
Module for an assistant bot that recognizes commands entered from the keyboard 
and responds according to the entered command.

This module demonstrates a simple implementation of a command-based interaction with a user,
handling predefined commands like greeting, help, and exit.
"""

def handle_command(command):
    """
    Handles the entered commands and prints corresponding messages.
    
    Args:
    - command (str): The command to handle.
    
    Returns:
    - bool: True if the command is 'exit', indicating the program should terminate.
            False otherwise, indicating the program should continue running.
    """
    if command == "hello":
        print("Hello! I'm your assistant bot. How can I assist you today?")
    elif command == "help":
        print("I can respond to the following commands:\n"
              "- hello: greetings\n"
              "- help: display this help message\n- exit: exit the program")
    elif command == "exit":
        print("Goodbye!")
        return True
    else:
        print("Sorry, I don't understand this command. Try 'help' for a list of commands.")
    return False

def main():
    """
    Main function to run the assistant bot.
    """
    print("Welcome! I'm your assistant bot. Enter 'help' to see the list of commands.")
    while True:
        command = input("Enter a command: ").strip().lower()
        if handle_command(command):
            break

if __name__ == "__main__":
    main()
