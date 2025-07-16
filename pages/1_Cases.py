import streamlit as st
import random
import json

# get current directory path
import os
current_dir = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(current_dir, 'learn_cases.json'), 'r') as f:
    quiz_data = json.load(f)


# Set page config first
st.set_page_config(
    page_title="ಮಾತು ಕಲಿಕೆ - Cases", 
    page_icon="📝",
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

    /* Button container - Fixed for horizontal layout */
    .button-container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: 0.5rem;
        justify-content: center;
        margin-bottom: 2rem;
    }

    /* Option container for proper inline display */
    .option {
        display: inline-block;
        margin: 0;
        flex: 0 0 auto;
    }

    /* Button styling */
    .stButton > button {
        width: auto !important;
        min-width: 100px;
        max-width: 200px;
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

    /* Wrong answer button - Greyed out */
    .option.wrong .stButton > button {
        background: #9ca3af !important;
        color: #6b7280 !important;
        border-color: #9ca3af !important;
        box-shadow: none !important;
        opacity: 0.6 !important;
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
        
        .button-container {
            flex-direction: column;
            align-items: center;
        }
        
        .option {
            width: 100%;
            margin-bottom: 0.5rem;
        }
        
        .stButton > button {
            width: 100% !important;
            max-width: none !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- State Management ---
if "current_question" not in st.session_state:
    question = random.choice(quiz_data)
    options = question["options"].copy()
    random.shuffle(options)
    question["options"] = options
    st.session_state.current_question = question
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

# Display translation
st.markdown(f"<div class='translation'>{translation}</div>", unsafe_allow_html=True)

# Display German sentence
st.markdown(f"<div class='german-sentence'>{sentence}</div>", unsafe_allow_html=True)

# Create columns for horizontal button layout
cols = st.columns(len(options))

# Render option buttons in columns
for i, opt in enumerate(options):
    with cols[i]:
        if opt in st.session_state.incorrect_guesses:
            # Wrong answer - show greyed out with X
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
            
            # Handle button clicks
            if clicked:
                if opt == correct:
                    st.session_state.answered_correctly = True
                    st.balloons()
                    st.rerun()
                else:
                    st.session_state.incorrect_guesses.add(opt)
                    st.rerun()

# Show success message and next button when answered correctly
if st.session_state.answered_correctly:
    st.markdown("<div class='success-message'>🎉 Richtig! Correct! 🎉</div>", unsafe_allow_html=True)
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("<div class='next-button'>", unsafe_allow_html=True)
    
    # Handle next button click
    if st.button("🔁 Nächste Frage / Next Question"):
        question = random.choice(quiz_data)
        options = question["options"].copy()
        random.shuffle(options)
        question["options"] = options
        st.session_state.current_question = question
        st.session_state.incorrect_guesses = set()
        st.session_state.answered_correctly = False
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)