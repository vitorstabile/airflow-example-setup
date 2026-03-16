# airflow-example-setup

# How to setup

- Clone the project

- Create the folders in the root of the project:
  - dags
  - logs
  - plugins
  - config
 
- If is necessary any other folder, put the patch of this folder in the docker-compose file
  - Ex: a data folder in the root of the project will be in the docker-compose ${AIRFLOW_PROJ_DIR:-.}/plugins:/opt/airflow/data

- setup the .env variables

- Make
  - ```docker compose up --build```
 
- Test the my_test_dag()
