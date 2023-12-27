# CarMarket
This is API for CRUD and listing by flask API with MongoDB

# Installation

### Conda
We recommend installing in a fresh Conda environment.
```
conda create --name carmarket
conda activate carmerket
```
Install requirements.txt
```
pip3 install -r requirements.txt
```
### Docker containers
To build a nemo container with Dockerfile from a branch, please run
```
docker build -t carmarket:latest .
```
Start docker containers
```
docker run -t -d --rm -v <carMarketFolder>:/app/src \
-p 8000:8000 carmarket:latest python3 app.py
```
