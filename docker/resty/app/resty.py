import yaml
import time
from kubernetes import client, config, watch

JOB_NAME = 'rowy-job-'
kubernetes_config_file_path = '~/.kube/config'

def create_job_object(id_number: str, job_id: str):
    container = client.V1Container(
        name='rowy-cronjob',
        image='blindspot/rowy-cronjob:latest',
        image_pull_policy='Never',
        env=[client.V1EnvVar(name="VALUE_ID", value=str(id_number))])

    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={'name': 'rowy-job'}),
        spec=client.V1PodSpec(restart_policy='OnFailure', containers=[container]))

    spec = client.V1JobSpec(template=template)

    job = client.V1Job(
        api_version='batch/v1',
        kind='Job',
        metadata=client.V1ObjectMeta(name=JOB_NAME + str(job_id)),
        spec=spec)

    return job

def create_job(api_instance, job):
    api_response = api_instance.create_namespaced_job(
        body=job,
        namespace='default')
    print("Job created. status='%s'" % str(api_response.status))

def delete_job(api_instance, job_id: str):
    api_response = api_instance.delete_namespaced_job(
        name=JOB_NAME + str(job_id),
        namespace='default',
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=0))
    print("Job deleted. status='%s'" % str(api_response.status))
