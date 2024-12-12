import streamlit as st
import random

# ---------------------------
# Session State Initialization
# ---------------------------
if "app_stage" not in st.session_state:
    # app_stage can be: "get_name", "why_here", "practice"
    st.session_state.app_stage = "get_name"
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "selected_tense_key" not in st.session_state:
    st.session_state.selected_tense_key = None
if "submitted_questions" not in st.session_state:
    st.session_state.submitted_questions = set()
if "randomized_messages" not in st.session_state:
    motivational_sentences = [
        "You're on fire! 🔥",
        "Keep smashing it! 💥",
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
    random.shuffle(motivational_sentences)
    st.session_state.randomized_messages = motivational_sentences

# ---------------------------
# Tenses Data
# ---------------------------
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
        ],
        "extra_examples": [
            "I always wake up at 7 AM.",
            "My brother doesn't eat fish.",
            "Do we need more milk?",
            "The Earth revolves around the Sun.",
            "They never watch TV in the morning."
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
            "Past habits or situations (often with 'used to')."
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
        ],
        "extra_examples": [
            "I visited my grandparents last weekend.",
            "They watched a movie yesterday.",
            "Did you talk to your friend about the issue?",
            "She cooked dinner last night.",
            "We didn’t see them at the party."
        ]
    },
}

# ---------------------------
# Helper Functions
# ---------------------------
def personalized_name():
    name = st.session_state.user_name.strip()
    return name if name else "You"

def reset_for_new_tense():
    st.session_state.submitted_questions = set()
    random.shuffle(st.session_state.randomized_messages)

# ---------------------------
# Layout: Sidebar Tense Selection
# ---------------------------
st.sidebar.title("Grammar Tense Selection")
tense_options = ["Select a tense..."] + [f"{key}. {tenses_data[key]['name']}" for key in tenses_data]
selected_option = st.sidebar.selectbox("Choose a tense to practice:", tense_options)

if selected_option != "Select a tense...":
    current_tense_key = selected_option.split('.')[0].strip()
    if current_tense_key != st.session_state.selected_tense_key:
        st.session_state.selected_tense_key = current_tense_key
        reset_for_new_tense()
else:
    st.session_state.selected_tense_key = None

# ---------------------------
# Screens
# ---------------------------

def show_get_name_screen():
    # Big, attractive font for name input
    st.markdown("""
    <style>
    .big-font {
        font-size: 50px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Welcome to the Grammar Genius Game!</p>', unsafe_allow_html=True)

    st.write("Please enter your name to begin:")
    user_name = st.text_input("", key="user_name")
    if user_name.strip():
        if st.button("Continue"):
            st.session_state.app_stage = "why_here"

def show_why_here_screen():
    # Modified the question to include the user's name at the start
    st.markdown(f"<h1 style='text-align:center;'>{personalized_name()} – Why are you here?!</h1>", unsafe_allow_html=True)

    options = [
        "Because I love learning English with all my heart",
        "My teacher made me use this app"
    ]
    choice = st.radio("", options)
    if st.button("Continue"):
        # Both answers are correct, so we just move on
        st.session_state.app_stage = "practice"

def show_practice_screen():
    if st.session_state.selected_tense_key is None:
        show_main_instructions()
    else:
        show_explanation_and_questions()

def show_main_instructions():
    st.title("Choose a tense from the sidebar!")
    st.write("Select a tense to begin practicing your English grammar. Once selected, you'll see the explanation and questions.")

def show_explanation_and_questions():
    key = st.session_state.selected_tense_key
    if key is None:
        return

    tense_info = tenses_data[key]

    # Fade-out cat gif at the top (optional)
    st.markdown("""
    <style>
    @keyframes fadeOut {
      from {opacity: 1;}
      to {opacity: 0;}
    }
    #catgif {
      animation: fadeOut 10s forwards;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<div id="catgif"><img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="200"></div>', unsafe_allow_html=True)

    st.header(tense_info["name"])
    st.subheader("How is it formed?")
    for form_type, form_rule in tense_info["formation"].items():
        st.write(f"**{form_type}:** {form_rule}")

    st.subheader("When do we use it?")
    for usage in tense_info["usage_explanation"]:
        st.write("- " + usage)

    with st.expander("More Examples"):
        if "extra_examples" in tense_info:
            for ex in tense_info["extra_examples"]:
                st.write("- " + ex)

    st.subheader("Practice Questions")
    total_questions = len(tense_info["usage_cases"])

    # Count how many have been answered
    answered_count = len(st.session_state.submitted_questions)
    st.write(f"Questions answered: {answered_count}/{total_questions}")

    if answered_count == total_questions:
        # All answered
        st.success(f"Congratulations, {personalized_name()}! You've answered all the questions!")
        # Dancing cat GIF at the end
        st.markdown('<img src="https://media.giphy.com/media/5Zesu5VPNGJlm/giphy.gif" width="300">', unsafe_allow_html=True)
        st.balloons()
        st.write("Feel free to choose another tense from the sidebar!")
        return

    # Display questions
    for i, case in enumerate(tense_info["usage_cases"]):
        answer_key = f"answer_{key}_{i}"
        submit_key = f"submit_{key}_{i}"

        if submit_key in st.session_state.submitted_questions:
            # Already answered: show the question and user's answer
            st.write(f"**{case['title']}**")
            st.write(case["question"])
            user_answer = st.session_state.get(answer_key, "")
            st.write(f"Your answer: {user_answer}")
            continue

        st.write(f"**{case['title']}**")
        st.write(case["question"])
        st.text_input("Your answer:", key=answer_key)

        if st.button("Submit", key=submit_key):
            user_answer = st.session_state.get(answer_key, "")
            st.session_state.submitted_questions.add(submit_key)
            msg_index = len(st.session_state.submitted_questions) - 1
            msg = st.session_state.randomized_messages[msg_index]

            # Personalize the message by adding the user's name
            if msg[0].isupper():
                personalized_msg = f"{personalized_name()}, {msg[0].lower() + msg[1:]}"
            else:
                personalized_msg = f"{personalized_name()}, {msg}"
            st.success(personalized_msg)

            # Immediately show the user's answer after submission
            st.write(f"Your answer: {user_answer}")

# ---------------------------
# Main Execution
# ---------------------------
def main():
    if st.session_state.app_stage == "get_name":
        show_get_name_screen()
    elif st.session_state.app_stage == "why_here":
        show_why_here_screen()
    elif st.session_state.app_stage == "practice":
        show_practice_screen()

if __name__ == "__main__":
    main()
