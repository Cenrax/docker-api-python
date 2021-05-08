import httpx 
from models.movie_model import MovieModel
from typing import Optional


async def getMovies(subtext:str) -> Optional[MovieModel]:
    url = f'https://movieservice.talkpython.fm/api/search/{subtext}'
    async with httpx.AsyncClient() as client: 
        resp: httpx.Response = await client.get(url)
        resp.raise_for_status()
        data = resp.json()
    result = data['hits']
    
    

    if not result:
        return None
    
    
    movie = MovieModel(**result[0])
    
    return movie
        