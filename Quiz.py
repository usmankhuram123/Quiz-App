import streamlit as st # Streamlit is used to build the interactive web app interface.
import pandas as pd # Pandas is used to organize and display quiz results in a table format.

# Quiz questions, options, and correct answers stored as a list of dictionaries
Quiz_data = [
    {
        "statement": "Which planet is known as the Red Planet?",
        "options": [
            "Jupiter",
            "Earth",
            "Venus",
            "Mars"
        ],
        "answer": "Mars"
    },
    {
        "statement": "What is the currency of Japan?",
        "options": [
            "Yen",
            "Won",
            "Yaun",
            "Ringgit"
        ],
        "answer": "Yen"
    },
    {
        "statement": "Which planet is closest to the Sun?",
        "options": [
            "Venus",
            "Earth",
            "Mercury",
            "Mars"
        ],
        "answer": "Mercury"
    },
    {
        "statement": "Which planet spins the fastest on its axis?",
        "options": [
            "Earth",
            "Jupiter",
            "Mars",
            "Neptune"
        ],
        "answer": "Jupiter"
    },
    {
        "statement": "What is the hardest natural substance on Earth?",
        "options": [
            "Gold",
            "Iron",
            "Diamond",
            "Quartz"
        ],
        "answer": "Diamond"
    },
    {
        "statement": "What is the name of the largest ocean on Earth?",
        "options": [
            "Atlantic",
            "Pacific",
            "Arctic",
            "Indian"
        ],
        "answer": "Pacific"
    },
    {
        "statement": "Which animal can hold its breath the longest underwater?",
        "options": [
            "Whale",
            "Crocodile",
            "Sea Turtle",
            "Sloth"
        ],
        "answer": "Sloth"
    },
    {
        "statement": "Which organ is responsible for filtering blood in the human body?",
        "options": [
            "Heart",
            "Liver",
            "Kidney",
            "Lungs"
        ],
        "answer": "Kidney"
    },
    {
        "statement": "Which country has the most volcanoes?",
        "options": [
            "Japan",
            "Indonesia",
            "USA",
            "Chile"
        ],
        "answer": "Indonesia"
    },
    {
        "statement": "Which planet is known for its rings?",
        "options": [
            "Jupiter",
            "Saturn",
            "Uranus",
            "Neptune"
        ],
        "answer": "Saturn"
    }
]

# App title and caption
st.title("Quiz App 📝")
st.caption("This is simple quiz app")

# Initialize session state variables to track progress and answers
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = []

if "show_result" not in st.session_state:
    st.session_state.show_result = False

# Initialize first question's radio button state
if f"q_0" not in st.session_state:
    st.session_state["q_0"] = None

# Function to move to the next question
def next_q(selected_option):
    st.session_state.selected_answer.append(selected_option)
    st.session_state.current_q += 1
    if st.session_state.current_q < len(Quiz_data):
        st.session_state[f"q_{st.session_state.current_q}"] = None
    else:
        st.session_state.show_result = True

# Function to restart the quiz
def restart_quiz():
    st.session_state.current_q = 0
    st.session_state.selected_answer = []
    st.session_state.show_result = False

# Display progress bar and question count
total_q = len(Quiz_data)
current_q = st.session_state.current_q
progress = current_q / total_q
st.progress(progress)
st.write(f"Question: {min(current_q + 1, total_q)} of {total_q}")

# Display current question or final results
if not st.session_state.show_result:
    current_q = st.session_state.current_q 
    q = Quiz_data[current_q]
    st.subheader(q["statement"])
    selected_option = st.radio(
        " Choose an answer:",
        q["options"],
        key = f"q_{current_q}"
    )
    st.button("Next ➡️", on_click = next_q, args = (selected_option,), type = "secondary")
else:
    # Calculate score and prepare result summary
    score = 0
    result = []
    for i, q in enumerate(Quiz_data):
        user_ans = st.session_state.selected_answer[i]
        correct_ans = q["answer"]
        is_correct = correct_ans == user_ans
        if is_correct:
            score += 1
        result.append(
            {
                "Question": q["statement"],
                "Your answer": user_ans,
                "Result": "✅ Correct" if is_correct else "❌ Incorrect",
                "Correct answer": correct_ans
            }
        )

    # Display score with feedback
    if (6 <= score < 9):
        st.success(f"Quiz Completed. Your Score is: {score}/{total_q} 🙂")
    elif score <= 6:
        st.warning(f"Quiz Completed. Your Score is: {score}/{total_q} 🫢")
    elif score >= 9:
        st.success(f"Quiz Completed. Your Score is: {score}/{total_q} 🥳")
        st.balloons()

    # Show detailed review of answers
    st.write("### Reviews 🔍")
    pd.DataFrame(result)
    st.dataframe(result)

    # Option to restart the quiz
    st.button("Restart Quiz 🔄", on_click = restart_quiz, type = "primary")
