import fastapi
import uvicorn
import movie_data
from models.movie_model import MovieModel

app = fastapi.FastAPI()

@app.get('/')
def index():
    return{
        "message":"Hello World"
    }

@app.get('/api/movie/{title}',response_model = MovieModel)
async def movie_search(title : str):
    movie = await movie_data.getMovies(title)
    if not movie:
        raise fastapi.HTTPException(status_code = 404)

    return movie.dict()


    
if __name__=='__main__':
    uvicorn.run(app)