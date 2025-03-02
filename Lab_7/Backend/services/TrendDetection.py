from wykop import WykopAPI
import services.WykopHandler as wh
from google import genai
from google.genai import types

api = WykopAPI("w55988974f3d3194b7dd98c7ab2c6765c2", "05f093e009943e9e9b911f2a8a9f1a00")
api.authenticate()
client = genai.Client(api_key="AIzaSyBVLiobdrNnyJT7zMN1HyLYa7bU52owuik")


def trend_detection(tag_name, number_of_pages, posts=None):
    if posts == None:
        posts = wh.get_posts_and_comments(tag_name, number_of_pages)
    posts = [f"Treść: {post[2]} data: {post[4]}" for post in posts]

    sys_instruct = """
    Jesteś analitykiem trendów na portalu społecznościowym. Twoim zadaniem jest analizować posty i komentarze użytkowników, aby wykryć najważniejsze trendy związane z danym tagiem (społecznością).

    Oto jak masz to zrobić:
    1. Analizuj treści postów i komentarzy, aby zidentyfikować powtarzające się tematy, słowa kluczowe i tagi.
    2. Jeśli w danych nie ma wyraźnych trendów, zwróć odpowiedź: "Brak trendów".
    3. Nie wymyślaj własnych tematów – opieraj się wyłącznie na dostarczonych danych.
    4. Każdy wpis lub komentarz ma format: "Początek: [treść] :Koniec". Znak "#" przed tekstem oznacza tag.

    Przykład:
    - Jeśli w danych często pojawia się tag "#rpa" i tematy związane z polityką, zwróć odpowiedź: "Główny trend: Dyskusje na temat polityki w RPA (#rpa)".
    - Jeśli w danych nie ma powtarzających się tematów, zwróć odpowiedź: "Brak trendów".

    Zwróc tylko 3 najbardziej poruszane tematy w formie zwięzłego podsumowania.
    1. Temat Jakiś data trwania: 23.02.2024 - 24.02.2024
    2. Temat inny data trwania: 22.02.2024 - 24.02.2024
    """

    text = ""
    for content in posts:
        text += "Poczatek:" + content + ":Koniec"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=text,
        config=types.GenerateContentConfig(
            max_output_tokens=500,
            temperature=0.1,
            system_instruction=sys_instruct
        )
    )

    return response.text

