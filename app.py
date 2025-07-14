import streamlit as st
import random

# Your German quiz data
quiz_data = [
    {
        "german_sentence": "Ich sehe _________ Ball.",
        "options": ["den", "dem", "der", "das", "die"],
        "correct_option": "den",
        "case": "Accusative",
        "english_translation": "I see the ball."
    },
    {
        "german_sentence": "Er hilft _________ Frau.",
        "options": ["der", "die", "dem", "den", "das"],
        "correct_option": "der",
        "case": "Dative",
        "english_translation": "He helps the woman."
    },
    {
        "german_sentence": "_________ Kind spielt im Garten.",
        "options": ["Das", "Dem", "Den", "Die", "Der"],
        "correct_option": "Das",
        "case": "Nominative",
        "english_translation": "The child is playing in the garden."
    },
    {
        "german_sentence": "Sie ruft _________ Bruder an.",
        "options": ["den", "dem", "der", "die", "das"],
        "correct_option": "den",
        "case": "Accusative",
        "english_translation": "She calls her brother."
    },
    {
        "german_sentence": "Wir geben _________ Mädchen ein Geschenk.",
        "options": ["dem", "den", "die", "das", "der"],
        "correct_option": "dem",
        "case": "Dative",
        "english_translation": "We give the girl a gift."
    },
    {
        "german_sentence": "_________ Lehrer erklärt die Aufgabe.",
        "options": ["Der", "Den", "Dem", "Das", "Die"],
        "correct_option": "Der",
        "case": "Nominative",
        "english_translation": "The teacher explains the task."
    },
    {
        "german_sentence": "Er besucht _________ Eltern oft.",
        "options": ["die", "der", "den", "das", "dem"],
        "correct_option": "die",
        "case": "Accusative",
        "english_translation": "He visits the parents often."
    },
    {
        "german_sentence": "Ich danke _________ Mann für die Hilfe.",
        "options": ["dem", "den", "der", "die", "das"],
        "correct_option": "dem",
        "case": "Dative",
        "english_translation": "I thank the man for the help."
    },
    {
        "german_sentence": "Sie bringt _________ Hund ins Haus.",
        "options": ["den", "dem", "der", "die", "das"],
        "correct_option": "den",
        "case": "Accusative",
        "english_translation": "She brings the dog into the house."
    },
    {
        "german_sentence": "_________ Auto ist rot.",
        "options": ["Das", "Den", "Dem", "Der", "Die"],
        "correct_option": "Das",
        "case": "Nominative",
        "english_translation": "The car is red."
    },
    {
        "german_sentence": "Wir helfen _________ Kindern mit den Hausaufgaben.",
        "options": ["den", "die", "dem", "der", "das"],
        "correct_option": "den",
        "case": "Dative",
        "english_translation": "We help the children with the homework."
    },
    {
        "german_sentence": "Sie kauft _________ Apfel.",
        "options": ["den", "dem", "der", "die", "das"],
        "correct_option": "den",
        "case": "Accusative",
        "english_translation": "She buys the apple."
    },
    {
        "german_sentence": "_________ Mädchen singt schön.",
        "options": ["Das", "Der", "Dem", "Den", "Die"],
        "correct_option": "Das",
        "case": "Nominative",
        "english_translation": "The girl sings beautifully."
    },
    {
        "german_sentence": "Ich vertraue _________ Freund.",
        "options": ["dem", "den", "der", "das", "die"],
        "correct_option": "dem",
        "case": "Dative",
        "english_translation": "I trust the friend."
    },
    {
        "german_sentence": "Sie hört _________ Musik jeden Tag.",
        "options": ["die", "der", "den", "dem", "das"],
        "correct_option": "die",
        "case": "Accusative",
        "english_translation": "She listens to music every day."
    },
    {
        "german_sentence": "_________ Mann ist müde.",
        "options": ["Der", "Den", "Dem", "Die", "Das"],
        "correct_option": "Der",
        "case": "Nominative",
        "english_translation": "The man is tired."
    },
    {
        "german_sentence": "Ich schicke _________ Frau eine E-Mail.",
        "options": ["der", "die", "dem", "das", "den"],
        "correct_option": "der",
        "case": "Dative",
        "english_translation": "I send the woman an email."
    },
    {
        "german_sentence": "Er liebt _________ Katze.",
        "options": ["die", "der", "das", "dem", "den"],
        "correct_option": "die",
        "case": "Accusative",
        "english_translation": "He loves the cat."
    },
    {
        "german_sentence": "_________ Kinder spielen draußen.",
        "options": ["Die", "Der", "Dem", "Den", "Das"],
        "correct_option": "Die",
        "case": "Nominative",
        "english_translation": "The children are playing outside."
    },
    {
        "german_sentence": "Wir gratulieren _________ Lehrer zum Erfolg.",
        "options": ["dem", "der", "den", "die", "das"],
        "correct_option": "dem",
        "case": "Dative",
        "english_translation": "We congratulate the teacher on the success."
    }
]

# Set page config first
st.set_page_config(
    page_title="Dollar Store Duolingo", 
    page_icon="💡",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
<style>
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container styling */
    .main > div {
        display: flex;
        justify-content: center;
        padding: 2rem 1rem;
    }

    .app-container {
        max-width: 650px;
        width: 100%;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        padding: 2rem;
    }

    /* Title styling */
    .main h1 {
        text-align: center !important;
        color: #1f2937 !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 2rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1) !important;
    }

    /* Common styling for both translation and German sentence */
    .translation, .german-sentence {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
        text-align: center;
        box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        min-height: 1.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Button container */
    .button-container {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
        margin-bottom: 2rem;
    }

    /* Button styling */
    .stButton > button {
        width: 100% !important;
        padding: 0.8rem 1.2rem !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        border: 2px solid #e5e7eb !important;
        background: white !important;
        color: #374151 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
    }

    .stButton > button:hover {
        background: #f9fafb !important;
        border-color: #3b82f6 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
    }

    /* Correct answer button */
    .option.correct .stButton > button {
        background: linear-gradient(135deg, #10b981, #059669) !important;
        color: white !important;
        border-color: #10b981 !important;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3) !important;
    }

    /* Wrong answer button */
    .option.wrong .stButton > button {
        background: linear-gradient(135deg, #ef4444, #dc2626) !important;
        color: white !important;
        border-color: #ef4444 !important;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3) !important;
    }

    /* Next button styling */
    .next-button .stButton > button {
        background: linear-gradient(135deg, #8b5cf6, #7c3aed) !important;
        color: white !important;
        border-color: #8b5cf6 !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
        padding: 1rem 2rem !important;
        box-shadow: 0 4px 16px rgba(139, 92, 246, 0.4) !important;
    }

    .next-button .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5) !important;
    }

    /* Success message styling */
    .success-message {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
        font-size: 1.1rem;
        margin: 1rem 0;
        box-shadow: 0 3px 10px rgba(16, 185, 129, 0.3);
    }

    /* Spacer */
    .spacer {
        height: 1rem;
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .app-container {
            padding: 1.5rem;
            margin: 1rem;
        }
        
        .main h1 {
            font-size: 2rem !important;
        }
        
        .translation, .german-sentence {
            font-size: 1.1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- State Management ---
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(quiz_data)
if "incorrect_guesses" not in st.session_state:
    st.session_state.incorrect_guesses = set()
if "answered_correctly" not in st.session_state:
    st.session_state.answered_correctly = False

question = st.session_state.current_question
sentence = question["german_sentence"]
options = question["options"]
correct = question["correct_option"]
translation = question["english_translation"]

st.title("ಮಾತು ಕಲಿಕೆ by Anil")

# Begin centered content
#st.markdown("<div class='app-container'>", unsafe_allow_html=True)

# Display translation
st.markdown(f"<div class='translation'>{translation}</div>", unsafe_allow_html=True)

# Display German sentence
st.markdown(f"<div class='german-sentence'>{sentence}</div>", unsafe_allow_html=True)

# Button container
st.markdown("<div class='button-container'>", unsafe_allow_html=True)

# Render option buttons
for opt in options:
    if opt in st.session_state.incorrect_guesses:
        # Wrong answer - show with X
        st.markdown("<div class='option wrong'>", unsafe_allow_html=True)
        st.button(f"✖️ {opt}", key=f"wrong_{opt}", disabled=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    elif st.session_state.answered_correctly:
        # Question answered - show correct answer with checkmark
        if opt == correct:
            st.markdown("<div class='option correct'>", unsafe_allow_html=True)
            st.button(f"✔️ {opt}", key=f"correct_{opt}", disabled=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='option'>", unsafe_allow_html=True)
            st.button(opt, key=f"done_{opt}", disabled=True)
            st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        # Active button - clickable
        st.markdown("<div class='option'>", unsafe_allow_html=True)
        clicked = st.button(opt, key=opt)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Handle button clicks outside the callback
        if clicked:
            if opt == correct:
                st.session_state.answered_correctly = True
                st.balloons()
                st.rerun()
            else:
                st.session_state.incorrect_guesses.add(opt)
                st.rerun()

#st.markdown("</div>", unsafe_allow_html=True)  # End button container

# Show success message and next button when answered correctly
if st.session_state.answered_correctly:
    st.markdown("<div class='success-message'>🎉 Richtig! Correct! 🎉</div>", unsafe_allow_html=True)
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("<div class='next-button'>", unsafe_allow_html=True)
    
    # Handle next button click
    if st.button("🔁 Nächste Frage / Next Question"):
        st.session_state.current_question = random.choice(quiz_data)
        st.session_state.incorrect_guesses = set()
        st.session_state.answered_correctly = False
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# End centered container
st.markdown("</div>", unsafe_allow_html=True)