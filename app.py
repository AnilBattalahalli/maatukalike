import streamlit as st
import random

# Your German quiz data
quiz_data = [
    {
        "german_sentence": "Ich _________ jeden Morgen Kaffee.",
        "verb_options": ["trinke", "essen", "spiele", "lesen", "schlafen"],
        "correct_verb": "trinke",
        "english_translation": "I drink coffee every morning."
    },
    {
        "german_sentence": "Sie _________ heute Abend ein Buch.",
        "verb_options": ["lesen", "schreiben", "hören", "sehen", "sprechen"],
        "correct_verb": "lesen",
        "english_translation": "She reads a book tonight."
    },
    {
        "german_sentence": "Wir _________ ins Kino am Wochenende.",
        "verb_options": ["gehen", "bleiben", "kommen", "fahren", "arbeiten"],
        "correct_verb": "gehen",
        "english_translation": "We go to the cinema on the weekend."
    },
    {
        "german_sentence": "Er _________ Deutsch sehr gut.",
        "verb_options": ["spricht", "lernt", "versteht", "schreibt", "hört"],
        "correct_verb": "spricht",
        "english_translation": "He speaks German very well."
    },
    {
        "german_sentence": "Du _________ müde nach der Arbeit.",
        "verb_options": ["bist", "hast", "seid", "sind", "ist"],
        "correct_verb": "bist",
        "english_translation": "You are tired after work."
    },
    {
        "german_sentence": "Die Kinder _________ im Garten.",
        "verb_options": ["spielen", "essen", "trinken", "schlafen", "malen"],
        "correct_verb": "spielen",
        "english_translation": "The children play in the garden."
    },
    {
        "german_sentence": "Ich _________ einen Apfel.",
        "verb_options": ["esse", "trinke", "kaufe", "verkaufe", "schneide"],
        "correct_verb": "esse",
        "english_translation": "I eat an apple."
    },
    {
        "german_sentence": "Sie _________ Musik.",
        "verb_options": ["hört", "sieht", "spricht", "liest", "schreibt"],
        "correct_verb": "hört",
        "english_translation": "She listens to music."
    },
    {
        "german_sentence": "Wir _________ in Berlin.",
        "verb_options": ["wohnen", "arbeiten", "besuchen", "fahren", "leben"],
        "correct_verb": "wohnen",
        "english_translation": "We live in Berlin."
    },
    {
        "german_sentence": "Er _________ ein Auto.",
        "verb_options": ["hat", "ist", "geht", "kommt", "macht"],
        "correct_verb": "hat",
        "english_translation": "He has a car."
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
options = question["verb_options"]
correct = question["correct_verb"]
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