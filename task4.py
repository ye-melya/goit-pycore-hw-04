def parse_input(user_input):
    parts = user_input.split()

    if len(parts) == 0:
        return "", []

    command = parts[0].lower()
    args = parts[1:]

    return command, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Введіть: add ім'я телефон"

    name, phone = args
    name = name.lower()
    contacts[name] = phone

    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Введіть: change ім'я телефон"

    name, phone = args
    name = name.lower()

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone

    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Введіть: phone ім'я"

    name = args[0].lower()

    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts):
    if len(contacts) == 0:
        return "No contacts."

    result = ""

    for name, phone in contacts.items():
        result = result + name + ": " + phone + "\n"

    return result.strip()


def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"] and len(args) == 0:
            print("Good bye!")
            break

        elif command == "hello" and len(args) == 0:
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all" and len(args) == 0:
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()