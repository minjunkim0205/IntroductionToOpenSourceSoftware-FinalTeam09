# module/gemini.py

# ---------------------------------------------------
# Import module
# ---------------------------------------------------
from google import genai
from google.genai import types

# ---------------------------------------------------
# Function
# ---------------------------------------------------
def api_check(_key: str) -> bool:
    client = genai.Client(api_key=_key)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                # 반드시 영어로 대답 해야합니다.
                system_instruction="You must answer in English."
            ),
            # 핑
            contents="ping"
        )
        print(response.text)
        return True
    except Exception as e:
        # print(e)
        return False

# ---------------------------------------------------
# Test
# ---------------------------------------------------
if __name__ == "__main__":
    key = str(input("Your Gemini API Key >> "))
    if api_check(key):
        print("Success", end="")
    else:
        print("Error", end="")
