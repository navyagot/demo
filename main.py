import json
import os


# Function to load entries for a specific user
def load_entries(username):
    """Load journal entries from a JSON file for a specific user."""
    filename = f'{username}_journal_entries.json'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
                return data.get('entries', {}) if isinstance(data.get('entries'), dict) else {}
            except json.JSONDecodeError:
                print("Error: Could not decode JSON, returning empty entries.")
                return {}
    return {}  # Return an empty dictionary if the file doesn't exist


# Function to save entries for a specific user
def save_entries(username, entries):
    """Save journal entries to a JSON file for a specific user."""
    filename = f'{username}_journal_entries.json'
    with open(filename, 'w') as file:
        json.dump({'entries': entries}, file)


def view_entry_names(entries):
    """Display all journal entry names."""
    if not entries:
        print("You have no journal entries.")
        return
    print("Your Journal Entry Names:")
    for idx, name in enumerate(entries.keys(), start=1):
        print(f"{idx}: {name}")

def check_answer(answer):
    if answer == 1 or answer == 2 or answer == 3 or answer == 4 or answer == 5:
        return True

    else:
        print("This is an invalid answer. Please try again and only input a number between 1 and 5.")
        return False


def chatbot():
    username = input("What is your username?")
    entries = load_entries(username)  # Load entries at the start
    print("Welcome to your journal!")
    choice = input("Would you like to journal, or would you rather take a short survey to see where you're at? "
                   "(survey/journal): ")
    if choice.lower() == "journal":
        while True:
            command = input("What would you like to do? (write/view/exit): ").strip().lower()

            if command == 'exit':
                # Save entries before exiting
                save_entries(username, entries)
                print("Goodbye!")
                break
            elif command == 'write':
                entry_name = input("Enter a name for your journal entry: ")
                entry_content = input("Enter your journal entry: ")
                entries[entry_name] = entry_content  # Save the entry with its name
                print("Your entry has been saved.")
            elif command == 'view':
                view_entry_names(entries)  # Display entry names
                entry_number = input("Enter the number of the entry you want to view (or 'back' to go back): ").strip()
                if entry_number.lower() == 'back':
                    continue
                try:
                    index = int(entry_number) - 1  # Convert to zero-based index
                    names_list = list(entries.keys())
                    if 0 <= index < len(names_list):
                        entry_name = names_list[index]
                        print(f"Entry '{entry_name}': {entries[entry_name]}")
                    else:
                        print("Invalid entry number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Unknown command. Please type 'write', 'view', or 'exit'.")

    elif choice.lower() == "survey":
        score = 0
        print("Please answer the following questions about how you are feeling with numbers 1-5, with 1 being the worst and 5 being the best.")
        firstAnswer = int(input("How would you rate your overall mental well-being currently? "))
        if check_answer(firstAnswer):
            score += firstAnswer
            secondAnswer = int(input("How would you rate your current stress levels on average? "))

            if check_answer(secondAnswer):
                score += secondAnswer
                thirdAnswer = int(input("Do you feel as though you have a support system regarding your mental health? "))

                if check_answer(thirdAnswer):
                    score += thirdAnswer

        while check_answer(firstAnswer) and check_answer(secondAnswer) and check_answer(thirdAnswer):
            if score >= 12:
                print("Congratulations! You seem to be doing very well in terms of your mental health, but it is important "
                      "to remember that this may not always be the case. Make sure to reach out for help if you need it, as "
                      "there are plenty of existing resources and websites for you to go to, and people to talk to.")
                break
            elif score <= 11 and score >= 8:
                print("You don't sound like you're doing too well. I recommend talking to a trusted family member or even and "
                      "trying to understand why you might be feeling this way. Make sure to relieve yourself of any unnecessary stressors "
                      "and try to maintain a positive attitude! Make sure to check out resources like Never a Bother, or the institute for Mental Health "
                      "to find the help you need. Always remember that you and your mental health are important!")
                break
            else:
                print("There are many resources available for you to get the help you need. According to your answers, your mental health "
                      "seems to be suffering and this can be detrimental for you and your physical health as well. Make sure to check out "
                      "websites like the National Institute for Mental Health or even websites like Never a Bother, where resources "
                      "and phone numbers are available to you for 24/7 use. Remember that you should prioritize your mental health "
                      "just as much as you prioritize other parts of your life. You are important.")
                break

    elif choice.lower() == "quit":
        print("Goodbye!")
    else:
        print("Unknown command. Please type 'journal', 'quiz', or 'exit'.")


chatbot()
