import streamlit as st
import random
import time
import json
import os

word_pairs = [
  {
    "german_word": "Start",
    "english_word": "start"
  },
  {
    "german_word": "auf",
    "english_word": "on"
  },
  {
    "german_word": "Deutsch",
    "english_word": "German"
  },
  {
    "german_word": "hier",
    "english_word": "here"
  },
  {
    "german_word": "lernen",
    "english_word": "learn"
  },
  {
    "german_word": "Sie",
    "english_word": "you"
  },
  {
    "german_word": "international",
    "english_word": "international"
  },
  {
    "german_word": "Wort",
    "english_word": "word"
  },
  {
    "german_word": "verstehen",
    "english_word": "understand"
  },
  {
    "german_word": "begrüßen",
    "english_word": "greet"
  },
  {
    "german_word": "vorstellen",
    "english_word": "introduce"
  },
  {
    "german_word": "und",
    "english_word": "and"
  },
  {
    "german_word": "anderer",
    "english_word": "other(s)"
  },
  {
    "german_word": "fragen",
    "english_word": "ask"
  },
  {
    "german_word": "Name",
    "english_word": "name"
  },
  {
    "german_word": "Herkunft",
    "english_word": "origins"
  },
  {
    "german_word": "Alphabet",
    "english_word": "alphabet"
  },
  {
    "german_word": "buchstabieren",
    "english_word": "spell"
  },
  {
    "german_word": "sehen",
    "english_word": "see"
  },
  {
    "german_word": "hören",
    "english_word": "hear"
  },
  {
    "german_word": "Bild",
    "english_word": "picture"
  },
  {
    "german_word": "was",
    "english_word": "what"
  },
  {
    "german_word": "zusammengehören",
    "english_word": "belong together"
  },
  {
    "german_word": "Musik",
    "english_word": "music"
  },
  {
    "german_word": "Tourist",
    "english_word": "tourist"
  },
  {
    "german_word": "Büro",
    "english_word": "office"
  },
  {
    "german_word": "Supermarkt",
    "english_word": "supermarket"
  },
  {
    "german_word": "Telefon",
    "english_word": "telephone"
  },
  {
    "german_word": "Kurs",
    "english_word": "course"
  },
  {
    "german_word": "Kaffee",
    "english_word": "coffee"
  },
  {
    "german_word": "Computer",
    "english_word": "computer"
  },
  {
    "german_word": "Cafeteria",
    "english_word": "cafeteria"
  },
  {
    "german_word": "Oper",
    "english_word": "opera"
  },
  {
    "german_word": "Espresso",
    "english_word": "espresso"
  },
  {
    "german_word": "Airbus",
    "english_word": "airbus"
  },
  {
    "german_word": "Euro",
    "english_word": "euro"
  },
  {
    "german_word": "Orchester",
    "english_word": "orchestra"
  },
  {
    "german_word": "Schule",
    "english_word": "school"
  },
  {
    "german_word": "wie",
    "english_word": "how"
  },
  {
    "german_word": "heißen",
    "english_word": "call"
  },
  {
    "german_word": "der",
    "english_word": "the"
  },
  {
    "german_word": "in",
    "english_word": "in"
  },
  {
    "german_word": "Ihr",
    "english_word": "your"
  },
  {
    "german_word": "Sprache",
    "english_word": "language"
  },
  {
    "german_word": "Ton",
    "english_word": "sound"
  },
  {
    "german_word": "wo",
    "english_word": "where"
  },
  {
    "german_word": "ist",
    "english_word": "is"
  },
  {
    "german_word": "kennen",
    "english_word": "know"
  },
  {
    "german_word": "Sprecher",
    "english_word": "speaker"
  },
  {
    "german_word": "kommen",
    "english_word": "come"
  },
  {
    "german_word": "aus",
    "english_word": "from"
  },
  {
    "german_word": "Frage",
    "english_word": "question"
  },
  {
    "german_word": "Antwort",
    "english_word": "answer"
  },
  {
    "german_word": "nachsprechen",
    "english_word": "repeat"
  },
  {
    "german_word": "Partnerinterview",
    "english_word": "interviewing"
  },
  {
    "german_word": "Partner/in",
    "english_word": "partner"
  },
  {
    "german_word": "fragen",
    "english_word": "ask"
  },
  {
    "german_word": "notieren",
    "english_word": "notes"
  },
  {
    "german_word": "berichten",
    "english_word": "report"
  },
  {
    "german_word": "lesen",
    "english_word": "read"
  },
  {
    "german_word": "wohnen",
    "english_word": "live"
  },
  {
    "german_word": "jetzt",
    "english_word": "now"
  },
  {
    "german_word": "auch",
    "english_word": "also"
  },
  {
    "german_word": "zuordnen",
    "english_word": "match"
  },
  {
    "german_word": "Personalangabe",
    "english_word": "information"
  },
  {
    "german_word": "im",
    "english_word": "in"
  },
  {
    "german_word": "Dialog",
    "english_word": "dialogue"
  },
  {
    "german_word": "Guten Tag!",
    "english_word": "Hello!"
  },
  {
    "german_word": "ich",
    "english_word": "I"
  },
  {
    "german_word": "bin",
    "english_word": "am"
  },
  {
    "german_word": "Frau",
    "english_word": "Mrs."
  },
  {
    "german_word": "Deutschlehrer/in",
    "english_word": "teacher"
  },
  {
    "german_word": "Lehrer/in",
    "english_word": "teacher"
  },
  {
    "german_word": "Hallo!",
    "english_word": "Hello!"
  },
  {
    "german_word": "mein",
    "english_word": "my"
  },
  {
    "german_word": "woher",
    "english_word": "from"
  },
  {
    "german_word": "wer",
    "english_word": "who"
  },
  {
    "german_word": "Herr",
    "english_word": "Mr."
  },
  {
    "german_word": "er",
    "english_word": "he"
  },
  {
    "german_word": "ein",
    "english_word": "a"
  },
  {
    "german_word": "Person",
    "english_word": "person"
  },
  {
    "german_word": "Aufgabe",
    "english_word": "task"
  },
  {
    "german_word": "ergänzen",
    "english_word": "complete"
  },
  {
    "german_word": "Redemittelkasten",
    "english_word": "box"
  },
  {
    "german_word": "Redemittel",
    "english_word": "expression"
  },
  {
    "german_word": "mit",
    "english_word": "with"
  },
  {
    "german_word": "Begrüßung",
    "english_word": "greeting"
  },
  {
    "german_word": "Vorstellung",
    "english_word": "introduction"
  },
  {
    "german_word": "vorher",
    "english_word": "before"
  },
  {
    "german_word": "war",
    "english_word": "was"
  },
  {
    "german_word": "für",
    "english_word": "for"
  },
  {
    "german_word": "Elektronikingenieur/in",
    "english_word": "engineer"
  },
  {
    "german_word": "Spezialität",
    "english_word": "specialty"
  },
  {
    "german_word": "Medizintechnologie",
    "english_word": "technology"
  },
  {
    "german_word": "Französisch",
    "english_word": "French"
  },
  {
    "german_word": "Chinesisch",
    "english_word": "Chinese"
  },
  {
    "german_word": "Skifahren",
    "english_word": "skiing"
  },
  {
    "german_word": "leben",
    "english_word": "live"
  },
  {
    "german_word": "Musiker/in",
    "english_word": "musician"
  },
  {
    "german_word": "spielen",
    "english_word": "play"
  },
  {
    "german_word": "Violine",
    "english_word": "violin"
  },
  {
    "german_word": "Symbol",
    "english_word": "symbol"
  },
  {
    "german_word": "Dynamik",
    "english_word": "dynamic(s)"
  },
  {
    "german_word": "Internationalität",
    "english_word": "internationality"
  },
  {
    "german_word": "Bank",
    "english_word": "bank"
  },
  {
    "german_word": "Basis",
    "english_word": "base"
  },
  {
    "german_word": "Heimat",
    "english_word": "land"
  },
  {
    "german_word": "Ufer",
    "english_word": "bank"
  },
  {
    "german_word": "Skaterparadies",
    "english_word": "paradise"
  },
  {
    "german_word": "dort",
    "english_word": "there"
  },
  {
    "german_word": "es",
    "english_word": "it"
  },
  {
    "german_word": "geben",
    "english_word": "give"
  },
  {
    "german_word": "Museum",
    "english_word": "museum"
  },
  {
    "german_word": "Vorname",
    "english_word": "name"
  },
  {
    "german_word": "Junge",
    "english_word": "boy"
  },
  {
    "german_word": "Mädchen",
    "english_word": "girl"
  },
  {
    "german_word": "noch einmal",
    "english_word": "again"
  },
  {
    "german_word": "Favorit",
    "english_word": "favourite"
  },
  {
    "german_word": "schnell",
    "english_word": "fast"
  },
  {
    "german_word": "Text",
    "english_word": "text"
  },
  {
    "german_word": "passen",
    "english_word": "fit"
  },
  {
    "german_word": "studieren",
    "english_word": "study"
  },
  {
    "german_word": "Hobby",
    "english_word": "hobby"
  },
  {
    "german_word": "Universität",
    "english_word": "university"
  },
  {
    "german_word": "Familie",
    "english_word": "family"
  },
  {
    "german_word": "Städtediktat",
    "english_word": "dictation"
  },
  {
    "german_word": "Stadt",
    "english_word": "city"
  },
  {
    "german_word": "Städtename",
    "english_word": "name"
  },
  {
    "german_word": "Abkürzung",
    "english_word": "abbreviation"
  },
  {
    "german_word": "Transport",
    "english_word": "transport"
  },
  {
    "german_word": "Auto",
    "english_word": "car"
  },
  {
    "german_word": "TV",
    "english_word": "TV"
  },
  {
    "german_word": "Spiel",
    "english_word": "game"
  },
  {
    "german_word": "Familienname",
    "english_word": "name"
  },
  {
    "german_word": "bei",
    "english_word": "by"
  },
  {
    "german_word": "welcher",
    "english_word": "which"
  },
  {
    "german_word": "Silbe",
    "english_word": "syllable"
  },
  {
    "german_word": "betonen",
    "english_word": "stress"
  },
  {
    "german_word": "ordnen",
    "english_word": "order"
  },
  {
    "german_word": "Geografie",
    "english_word": "geography"
  },
  {
    "german_word": "Tourismus",
    "english_word": "tourism"
  },
  {
    "german_word": "Zeitung",
    "english_word": "newspaper"
  },
  {
    "german_word": "Collage",
    "english_word": "collage"
  },
  {
    "german_word": "machen",
    "english_word": "make"
  },
  {
    "german_word": "global",
    "english_word": "global"
  },
  {
    "german_word": "Marktplatz",
    "english_word": "marketplace"
  },
  {
    "german_word": "Einwohner/in",
    "english_word": "resident"
  },
  {
    "german_word": "Flair",
    "english_word": "flair"
  },
  {
    "german_word": "Minimetropole",
    "english_word": "city"
  },
  {
    "german_word": "Prozent",
    "english_word": "percent"
  },
  {
    "german_word": "Ausland",
    "english_word": "abroad"
  },
  {
    "german_word": "Skyline",
    "english_word": "skyline"
  },
  {
    "german_word": "dann",
    "english_word": "then"
  },
  {
    "german_word": "zurück",
    "english_word": "back"
  },
  {
    "german_word": "sprechen",
    "english_word": "speak"
  },
  {
    "german_word": "Englisch",
    "english_word": "English"
  },
  {
    "german_word": "Student/in",
    "english_word": "student"
  },
  {
    "german_word": "Kommunikation",
    "english_word": "communication(s)"
  },
  {
    "german_word": "interkulturell",
    "english_word": "inter-cultural"
  },
  {
    "german_word": "Semester",
    "english_word": "semester"
  },
  {
    "german_word": "Freund/in",
    "english_word": "friend"
  },
  {
    "german_word": "Polnisch",
    "english_word": "Polish"
  },
  {
    "german_word": "Russisch",
    "english_word": "Russian"
  },
  {
    "german_word": "ein bisschen",
    "english_word": "bit"
  },
  {
    "german_word": "seit",
    "english_word": "since"
  },
  {
    "german_word": "Spanisch",
    "english_word": "Spanish"
  },
  {
    "german_word": "Job",
    "english_word": "job"
  },
  {
    "german_word": "suchen",
    "english_word": "search"
  },
  {
    "german_word": "Jahr",
    "english_word": "year"
  },
  {
    "german_word": "alt",
    "english_word": "old"
  },
  {
    "german_word": "sein",
    "english_word": "his"
  },
  {
    "german_word": "Minute",
    "english_word": "minute"
  },
  {
    "german_word": "am",
    "english_word": "at"
  },
  {
    "german_word": "Pilot/in",
    "english_word": "pilot"
  },
  {
    "german_word": "mögen",
    "english_word": "like"
  },
  {
    "german_word": "fliegen",
    "english_word": "fly"
  },
  {
    "german_word": "heute",
    "english_word": "today"
  },
  {
    "german_word": "von ... nach",
    "english_word": "from"
  },
  {
    "german_word": "nach",
    "english_word": "to"
  },
  {
    "german_word": "gehören",
    "english_word": "belong"
  },
  {
    "german_word": "Ensemble",
    "english_word": "ensemble"
  },
  {
    "german_word": "finden",
    "english_word": "find"
  },
  {
    "german_word": "fantastisch",
    "english_word": "fantastic"
  },
  {
    "german_word": "Mensch",
    "english_word": "person"
  },
  {
    "german_word": "Restaurant",
    "english_word": "restaurant"
  },
  {
    "german_word": "Atmosphäre",
    "english_word": "atmosphere"
  },
  {
    "german_word": "Sommer",
    "english_word": "summer"
  },
  {
    "german_word": "Café",
    "english_word": "café"
  },
  {
    "german_word": "haben",
    "english_word": "have"
  },
  {
    "german_word": "Konzert",
    "english_word": "concert"
  },
  {
    "german_word": "auswählen",
    "english_word": "choose"
  },
  {
    "german_word": "sortieren",
    "english_word": "sort"
  },
  {
    "german_word": "Technik",
    "english_word": "technique"
  }
]

def load_word_pairs():
    return word_pairs

def initialize_game():
    """Initialize game state"""
    if 'game_initialized' not in st.session_state:
        word_pairs = load_word_pairs()
        
        st.session_state.game_initialized = True
        st.session_state.selected_word = None
        st.session_state.selected_type = None
        st.session_state.matched_pairs = set()
        st.session_state.flash_message = ""
        st.session_state.flash_type = ""

        # Randomly pick 5 word pairs and assign IDs
        selected_pairs = random.sample(word_pairs, min(5, len(word_pairs)))
        for idx, pair in enumerate(selected_pairs):
            pair["id"] = str(idx)  # assign unique ID as string

        st.session_state.word_pairs = selected_pairs  # store the subset
        
        # Shuffle the displayed word lists
        english_words = [(pair["id"], pair["english_word"]) for pair in selected_pairs]
        german_words = [(pair["id"], pair["german_word"]) for pair in selected_pairs]
        random.shuffle(english_words)
        random.shuffle(german_words)
        
        st.session_state.english_words = english_words
        st.session_state.german_words = german_words

def reset_game():
    """Reset the game"""
    st.session_state.clear()
    initialize_game()

def handle_word_click(word_id, word_text, word_type):
    """Handle clicking on a word with enforced selection order"""
    if word_id in st.session_state.matched_pairs:
        return  # Already matched
    
    if st.session_state.selected_word is None:
        # First selection - must be from English column
        if word_type != "english":
            st.session_state.flash_message = "❌ Please select from English column first!"
            st.session_state.flash_type = "error"
            return
        
        st.session_state.selected_word = word_id
        st.session_state.selected_type = word_type
        st.session_state.flash_message = f"Selected: {word_text}. Now select the German translation."
        st.session_state.flash_type = "info"
    else:
        # Second selection - must be from German column
        if word_type != "german":
            st.session_state.flash_message = "❌ Please select from German column to complete the match!"
            st.session_state.flash_type = "error"
            return
        
        if st.session_state.selected_word == word_id:
            # Correct match!
            st.session_state.matched_pairs.add(word_id)
            st.session_state.flash_message = f"✅ Correct match!"
            st.session_state.flash_type = "success"
            st.session_state.selected_word = None
            st.session_state.selected_type = None
            # Force UI refresh to show matched buttons immediately
            st.rerun()
        else:
            # Wrong match
            st.session_state.flash_message = "❌ Wrong match! Try again."
            st.session_state.flash_type = "error"
            st.session_state.selected_word = None
            st.session_state.selected_type = None

# Set page config at the top level
st.set_page_config(
    page_title="Dollar Store Duolingo",
    page_icon="🎯",
    layout="wide"
)

def main():
    # Custom CSS with mobile responsiveness
    st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        margin: 5px 0;
        transition: all 0.3s;
        position: relative;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .stButton > button {
            height: 50px;
            font-size: 14px;
        }
        
        .game-title {
            font-size: 1.8rem !important;
        }
        
        .stColumns {
            gap: 0.5rem;
        }
    }
    
    .selected-button {
        background-color: #ff6b6b !important;
        color: white !important;
        border: 2px solid #ff5252 !important;
    }
    
    .matched-button {
        background-color: #4caf50 !important;
        color: white !important;
        opacity: 0.7;
    }
    
    .match-display {
        background-color: #e8f5e8;
        border-left: 4px solid #4caf50;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        font-size: 14px;
    }
    
    .game-title {
        text-align: center;
        color: #2e7d32;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    
    .instruction-box {
        background-color: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
        font-size: 14px;
    }
    
    .progress-bar {
        background-color: #e0e0e0;
        border-radius: 10px;
        height: 20px;
        margin: 10px 0;
    }
    
    .progress-fill {
        background-color: #4caf50;
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    .game-container {
        position: relative;
    }
    
    .connection-line {
        position: absolute;
        height: 2px;
        background: linear-gradient(90deg, #4caf50, #66bb6a);
        z-index: 1000;
        border-radius: 1px;
        animation: drawLine 0.5s ease-in-out;
    }
    
    @keyframes drawLine {
        from {
            width: 0%;
        }
        to {
            width: 100%;
        }
    }
    
    .word-button {
        position: relative;
        z-index: 1001;
    }
    
    /* Add connecting dots */
    .connection-line::before,
    .connection-line::after {
        content: '';
        position: absolute;
        width: 8px;
        height: 8px;
        background-color: #4caf50;
        border-radius: 50%;
        top: -3px;
    }
    
    .connection-line::before {
        left: -4px;
    }
    
    .connection-line::after {
        right: -4px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    initialize_game()
    
    st.markdown('<h1 class="game-title">Dollar Store Duolingo by Anil</h1>', unsafe_allow_html=True)
    
    # Instructions
    st.markdown('''
    <div class="instruction-box">
        <strong>📝 How to play:</strong><br>
        1. Select a word from the English column first<br>
        2. Then select its German translation from the German column<br>
        3. Game will auto-reset when you complete all matches!
    </div>
    ''', unsafe_allow_html=True)
    
    # Progress bar - only show if game is initialized
    if hasattr(st.session_state, 'word_pairs') and hasattr(st.session_state, 'matched_pairs'):
        progress = len(st.session_state.matched_pairs) / len(st.session_state.word_pairs) * 100
        st.markdown(f'''
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress}%"></div>
        </div>
        <p style="text-align: center; margin: 5px 0;">Progress: {len(st.session_state.matched_pairs)}/{len(st.session_state.word_pairs)} matches</p>
        ''', unsafe_allow_html=True)
    
    # Flash messages
    if hasattr(st.session_state, 'flash_message') and st.session_state.flash_message:
        if st.session_state.flash_type == "success":
            st.success(st.session_state.flash_message)
        elif st.session_state.flash_type == "error":
            st.error(st.session_state.flash_message)
        else:
            st.info(st.session_state.flash_message)
    
    # Game area - only show if initialized
    if not hasattr(st.session_state, 'english_words') or not hasattr(st.session_state, 'german_words'):
        st.error("Game not properly initialized. Please refresh the page.")
        return
    
    # Create a container for the game with connection lines
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🇺🇸 English (Select First)")
        for idx, (word_id, word_text) in enumerate(st.session_state.english_words):
            is_selected = (st.session_state.selected_word == word_id and 
                          st.session_state.selected_type == "english")
            is_matched = word_id in st.session_state.matched_pairs
            
            button_key = f"en_{word_id}"
            
            if is_matched:
                st.button(f"✅ {word_text}", key=button_key, disabled=True)
            else:
                button_text = f"▶ {word_text} ◀" if is_selected else word_text
                if st.button(button_text, key=button_key):
                    handle_word_click(word_id, word_text, "english")
    
    with col2:
        st.subheader("🇩🇪 German (Select Second)")
        for idx, (word_id, word_text) in enumerate(st.session_state.german_words):
            is_selected = (st.session_state.selected_word == word_id and 
                          st.session_state.selected_type == "german")
            is_matched = word_id in st.session_state.matched_pairs
            
            button_key = f"de_{word_id}"
            
            if is_matched:
                st.button(f"✅ {word_text}", key=button_key, disabled=True)
            else:
                button_text = f"▶ {word_text} ◀" if is_selected else word_text
                # Disable German buttons if no English word is selected
                disabled = not hasattr(st.session_state, 'selected_word') or st.session_state.selected_word is None
                if st.button(button_text, key=button_key, disabled=disabled):
                    handle_word_click(word_id, word_text, "german")
    
    # Add connection lines for matched pairs
    if hasattr(st.session_state, 'matched_pairs') and st.session_state.matched_pairs:
        connection_lines = []
        for word_id in st.session_state.matched_pairs:
            # Find positions of matched words
            english_pos = next((i for i, (id, _) in enumerate(st.session_state.english_words) if id == word_id), -1)
            german_pos = next((i for i, (id, _) in enumerate(st.session_state.german_words) if id == word_id), -1)
            
            if english_pos != -1 and german_pos != -1:
                # Calculate line position (approximate)
                line_top = 150 + (english_pos * 70) + 30  # Adjust based on button height and spacing
                connection_lines.append(f"""
                    <div class="connection-line" style="
                        top: {line_top}px;
                        left: 50%;
                        width: 50%;
                        transform: translateX(-50%);
                    "></div>
                """)
        
        # Add all connection lines
        st.markdown(''.join(connection_lines), unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Matches display
    if hasattr(st.session_state, 'matched_pairs') and st.session_state.matched_pairs:
        st.subheader("🎉 Matches")
        for word_id in sorted(st.session_state.matched_pairs):
            # Find the matching pair from session state
            english_word = next(pair["english_word"] for pair in st.session_state.word_pairs if pair["id"] == word_id)
            german_word = next(pair["german_word"] for pair in st.session_state.word_pairs if pair["id"] == word_id)
            
            st.markdown(f'<div class="match-display">✓ {english_word} ↔ {german_word}</div>', 
                       unsafe_allow_html=True)
    
    # Check if game is complete
    if (hasattr(st.session_state, 'matched_pairs') and hasattr(st.session_state, 'word_pairs') and 
        len(st.session_state.matched_pairs) == len(st.session_state.word_pairs)):
        st.balloons()
        st.success("🎉 Congratulations! You matched all words! 🎉")
        st.info("🔄 Starting a new game in 3 seconds...")
        
        # Auto-reset after 3 seconds
        time.sleep(3)
        reset_game()
        st.rerun()
    
    # Manual reset button
    st.divider()
    if st.button("🔄 Reset Game", type="secondary"):
        reset_game()
        st.rerun()

# Run the main function
if __name__ == "__main__":
    main()