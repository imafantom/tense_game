import sys
import os
import time
from colorama import init, Fore, Style

init(autoreset=True)

# ---------------------------------------------------------
# Data structures and constants
# ---------------------------------------------------------

# Tenses data: Each entry includes a brief explanation and some example sentences.
tenses_info = {
    "1": {
        "name": "Present Simple",
        "explanation": "The Present Simple is used for habits, general truths, and routines.",
        "examples": [
            "I drink coffee every morning.",
            "He walks to work every day.",
            "They usually play tennis on weekends.",
            "The sun rises in the east and sets in the west.",
            "My friend tells the funniest jokes."
        ]
    },
    "2": {
        "name": "Past Simple",
        "explanation": "The Past Simple is used for actions completed in the past, often with a time reference.",
        "examples": [
            "I visited my grandparents last weekend.",
            "She cooked a delicious meal yesterday.",
            "They watched a movie on Friday night.",
            "He cleaned his room before dinner.",
            "We danced until midnight at the party."
        ]
    },
    "3": {
        "name": "Present Continuous",
        "explanation": "The Present Continuous is used for actions happening right now or around the current time.",
        "examples": [
            "I am studying English at the moment.",
            "She is baking cookies right now.",
            "They are playing football in the park.",
            "We are learning new skills every day.",
            "He is watching a funny cat video."
        ]
    },
    "4": {
        "name": "Past Continuous",
        "explanation": "The Past Continuous is used for actions that were in progress at a particular time in the past.",
        "examples": [
            "I was reading a book when you called.",
            "They were walking their dog yesterday evening.",
            "She was cooking dinner while listening to the radio.",
            "We were chatting about our holidays when the bus arrived.",
            "He was playing video games all afternoon."
        ]
    },
    "5": {
        "name": "Present Perfect",
        "explanation": "The Present Perfect is used for actions that happened at an unspecified time, or that started in the past and continue now.",
        "examples": [
            "I have visited Paris three times.",
            "She has lost her keys again!",
            "They have already eaten breakfast.",
            "We have watched that movie before.",
            "He has just finished his homework."
        ]
    },
    "6": {
        "name": "Future Simple",
        "explanation": "The Future Simple is used for predictions, promises, and decisions made at the moment of speaking.",
        "examples": [
            "I will call you tomorrow.",
            "She will visit her aunt next week.",
            "They will probably come to the party.",
            "We will see what happens.",
            "He will finish the project soon."
        ]
    },
    "7": {
        "name": "Future Continuous",
        "explanation": "The Future Continuous is used for actions that will be in progress at a certain time in the future.",
        "examples": [
            "I will be working at 8 PM tomorrow.",
            "She will be studying abroad next semester.",
            "They will be traveling through Europe in June.",
            "We will be waiting for your call.",
            "He will be sleeping when you arrive."
        ]
    }
}

# Predefined motivational sentences.
# Each sentence should be slightly longer and more encouraging than the last.
motivational_sentences = [
    "You're on fire! 🔥",
    "Keep smashing it, language legend! 💥",
    "Fantastic answer! Your words are shining brighter now! 🌟",
    "You're a grammar wizard! Conjugations bend to your will! 🧙‍♂️",
    "Way to go, champ! That sentence just leapt off the page! 🏆",
    "Bravo! That's the spirit! Your linguistic muscles are flexing! 👏",
    "Grammar genius at work! Your sentences sparkle like diamonds! 🧠",
    "Outstanding! The grammar gods are smiling upon you now! 🥳",
    "You're unstoppable! The universe is taking notes from your syntax! 🚀",
    "Wonderful! Each answer you give writes poetry in the sky! 🎩✨",
    "You're dazzling! These sentences are lining up to be in your presence! ✨🌈",
    "Impressive! Your answers radiate confidence and linguistic flair! 💎💃",
    "Marvelous! The grammar galaxy bows before your might! 🌌🏅",
    "Astonishing! Every verb you conjure becomes a masterpiece! 🎉📚",
    "Magnificent! Even dictionaries blush at your command of words! 🦄📖",
    "Incredible! Grammarians form fan clubs in your honor! 🎶💫",
    "Stupendous! Your verb forms could charm the toughest critics! 🍀💬",
    "Glorious! Your tense usage now inspires entire textbooks! 🦋🔥",
    "Remarkable! Each reply is like a linguistic symphony in action! 🎼🌍",
    "Spectacular! Your English prowess bursts forth like cosmic fireworks! 💥🚀🎉"
]

# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def clear_screen():
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.CYAN + Style.BRIGHT + title.center(60))
    print(Fore.CYAN + Style.BRIGHT + "=" * 60 + "\n" + Style.RESET_ALL)

def print_divider():
    print(Fore.BLUE + "-" * 60 + Style.RESET_ALL)

def slow_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ---------------------------------------------------------
# Core functions
# ---------------------------------------------------------

def show_introduction():
    clear_screen()
    print_header("Welcome to the Grammar Genius Game!")
    introduction_text = (
        "In this game, you'll practice using English verb tenses by answering questions.\n"
        "Here's how it works:\n"
        "- From the main menu, select a tense you'd like to practice.\n"
        "- We'll show you a brief explanation and a few example sentences.\n"
        "- Then, you'll answer 10 questions in that tense.\n"
        "- After each answer, you'll receive a motivational message that grows more enthusiastic!\n"
        "Ready to become a grammar hero? Let's begin!"
    )
    slow_print(introduction_text, 0.003)
    input(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)

def show_main_menu():
    clear_screen()
    print_header("Main Menu")
    print(Fore.YELLOW + "Select a tense to practice:" + Style.RESET_ALL)
    for key, info in tenses_info.items():
        print(f"{key}. {info['name']}")
    print("8. Exit")
    print_divider()

def show_tense_info(tense_key):
    clear_screen()
    name = tenses_info[tense_key]["name"]
    explanation = tenses_info[tense_key]["explanation"]
    examples = tenses_info[tense_key]["examples"]

    print_header(name)
    slow_print(Fore.WHITE + explanation + Style.RESET_ALL, 0.003)
    print_divider()
    slow_print("Examples:", 0.003)
    for ex in examples:
        slow_print(Fore.MAGENTA + "- " + ex + Style.RESET_ALL, 0.003)
    print_divider()

def ask_questions(tense_key):
    # In a real scenario, here we could generate or store questions. 
    # For simplicity, we'll use a generic prompt and let the user input anything.
    # The focus is on the structure, motivation, and visual layout.
    name = tenses_info[tense_key]["name"]

    slow_print(Fore.YELLOW + "Now, let's practice " + name + "!" + Style.RESET_ALL, 0.003)
    slow_print("Answer the following 10 questions using the " + name + ".", 0.003)
    print_divider()

    for i in range(10):
        question_num = i + 1
        question_prompt = f"Question {question_num}: Please write a sentence using {name}.\nYour answer: "
        user_answer = input(Fore.GREEN + question_prompt + Style.RESET_ALL)
        
        # Display motivational message
        if i < len(motivational_sentences):
            message = motivational_sentences[i]
        else:
            # If we somehow go beyond the list length, just repeat the last one.
            message = motivational_sentences[-1]
        
        slow_print(Fore.CYAN + message + Style.RESET_ALL, 0.003)
        print_divider()

    slow_print("Great job! You've completed the 10 questions for " + name + ".", 0.003)
    input(Fore.GREEN + "Press Enter to return to the main menu..." + Style.RESET_ALL)

def main():
    show_introduction()

    while True:
        show_main_menu()
        choice = input(Fore.GREEN + "Enter your choice: " + Style.RESET_ALL)
        
        if choice in tenses_info:
            show_tense_info(choice)
            input(Fore.GREEN + "Press Enter to start the questions..." + Style.RESET_ALL)
            ask_questions(choice)
        elif choice == "8":
            slow_print(Fore.YELLOW + "Thanks for playing! Keep practicing and shining brightly in your English journey!" + Style.RESET_ALL, 0.003)
            break
        else:
            slow_print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL, 0.003)

if __name__ == "__main__":
    main()
