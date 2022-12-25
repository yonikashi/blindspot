#!/bin/bash -e
BASE_DIR=$PWD
TF_WORKSAPCE=test-app-5

cd $BASE_DIR/docker/rowy
docker build . -t blindspot/rowy-cronjob:latest -f rowy.Dockerfile
cd $BASE_DIR/docker/postgresql-db
docker build . -t postgresql-db -f db.Dockerfile
cd $BASE_DIR/docker/resty
docker build . -t blindspot/resty-api:latest -f resty.Dockerfile

cd $BASE_DIR/terraform/local

terraform workspace new $TF_WORKSAPCE && terraform workspace select $TF_WORKSAPCE
terraform init
terraform apply --auto-approve

export LOCAL_PORT=$(kubectl get svc resty-chart -o yaml | grep nodePort | cut -f 2 -d ':' | tr -d ' ')
echo "==============================================="
echo "Run the following command to debug localy the flow:"
echo "curl -X POST http://localhost:$LOCAL_PORT/api\?value\=12345 -vvv"
echo "==============================================="
