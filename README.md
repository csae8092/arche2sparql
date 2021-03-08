# arche2sparql

dockerized script to

* fetch data from ARCHE
* Post it against some Triple Store

## configure

provide a `.env` file to pass in secrets as environment variables, something like

```
BGUSER=username
BGPW=password
```

endpoints of ARCHE and TripleStore are hard coded in the script

## install/run

* build the Image with `docker build -t archetosparql .`
* run it with `docker run --rm --env-file ./.env archetosparql:latest`


## without docker

* install requirements
* set environemt variables (see above)
* run `python sync.py`