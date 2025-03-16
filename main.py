import re
import random
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Blacklist of common weak passwords
    common_passwords = {"password", "123456", "qwerty", "abc123", "password123", "letmein"}
    if password.lower() in common_passwords:
        return "❌ Weak Password - This password is too common. Choose a unique one."
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.\n" + "\n".join(feedback)
    else:
        return "❌ Weak Password - Improve it using the suggestions below:\n" + "\n".join(feedback)

def generate_strong_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")
if password:
    result = check_password_strength(password)
    st.write(result)

    if "Weak" in result:
        if st.button("Generate Strong Password"):
            st.write("💡 Suggested Strong Password:", generate_strong_password())
