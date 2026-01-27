# llm_utils.py
from openai import OpenAI
import os

client = OpenAI()  # Make sure your OPENAI_API_KEY is set in env

def generate_explanation(crop, conditions):
    """
    Generate AI explanation for a crop based on input conditions
    """
    prompt = f"""
    Crop: {crop}
    Conditions: {conditions}

    Explain why this crop is suitable under these conditions and give 2-3 actionable farming tips.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI explanation failed: {str(e)}"


