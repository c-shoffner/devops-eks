# DevOps Exercise
</br>

The purpose of this exercise is to demonstrate the skills and ability required to containerize and deploy an application while using a CICD workflow. 

In the excercise, I have done the following: 
- Create an application.
- Containerize it. 
- Push to container registry.
- Provision EKS Infrastructure with Terraform. 
- Deploy to EKS cluster. 
- Set public DNS. 
- Run health check on application.

There are two methods that can be used for this exercise. 

1. [GitHub Actions](#github-actions)
2. [Deployment Bash Script](#deployment-bash-script)


## GitHub Actions
### System Requirements
The GitHub Action will download and install all system requirements.

### Setup
The following will need to be configured before the Action can be run.
- Generate [AWS Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html)
- Gather [Dockerhub Token](https://docs.docker.com/docker-hub/access-tokens/) and Username
- Generate [Terraform Cloud Token](https://developer.hashicorp.com/terraform/tutorials/cloud-get-started/cloud-login) and find the workspace ID.
#### *Optional*
- Generate [CloudFlare API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/), then use it to grab the [DNS Record & Zone ID](https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-list-dns-records)

**Once the tokens and credentials are gathered above, set the following secrets in GitHub Actions**
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `DOCKERHUB_TOKEN`
- `DOCKERHUB_USERNAME`
- `TF_API_TOKEN`
- `TF_CLOUD_ORGANIZATION`

#### *Optional*

- `CLOUDFLARE_API`
- `DNS_RECORD`
- `ZONE_ID`

### Deployment
The GitHub Action will do the following:
- Provision EKS instance using the Terraform Job.
- Build and push the python application to Docker Hub.
- Deploy the application to the EKS Cluster. 
- Grab the service address once the application has been deployed.
- Take the app service address and make an API call to CloudFlare to make the webhook accessible from http://devops.shoff.page:5000 (if CLOUDFLARE_API key is found. If not found, this step is skipped).
- Run python tests to ensure the webhook is up and functional.

### Clean Up
To destroy all instances, login to your Terraform Cloud account. Go to:  

    Workspace -> Settings -> Destruction and Deletion -> Queue Destroy Plan

## Deployment Bash Script

### System Requirements
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) (tested with v1.40)
- [Docker](https://docs.docker.com/engine/install/) (tested with v20)
- [kubectl](https://kubernetes.io/docs/tasks/tools/) (tested with v1.25.4)
- [python](https://www.python.org/downloads/) (tested with python3.8)
- [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (tested with 2.7.4)

### Setup
- Generate [AWS Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).
- Authenticate to your [Docker Repository](https://docs.docker.com/engine/reference/commandline/login/).
- Verify the custom variables at the beginning of the `deployment.sh` are accurate.
- There are several environment variables used during the `deployment.sh`. These will need to be specified before running the script.

```sh
### REQUIRED ###
export AWS_ACCESS_KEY_ID="#############"
export AWS_SECRET_ACCESS_KEY="#############"

### OPTIONAL ###
export ZONE_ID="#############"
export DNS_RECORD="#############"
export CLOUDFLARE_API="#############"
```

### Deployment
The `deployment.sh` at the root of the repository will automatically complete the exercise. It will go through the following steps:

- Provision EKS instance by using the files in the `terraform` folder.
- Grab the context of the newly created EKS cluster, then set the context on the local machine.
- Build the docker image within the `app` folder, then tag it and push it to dockerhub.
- Deploy to the EKS cluster by using the manifest in the `manifest` folder.
- Grab the service address once the application has been deployed.
- Take the app service address and make an API call to CloudFlare to make the webhook accessible from http://devops.shoff.page:5000 (if `CLOUDFLARE_API` key is found. If not found, this step is skipped).
- Run python tests to ensure the webhook is up and functional.

### Cleanup
To destroy all instances, you can `cd` into the `terraform` folder and run `terraform destroy`.