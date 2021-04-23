import fastapi
from api.location import Location
from api.umbrella_status import UmbrellaStatus
import httpx

router = fastapi.APIRouter()

@router.get('/api/umbrella', response_model = UmbrellaStatus)
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()):
    url = f'https://weather.talkpython.fm/api/weather?city={location.city}&conutry={location.country}&units=imperial'
    if location.state:
        url += f'&state={location.state}'
    
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        #print(resp.status_code)
        #print(resp.text)

        data = resp.json()
    
    weather = data.get('weather', {})
    category = weather.get('category','UNKNOWN')
    
    forecast = data.get('forecast', {})
    temp = forecast.get('temp', 0.0)

    bring = category.lower().strip() == 'rain'

    umbrella = UmbrellaStatus(bring_umbrella=bring, temp=temp)

    return umbrella