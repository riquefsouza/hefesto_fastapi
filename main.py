import fastapi
import uvicorn
from base.views import home
from admin.controllers import AdmUserController, AdmMenuController, AdmPageController
from admin.controllers import AdmParameterCategoryController, AdmParameterController, AdmProfileController
from api import wheather_api
from base.controllers import LoginController

app = fastapi.FastAPI()

def configure():
    app.include_router(home.router)
    app.include_router(wheather_api.router)
    app.include_router(LoginController.router)
    app.include_router(AdmMenuController.router)
    app.include_router(AdmPageController.router)
    app.include_router(AdmParameterCategoryController.router)
    app.include_router(AdmParameterController.router)
    app.include_router(AdmProfileController.router)
    app.include_router(AdmUserController.router)

configure()

#if __name__ == '__main__':
#    uvicorn.run(app)
