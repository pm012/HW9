
phone_book = dict()

# Decorator implementation
# handling errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone, please"
        except IndexError:
            return "Invalid command. Type 'help' for a list of commands."
       
    return inner

# Handlers

# Greetings (command: hello)
def answer_greeting():
    return "How can I help you?"

# Add contact to the data base (command: add)
@input_error
def set_contact(name:str, phone:str)->str:
    phone_book[name] = phone
    return f"Contact {name} {phone} is added to DBMS"

# Update phone for existing contact by its name (command: change)
@input_error
def update_phone(name:str, phone:str)->str:
    if name in phone_book:
        phone_book[name]= phone
        return f"Contact {name} phone number is changed to {phone}"
    else:
        return f"Contact {name} is not found!"

# Get contact phone by name (command: phone)
@input_error
def get_phone(name:str)->str:
    if name in phone_book:
        return f" The contact {name} has phone number: {phone_book[name]}"
    else:
        return f"Contact {name} not found"

# Print all contacts in the data base (command: show all)
def display():
    if not phone_book:
        return "No contacts found."
    else:
        result = "Contacts:\n"
        for name, phone in phone_book.items():
            result+= f"{name}: {phone}\n"
        return result    


# Quit the program ( command: good buy, close, exit)
def quit_bot():
    quit()

# Hendler function
@input_error
def get_handler(command):    
    return COMMANDS[command]



COMMANDS = {
    'hello': answer_greeting,
    'add': set_contact,
    'change': update_phone,
    'phone' : get_phone,
    'show all': display,
    'exit' : quit_bot
}




def main():
    exit_cmds = ["good bye", "close", "exit"]
    while True:
        commands = input("Enter a command(hello, add, change, phone, show all, exit or [good bye, close]) from the list above: ").split(' ')
        if commands[0] in exit_cmds:
            commands[0]='exit'
        match commands[0]:
            case 'exit':
                print("Good bye!")
                get_handler(commands[0])()
            case 'hello':
                print(get_handler(commands[0])())
            case 'add':
                print(get_handler(commands[0])(commands[1], commands[2]))
            case 'change':
                print(get_handler(commands[0])(commands[1], commands[2]))
            case 'phone':
                print(get_handler(commands[0])(commands[1]))
            case 'show':
                if commands[1]=='all':
                    print(get_handler(f"{commands[0]} {commands[1]}")())
            case _:
                print("Invalid parameters")
        

if __name__ == '__main__':
    main()

