# CRN143

## Setup docker

1. Clone this repository
2. Copy `.env.example` to `.env`
3. Fill in your own values in the `.env` file
4. Run `docker-compose up -d` to start the services
5. Open browser go to http://localhost:{PGADMIN_EXTERNAL_PORT}/browser/

you must have docker desktop

## Loading data

1. clone repo https://github.com/PacktPublishing/SQL-for-Data-Analytics-Third-Edition
2. locate the datasets folder in the repo

## steps

1. Create DB
```{powershell}
docker-compose exec {POSTGRES_CONTAINER_NAME} createdb -U {POSTGRES_USER} sqlda
```

2. copy data to docker
```{powershell}
docker cp "{your_path}\data.dump" {POSTGRES_CONTAINER_NAME}:/tmp/data.dump
```

3. Load data to db
```{powershell}
docker-compose exec {POSTGRES_CONTAINER_NAME} psql -U {POSTGRES_USER} -d sqlda -f /tmp/data.dump
```

4. Validate import
```{powershell}
docker exec {POSTGRES_CONTAINER_NAME} psql -U {POSTGRES_USER} -d sqlda -c "\dt"
```

5. List all DBs
```{powershell}
docker exec {POSTGRES_CONTAINER_NAME} psql -U {POSTGRES_USER} -c "\l"
```

## Python 

### Security

1. create config.ini in week 4 folder and add following - change information as needed
```
[postgresql]
user = user
password = password
host = 127.0.0.1
port = 5432
database = postgres
```