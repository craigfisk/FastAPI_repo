from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithID

app = FastAPI()

BANDS = [
    {"id": 1, 'name': 'The Kinks', 'genre': 'Rock'},          
    {"id": 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {"id": 3, 'name': 'Black Sabbath', 'genre': 'Metal', 'albums': [
        {'title': 'Master of Reality', 'release_date': '1971-07-21'},
        {'title': 'Dog Food', 'release_date': '1972-07-21'}
    ]}, 
    {"id": 4, 'name': 'Wu-Tang Clan', 'genre': 'Hip-Hop'},    
]

@app.get('/bands')
async def bands(
    genre: GenreURLChoices | None = None,
    has_albums: bool = False
    ) -> list[BandWithID]:
    band_list = [BandWithID(**b) for b in BANDS]

    if genre:
        band_list = [
            b for b in band_list if b.genre.lower() == genre.value
        ]
    
    if has_albums:
        band_list = [b for b in band_list if len(b.albums) > 0]
    return band_list 

@app.get('/bands/{band_id}')  
async def band(band_id: int) -> BandWithID:
    band = next((BandWithID(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail='Band not found')
    return band

@app.get('/bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]

@app.post("/bands")
async def create_band(band_data: BandCreate) -> BandWithID:
    id = BANDS[-1]['id'] + 1
    band = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band
    # return BandWithID(**band)   
    
    # new_band = band_data.dict()
    # new_band['id'] = new_id
    # new_band['albums'] = []
    # BANDS.append(new_band)
    # return BandWithID(**new_band)
    


