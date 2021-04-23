import fastapi
import uvicorn
from base.views import home
from admin.controllers import AdmUserController
from api import wheather_api

app = fastapi.FastAPI()

def configure():
    app.include_router(home.router)
    app.include_router(AdmUserController.router)
    app.include_router(wheather_api.router)

configure()

#if __name__ == '__main__':
#    uvicorn.run(app)
