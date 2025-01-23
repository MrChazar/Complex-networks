import asyncio

from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware
import services.WordTransform as Wf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "localhost"],
    allow_credentials=True,
    allow_methods=["*"],  # Zezwól na wszystkie metody (GET, POST, itp.)
    allow_headers=["*"],  # Zezwól na wszystkie nagłówki
)

@app.get("/get-name")
def get_name():
    return {"name": "dupa"}

# Asynchroniczny endpoint
@app.post("/trend/word-cloud")
async def get_text_for_wordcloud(
    tag_name: str = Query(..., description="Nazwa tagu do analizy"),
    number_of_pages: int = Query(..., description="Liczba stron do przetworzenia")
):
    # Opakowanie synchronicznej funkcji w asyncio.to_thread, aby nie blokować event loop
    data = await asyncio.to_thread(Wf.generate_text_for_wordcloud, tag_name, number_of_pages)
    return data

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)