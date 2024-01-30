# CarMarket
This is API for CRUD and listing by flask API with MongoDB.
It has 3 part
  -  Broker Infomation (create new broker, update broker data, delete broker data and show Broker Infomation with their cars data)
  -  Car Infomation (create new car, update car data, delete car data and show car Infomation)
  -  Listing data for see all car status

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
docker run -t -d --rm -v <carMarketFolder>:/app/src -p 8000:8000 carmarket:latest python3 app.py
```

# API testing
### Postman
  - Download CarMatketAPIForPastman from a branch
  - Import CarMatketAPIForPastman to postman
  - Change IP and parameter 
### Swagger
  - Go to web brower
```
http://<IP>:8000/api/docs/
```
[prove_file_name]_score.xlsx
