conda update -n base -c defaults conda
conda install -c conda-forge fastapi
conda install -c conda-forge uvicorn
uvicorn --version

python3 -m venv venv
. venv/bin/activate
pip install -U pip setuptools

ou

deactivate

pip install fastapi
pip install uvicorn

uvicorn main:app --reload

git init

touch .gitignore
__pycache__
venv
.DS_Store

git add .

git commit -m "hefesto-fastapi"

/* SWAGGER */
http://localhost:8000/docs

/* REDOC */
http://localhost:8000/redoc

