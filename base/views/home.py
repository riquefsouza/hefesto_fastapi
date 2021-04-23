import fastapi 
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates("base/templates")

router = fastapi.APIRouter()

@router.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

