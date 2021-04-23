import fastapi
import uvicorn
from base.views import home
from admin.controllers import AdmUserController


app = fastapi.FastAPI()

def configure():
    app.include_router(home.router)
    app.include_router(AdmUserController.router)

configure()

#if __name__ == '__main__':
#    uvicorn.run(app)