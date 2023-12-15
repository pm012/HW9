
phone_book = dict()


# handling errors
def input_error(func):
    pass


# Decorator
@input_error
def error_handling_factory():
    pass

# Handlers

# Greetings (command: hello)
def answer_greeting():
    return "How can I help you?"

# Add contact to the data base (command: add)
def set_contact(name:str, phone:str)->str:
    phone_book[name] = phone

# Update phone for existing contact by its name (command: change)
def update_phone(name:str, phone:str)->str:
    phone_book.update({name: phone})

# Get contact phone by name (command: phone)
def get_phone(name:str)->str:
    return phone_book[name]

# Quit the program ( command: good buy, close, exit)
def quit_bot():
    quit()

# Hendler function
def get_handler(command):
    return COMMANDS[command]

# Print all contacts in the data base (command: show all)
def display():
    return str(phone_book)

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
                get_handler(commands[0])(commands[1], commands[2])
            case 'change':
                get_handler(commands[0])(commands[1], commands[2])
            case 'phone':
                print(get_handler(commands[0])(commands[1]))
            case 'show':
                if commands[1]=='all':
                    print(get_handler(f"{commands[0]} {commands[1]}")())
        

if __name__ == '__main__':
    main()

