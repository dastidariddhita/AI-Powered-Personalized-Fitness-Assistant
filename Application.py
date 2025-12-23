# app.py
import streamlit as st
from datetime import date
import pandas as pd

# Import Groq client
try:
    from groq import Groq
    _HAS_GROQ = True
except Exception:
    _HAS_GROQ = False

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Fitness Assistant", page_icon="💪", layout="wide")

# ---------- HELPERS ----------
def detect_intent(text: str) -> str:
    """
    Return one of: 'nutrition', 'workout', or 'other'.
    Analyzes text (like an AI's response) to see if it's a plan
    by counting keywords.
    """
    text = (text or "").lower()
    
    # Added more specific keywords to improve accuracy
    workout_keywords = [
        'workout', 'exercise', 'gym', 'lift', 'hiit', 'cardio', 'strength', 
        'routine', 'sets', 'reps', 'weekly grid', 'day 1', 'mon -', 'tue -', 
        'wed -', 'thu -', 'fri -', 'sat -', 'sun -', 'push-up', 'squat', 
        'dumbbell', 'circuit', 'warm-up', 'cool-down'
    ]
    nutrition_keywords = [
        'diet', 'food', 'meal', 'nutrition', 'snack', 'calorie', 'protein', 
        'kcal', 'carb', 'recipe', 'breakfast', 'lunch', 'dinner', 'meal plan',
        'yogurt', 'chicken', 'quinoa', 'oats', 'macros'
    ]

    # --- NEW: Count the keywords ---
    workout_score = 0
    nutrition_score = 0

    for word in workout_keywords:
        if word in text:
            workout_score += 1
            
    for word in nutrition_keywords:
        if word in text:
            nutrition_score += 1

    # --- FIX: Return the category with the higher score ---
    # Only save if there's a clear winner (score > 0)
    if workout_score > nutrition_score and workout_score > 0:
        return 'workout'
    if nutrition_score > workout_score and nutrition_score > 0:
        return 'nutrition'
    
    # If scores are equal or zero, it's not a plan
    return 'other'

def get_system_prompt(profile: dict) -> str:
# ... (rest of your code is unchanged) ...
    """
    Creates a dynamic system prompt based on the user's profile.
    """
    return (
        "You are a helpful, expert fitness assistant. "
        "You MUST tailor your responses to the user's profile.\n"
        "Here is the user's profile:\n"
        f"- Name: {profile['name']}\n"
        f"- Age: {profile['age']}\n"
        f"- Sex: {profile['sex']}\n"
        f"- Main Goal: {profile['goal']}\n\n"
        "Your duties:\n"
        "1.  **Nutrition:** If asked for meal plans, provide them tailored to the user's goal (e.g., calorie deficit for 'Weight Loss').\n"
        "2.  **Workouts:** If asked for exercises, create plans suitable for their goal. Give structured plans (e.g., 'WEEKLY GRID', 'Day 1: ...', 'Sets/Reps: ...').\n"
        "3.  **Motivation:** If asked for motivation, provide concise, actionable tips.\n"
        "4.  **Medical:** If the user mentions pain, injury, or medical issues, "
        "   you MUST respond with a disclaimer: 'I am an AI, not a medical professional. "
        "   Please consult a healthcare professional for any medical advice or concerns.' Do NOT provide any diagnosis or treatment.\n"
        "5.  **Context:** Pay close attention to the chat history to understand follow-up questions."
    )

def call_model(api_key: str, system_prompt: str, messages: list) -> str:
    """
    Call the Groq model with the full conversation history.
    """
    if not api_key:
        return "⚠️ No API key provided. Please enter your Groq API key in the sidebar."
    if not _HAS_GROQ:
        return "⚠️ Groq client library not installed. Install `groq`."

    full_message_list = [{"role": "system", "content": system_prompt}] + messages
    
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="moonshotai/kimi-k2-instruct",
            messages=full_message_list,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error calling model: {e}"

# ---------- SIDEBAR ----------
st.sidebar.title("💪 Fitness AI")
st.sidebar.markdown("...")  # Your markdown link

api_key = st.secrets.get("GROQ_API_KEY")
if not api_key:
    st.sidebar.warning("GROQ_API_KEY not found in secrets.")
    api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password", key="local_api_key")

st.sidebar.markdown("---")
st.sidebar.header("Your Profile")
default_name = "Swastika"
name = st.sidebar.text_input("Name", value=default_name, key="profile_name")
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=20, key="profile_age")
sex = st.sidebar.selectbox("Sex", ["Female", "Male", "Other"], key="profile_sex")
goal = st.sidebar.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Endurance", "General Fitness"], key="profile_goal")
st.sidebar.write(f"🏁 Goal: **{goal}**")
st.sidebar.caption(f"App last updated: {date.today().strftime('%d %b %Y')}")
st.sidebar.markdown("---")
st.sidebar.write("Tip: Don't hardcode your API key. Use the sidebar or `secrets.toml`.")

# ---------- NAVIGATION ----------
page = st.sidebar.radio("Go to", ["Chat Assistant", "Dashboard"], index=0)

# ---------- SESSION STATE SETUP ----------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "workout_plans" not in st.session_state:
    st.session_state.workout_plans = []
if "meal_plans" not in st.session_state:
    st.session_state.meal_plans = []

# ---------- DASHBOARD PAGE ----------
if page == "Dashboard":
    st.title("📊 Fitness Dashboard")
    st.subheader("👤 Personal Info")
    col1, col2, col3 = st.columns(3)
    col1.metric("Name", name)
    col2.metric("Age", age)
    col3.metric("Sex", sex)

    st.subheader("My Generated Meal Plans")
    if not st.session_state.meal_plans:
        st.info("No meal plans generated yet. Go to the Chat Assistant to create one!")
    else:
        # Show newest plans first
        for i, plan in enumerate(reversed(st.session_state.meal_plans)):
            with st.expander(f"Meal Plan {len(st.session_state.meal_plans) - i}"):
                st.markdown(plan)
    
    st.subheader("My Generated Workout Plans")
    if not st.session_state.workout_plans:
        st.info("No workout plans generated yet. Go to the Chat Assistant to create one!")
    else:
        # Show newest plans first
        for i, plan in enumerate(reversed(st.session_state.workout_plans)):
            with st.expander(f"Workout Plan {len(st.session_state.workout_plans) - i}"):
                st.markdown(plan)

# ---------- CHAT PAGE ----------
elif page == "Chat Assistant":
    st.title("💬 Fitness Chat Assistant")

    if st.session_state.messages:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    user_input = st.chat_input("Ask me about workouts, meals, or motivation!", key="fitness_chat")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        profile_data = {"name": name, "age": age, "sex": sex, "goal": goal}
        system_prompt = get_system_prompt(profile_data)
        
        with st.chat_message("assistant"):
            with st.status("🤖 Generating response...", expanded=True) as status:
                model_reply = call_model(
                    api_key, 
                    system_prompt, 
                    st.session_state.messages
                )
                st.markdown(model_reply)
                status.update(label="Response generated!", state="complete")
        
        st.session_state.messages.append({"role": "assistant", "content": model_reply})

        # --- NEW: SAVE TO DASHBOARD ---
        # Analyze the AI's response to see if it's a plan
        response_intent = detect_intent(model_reply)
        
        if response_intent == 'workout':
            st.session_state.workout_plans.append(model_reply)
            st.toast("Workout plan saved to dashboard!")
        elif response_intent == 'nutrition':
            st.session_state.meal_plans.append(model_reply)
            st.toast("Meal plan saved to dashboard!")
        # -------------------------------

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built with ❤️ — edit the code to customize model, prompts, or UI.")
