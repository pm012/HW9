
phone_book = dict()

# Decorator implementation
# handling errors
def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError as e:
            if str(e)=='':
                return "Provide a usernmae"
            else:
                return str(e)
        except ValueError as e:
            if str(e)=="Invalid parameters":
                return "Unable to update. Incorrect usename. Use add <name> <phone> to add a new user"
            else:
                return str(e)
        except IndexError as e:
            if str(e)=='list index out of range':
                return "Provide name and phone"
            else:
                return str(e)
       
    return inner

# Handlers

# Greetings (command: hello)
def answer_greeting():
    return "How can I help you?"

# Add contact to the data base (command: add)
@input_error
def set_contact(*args)->str:    
    if args[0][1] in phone_book:
        raise ValueError(f"Contact with such name ({args[0][1]}) already exists. You should use 'change' command to ammend it")
    else:
        phone_book[args[0][1]] = args[0][2]
        return f"Contact {args[0][1]} {args[0][2]} is added to DBMS"

# Update phone for existing contact by its name (command: change)
@input_error
def update_phone(*args)->str:    
    if args[0][1] in phone_book:
        phone_book[args[0][1]]= args[0][2]
        return f"Contact {args[0][1]} phone number is changed to {args[0][2]}"
    else:
        raise ValueError(f"Contact {args[0][1]} is not found!")

# Get contact phone by name (command: phone)
@input_error
def get_phone(*args)->str:
    if len(args)<=1:
        raise ValueError(f"Please, provide name for this command")
    if args[0][1] in phone_book:
        return f" The contact {args[0][1]} has phone number: {phone_book[args[0][1]]}"
    else:
        raise KeyError(f"No contact with name {args[0][1]}")

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

# Handler function
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
                print(get_handler(commands[0])(commands))
            case 'change':
                print(get_handler(commands[0])(commands))
            case 'phone':
                print(get_handler(commands[0])(commands))
            case 'show':
                if commands[1]=='all':
                    print(get_handler(f"{commands[0]} {commands[1]}")())
            case _:
                print("Incorrect command, please provide the command from the list in command prompt")
        

if __name__ == '__main__':
    main()

