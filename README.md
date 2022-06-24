## How to run this project

1 Running the app directly with python <br /> <br />
All Python packages can be installed using a requirements.txt file with pip or conda venv<br /> 
set env variables in your ~/.bashrc
```
export POSTGRES_USER=zelda
export POSTGRES_DB=zelda
export POSTGRES_PASS=burgermenu
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
2 Running the app with docker compose <br /> <br />
In stack.yml change env variables for your database then run
```
sudo docker-compose -f stack.yml up
```