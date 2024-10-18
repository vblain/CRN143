# CRN143

## Setup docker

1. Clone this repository
2. Copy `.env.example` to `.env`
3. Fill in your own values in the `.env` file
4. Run `docker-compose up -d` to start the services
5. Open browser go to http://localhost:5050/browser/

you must have docker desktop

## Loading data

1. clone repo https://github.com/TrainingByPackt/SQL-for-Data-Analytics/tree/master
2. following direction from Datasets Loading_the_sample_datasets_instructions.pdf

## steps

1. Create DB
```{powershell}
docker-compose exec postgres createdb -U {your_user_name} sqlda
```

2. copy data to docker
```{powershell}
docker cp "{your_path}\SQL for Data Analytics\SQL-for-Data-Analytics-master\Datasets\data.dump" my_postgres:/tmp/data.dump
```

3. Load data to db
```{powershell}
docker-compose exec postgres psql -U {your_user_name} -d sqlda -f /tmp/data.dump
```

4. Validate import
```{powershell}
docker-compose exec postgres psql -U {your_user_name} -d sqlda -c "\dt"
```

5. List all DBs
```{powershell}
docker-compose exec postgres psql -U {your_user_name} -c "\l"
```