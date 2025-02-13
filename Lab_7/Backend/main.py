import asyncio

from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware
import services.WordTransform as Wf
import services.TrendDetection as td
import services.TrendWord as tw

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Zezwól na wszystkie metody (GET, POST, itp.)
    allow_headers=["*"],  # Zezwól na wszystkie nagłówki
)



# Asynchroniczny endpoint dla stworzenia word cloud
@app.get("/trend/word-cloud")
async def get_text_for_wordcloud(tag_name: str = Query(..., description="Nazwa tagu do analizy"),
    number_of_pages: int = Query(..., description="Liczba stron do przetworzenia")
):
    data = await asyncio.to_thread(Wf.generate_text_for_wordcloud, tag_name, number_of_pages)
    return data


# Asynchroniczny endpoint dla wykrycia trendów przez gemini
@app.get("/trend/trend-detection")
async def trend_detection(tag_name: str = Query(..., description="Nazwa tagu do analizy"),
    number_of_pages: int = Query(..., description="Liczba stron do przetworzenia")):
    data = await asyncio.to_thread(td.trend_detection, tag_name, number_of_pages)
    return data

@app.get("/trend/combined")
async def combine(tag_name: str = Query(..., description="Nazwa tagu do analizy"),
    number_of_pages: int = Query(..., description="Liczba stron do przetworzenia")):
    data = await asyncio.to_thread(tw.combine, tag_name, number_of_pages)
    return data

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)