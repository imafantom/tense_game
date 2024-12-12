import streamlit as st

# Initialize session state variables
if "selected_tense_key" not in st.session_state:
    st.session_state.selected_tense_key = None
if "answers" not in st.session_state:
    st.session_state.answers = []
if "submitted_questions" not in st.session_state:
    st.session_state.submitted_questions = set()
if "previous_tense" not in st.session_state:
    st.session_state.previous_tense = None

# Motivational messages
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

tenses_data = {
    "1": {
        "name": "Present Simple",
        "formation": {
            "Positive": "Subject + base form (e.g., 'I eat')",
            "Negative": "Subject + do not/does not + base form (e.g., 'I do not eat')",
            "Question": "Do/Does + subject + base form? (e.g., 'Do you eat?')",
            "Short answer": "'Yes, I do.' / 'No, I don't.'"
        },
        "usage_explanation": [
            "General or always true facts.",
            "Situations that are more or less permanent.",
            "Habits or things done regularly.",
            "Short actions happening now (e.g., in sports commentary).",
            "Regular events (often with always, often, never)."
        ],
        "usage_cases": [
            {"title": "Expressing facts and general truths", 
             "question": "Does water boil if you heat it up?"},
            {"title": "Describing habits",
             "question": "What do you usually do after waking up?"},
            {"title": "Talking about permanent situations",
             "question": "Where do you live?"},
            {"title": "Regular events",
             "question": "How often do you go to the gym?"},
            {"title": "Describing routines",
             "question": "What time do you start work every day?"},
            {"title": "Present commentary (sports/narration)",
             "question": "Does the commentator describe the players' actions as they happen?"},
            {"title": "General preferences",
             "question": "Which type of music do you prefer?"},
            {"title": "Timetabled events",
             "question": "When does the train leave?"},
            {"title": "Stating a general ability",
             "question": "Do you speak Spanish fluently?"},
            {"title": "Describing personality traits",
             "question": "Does your friend often help others?"}
        ]
    },
    "2": {
        "name": "Past Simple",
        "formation": {
            "Positive": "Subject + past form (e.g., 'I ate')",
            "Negative": "Subject + did not + base form (e.g., 'I did not eat')",
            "Question": "Did + subject + base form? (e.g., 'Did you eat?')",
            "Short answer": "'Yes, I did.' / 'No, I didn't.'"
        },
        "usage_explanation": [
            "Completed actions in the past.",
            "Actions that happened at a specific time.",
            "A series of actions in the past.",
            "Past habits or situations (often used with 'used to')."
        ],
        "usage_cases": [
            {"title": "Completed actions at a specific time",
             "question": "What did you do yesterday evening?"},
            {"title": "A specific past event",
             "question": "Did you attend the concert last Friday?"},
            {"title": "A series of events",
             "question": "What happened after you arrived home?"},
            {"title": "Past habits",
             "question": "Where did you usually spend your summer holidays as a child?"},
            {"title": "Situations that no longer exist",
             "question": "Did you live in another country before?"},
            {"title": "Historical facts",
             "question": "Which year did the Second World War end?"},
            {"title": "Personal achievements",
             "question": "What was the best meal you ever cooked?"},
            {"title": "Past trips or experiences",
             "question": "Where did you travel last year?"},
            {"title": "Old favorites",
             "question": "Which TV shows did you like when you were younger?"},
            {"title": "Childhood memories",
             "question": "Did you have a favorite toy when you were a kid?"}
        ]
    },
    "3": {
        "name": "Present Continuous",
        "formation": {
            "Positive": "Subject + am/is/are + verb-ing (e.g., 'I am eating')",
            "Negative": "Subject + am/is/are + not + verb-ing (e.g., 'I am not eating')",
            "Question": "Am/Is/Are + subject + verb-ing? (e.g., 'Are you eating?')",
            "Short answer": "'Yes, I am.' / 'No, I'm not.'"
        },
        "usage_explanation": [
            "Actions happening now, at this moment.",
            "Temporary situations.",
            "Trends and changing situations.",
            "Annoying habits (often with 'always')."
        ],
        "usage_cases": [
            {"title": "Actions happening right now",
             "question": "What are you doing at the moment?"},
            {"title": "Temporary situations",
             "question": "Are you staying with your parents this week?"},
            {"title": "Trends",
             "question": "Is online learning becoming more popular these days?"},
            {"title": "Changing situations",
             "question": "Is your town growing rapidly?"},
            {"title": "Annoying habits",
             "question": "Are you always leaving your keys on the table?"},
            {"title": "Current personal projects",
             "question": "Are you working on any new skills right now?"},
            {"title": "Unusual behavior",
             "question": "Are you eating more vegetables than usual lately?"},
            {"title": "Events in progress",
             "question": "Are they building a new mall near your house?"},
            {"title": "Ongoing discussions",
             "question": "Are people talking about the latest news?"},
            {"title": "Temporary job",
             "question": "Is your friend working at a cafe this summer?"}
        ]
    },
}

def reset_questions():
    st.session_state.answers = []
    st.session_state.submitted_questions = set()

# Sidebar: Always Visible Tense Selection
st.sidebar.title("Grammar Tense Selection")
tense_options = ["Select a tense..."] + [f"{key}. {tenses_data[key]['name']}" for key in tenses_data]
selected_option = st.sidebar.selectbox("Choose a tense to practice:", tense_options)

if selected_option != "Select a tense...":
    # If user picks a tense different from the previous one, reset answers
    current_tense_key = selected_option.split('.')[0].strip()
    if current_tense_key != st.session_state.selected_tense_key:
        st.session_state.selected_tense_key = current_tense_key
        reset_questions()
else:
    st.session_state.selected_tense_key = None
    reset_questions()

def show_welcome():
    st.image("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", use_column_width=True)
    st.title("Welcome to the Grammar Genius Game! 🎉")
    st.write("""
    Get ready to boost your English grammar skills in a fun and interactive way!
    
    1. Use the sidebar to choose an English tense.
    2. Read how it's formed, when to use it, and review sample usage cases.
    3. Answer the questions under each usage case.
    4. Receive motivational feedback as you progress!

    Let's get started! Pick a tense from the sidebar.
    """)

def show_explanation_and_questions():
    key = st.session_state.selected_tense_key
    tense_info = tenses_data[key]

    st.image("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", use_column_width=True)
    st.header(tense_info["name"])

    st.subheader("How is it formed?")
    for form_type, form_rule in tense_info["formation"].items():
        st.write(f"**{form_type}:** {form_rule}")

    st.subheader("When do we use it?")
    for usage in tense_info["usage_explanation"]:
        st.write("- " + usage)

    st.subheader("Practice Questions")
    st.write("Below are several usage cases of this tense. Please answer each question accordingly.")

    # Display all usage cases
    for i, case in enumerate(tense_info["usage_cases"]):
        st.write(f"**{case['title']}**")
        st.write(case["question"])
        answer_key = f"answer_{key}_{i}"
        if answer_key not in st.session_state:
            st.session_state[answer_key] = ""
        user_answer = st.text_input("Your answer:", key=answer_key)
        submit_key = f"submit_{key}_{i}"

        if st.button("Submit", key=submit_key):
            # Only record if not submitted before
            if submit_key not in st.session_state.submitted_questions:
                st.session_state.answers.append(user_answer)
                msg_index = min(len(st.session_state.answers)-1, len(motivational_sentences)-1)
                st.success(motivational_sentences[msg_index])
                st.session_state.submitted_questions.add(submit_key)
                st.experimental_rerun()

        # If already submitted, show success message again (based on the order of answers)
        if submit_key in st.session_state.submitted_questions:
            # Find index of this question's answer in the list
            # Since we append answers in order, the index should match the submission order
            q_index = list(st.session_state.submitted_questions).index(submit_key)
            if q_index < len(motivational_sentences):
                st.success(motivational_sentences[q_index])


def main():
    if st.session_state.selected_tense_key is None:
        show_welcome()
    else:
        show_explanation_and_questions()

if __name__ == "__main__":
    main()

