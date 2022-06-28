## How to run this project

1 Running the app with docker compose <br /> <br />
Run
```
sudo docker-compose -f stack.yml up
```
The results will be displayed on your machine at http://127.0.0.1:8080/show  <br />
And inside the docker network at http://127.0.0.1:8001/show <br /><br />
2 Running the app directly with python <br /> <br />
All Python packages can be installed using a requirements.txt file with pip or conda venv<br /> 
set env variables in your ~/.bashrc so they correspond to a DB you want to use
```
export POSTGRES_USER=postgres
export POSTGRES_DB=postgres
export POSTGRES_PASS=example
export POSTGRES_PORT=5432
export POSTGRES_HOST=localhost
```
make sure that the psql server is running using
```
pg_lsclusters
```
if the cluster is down start it like so
```
sudo pg_ctlcluster <Ver> <Cluster> start
```
Launch the app
```
python3 main.py
```