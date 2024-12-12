import streamlit as st

# Initialize session state variables if they don't exist
if "mode" not in st.session_state:
    st.session_state.mode = "menu"
if "selected_tense_key" not in st.session_state:
    st.session_state.selected_tense_key = None
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# Tense data with 10 examples each
tenses_info = {
    "1": {
        "name": "Present Simple",
        "explanation": "The Present Simple is used for habits, general truths, and routines.",
        "examples": [
            "I drink coffee every morning.",
            "He walks to work every day.",
            "They usually play tennis on weekends.",
            "The sun rises in the east and sets in the west.",
            "My friend tells the funniest jokes.",
            "Birds sing outside my window at dawn.",
            "Students learn new things at school.",
            "My sister works at a hospital.",
            "We enjoy reading good books.",
            "Cars stop at red lights."
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
            "We danced until midnight at the party.",
            "I lost my keys yesterday.",
            "They traveled to Spain last summer.",
            "He studied French in high school.",
            "We painted the living room walls.",
            "She finished her report on time."
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
            "He is watching a funny cat video.",
            "I am currently listening to music.",
            "You are improving with every practice.",
            "We are planning our next vacation.",
            "They are building a new playground.",
            "She is writing her new novel."
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
            "He was playing video games all afternoon.",
            "I was working late when the power went out.",
            "You were trying to fix the printer at midnight.",
            "They were painting the fence all morning.",
            "She was waiting patiently in line.",
            "We were discussing the problem for hours."
        ]
    },
    "5": {
        "name": "Present Perfect",
        "explanation": "The Present Perfect is used for actions that happened at an unspecified time or started in the past and continue now.",
        "examples": [
            "I have visited Paris three times.",
            "She has lost her keys again!",
            "They have already eaten breakfast.",
            "We have watched that movie before.",
            "He has just finished his homework.",
            "I have met many interesting people this year.",
            "You have grown so much since last summer.",
            "We have improved our cooking skills recently.",
            "They have opened a new store in town.",
            "She has studied hard for the exam."
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
            "He will finish the project soon.",
            "I will bake a cake for the party.",
            "She will announce the results later.",
            "They will remember this moment forever.",
            "He will pass his driving test.",
            "We will start the project next month."
        ]
    },
    "7": {
        "name": "Future Continuous",
        "explanation": "The Future Continuous is used for actions that will be in progress at a particular time in the future.",
        "examples": [
            "I will be working at 8 PM tomorrow.",
            "She will be studying abroad next semester.",
            "They will be traveling through Europe in June.",
            "We will be waiting for your call.",
            "He will be sleeping when you arrive.",
            "I will be reading a novel this evening.",
            "She will be exercising at the gym tomorrow morning.",
            "They will be exploring the city by bike.",
            "We will be rehearsing for the show.",
            "He will be recording new songs next week."
        ]
    }
}

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

def show_menu():
    st.title("Grammar Genius Game")
    st.write("Practice English tenses with a friendly, interactive interface!")
    tense_options = [f"{key}. {tenses_info[key]['name']}" for key in tenses_info]
    choice = st.selectbox("Select a tense to practice:", tense_options + ["Exit"])
    if st.button("Start"):
        if "Exit" in choice:
            st.write("Thanks for visiting! Come back anytime.")
        else:
            key = choice.split('.')[0]
            st.session_state.selected_tense_key = key.strip()
            st.session_state.mode = "explanation"
            st.session_state.question_index = 0
            st.session_state.answers = []

def show_explanation():
    key = st.session_state.selected_tense_key
    info = tenses_info[key]
    st.title(info["name"])
    st.write(info["explanation"])
    st.markdown("**Examples:**")
    for ex in info["examples"]:
        st.write("- " + ex)
    if st.button("Begin Practice"):
        st.session_state.mode = "questioning"

def show_question():
    key = st.session_state.selected_tense_key
    info = tenses_info[key]
    q_num = st.session_state.question_index + 1
    st.title(f"Question {q_num}")
    st.write(f"Please write a sentence using **{info['name']}**.")

    # Use a unique key for the text input so it does not persist from previous questions
    user_answer = st.text_input("Your answer", key=f"answer_q{q_num}")

    if st.button("Submit Answer", key=f"submit_q{q_num}"):
        st.session_state.answers.append(user_answer)
        # Show motivational message
        msg_index = min(len(st.session_state.answers)-1, len(motivational_sentences)-1)
        st.write(motivational_sentences[msg_index])

        if q_num == 10:
            # After 10 questions, go to done mode
            st.session_state.mode = "done"
        else:
            # Move to the next question
            st.session_state.question_index += 1

def show_done():
    key = st.session_state.selected_tense_key
    info = tenses_info[key]
    st.title("Great Job!")
    st.write(f"You've completed the 10 questions for {info['name']}!")
    if st.button("Return to Main Menu"):
        st.session_state.mode = "menu"

# Main logic
if st.session_state.mode == "menu":
    show_menu()
elif st.session_state.mode == "explanation":
    show_explanation()
elif st.session_state.mode == "questioning":
    show_question()
elif st.session_state.mode == "done":
    show_done()

