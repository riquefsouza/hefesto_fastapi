conda update -n base -c defaults conda
conda install -c conda-forge fastapi
conda install -c conda-forge uvicorn
uvicorn --version

python3 -m venv fastapi-env
source fastapi-env/bin/activate
ou
deactivate
pip3 install fastapi				 --> opcional
pip3 install uvicorn 				 --> opcional

uvicorn main:app --reload

git init

touch .gitignore
__pycache__
fastapi-env
.DS_Store

git add .

git commit -m "hefesto-fastapi"

/* SWAGGER */
http://localhost:8000/docs

