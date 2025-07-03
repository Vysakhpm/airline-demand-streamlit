# gpt_summary.py
import openai
import os

def generate_summary(top_countries, avg_velocity):
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
        Analyze the following airline flight data and generate a brief trend summary:

        Top countries by flight count: {top_countries}
        Top countries by average velocity: {avg_velocity}

        Keep it short (2–3 sentences) and professional.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=120
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error generating summary: {str(e)}"
