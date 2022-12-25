[TOC]



# Blindspot resty and rowy framework
This repository is a part of a test framework still in POC phase.

### Goal
The goal of this terraform deployment is to install on local kubernetes cluster helm chart: `resty-chart`.
The chart is not published yet therfore it is still part of this repository.

------------


#### Prerequisites
- Terraform > 0.13.4;
- Kubectl > v1.22.4;

##### How to install
1. Clone the repository localy and go inside `blindspot` folder.
2. Run the bash script `./build-run-local.sh` to build the relevant docker containers and to trigger terraform apply.
3. Approve the terraform by typing `yes`.
4. Check the curl example shown at the output to trigger the flow.

##### How to remove
1. Go to the folder `blindspot/terraform/local`.
2. Run `terraform destroy` and approve.

##### How to test the flow localy
1. Run a curl command to send post request to the local service endpoint **(Example command is presented on script completion)**
```
curl -X POST http://localhost:$LOCAL_PORT/api\?value\=12345
```

### To be done
- Support deployment on cloud environment (not tested).
- Create helm release process and seperate to different repo,
- Create CI process for artifacts so not to build it localy and change pull policy from `Never` to `IfNotPresent`.
- Add prometheus exporter to resty microservice to fetch response time of requests.
- Enrich parameters passed to terraform and to helm chart to make it more flexible (change namespace deployment / replicas etc...).
