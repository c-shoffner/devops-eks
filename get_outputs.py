import requests, json, os, base64

tf_api_token = os.getenv('TF_API_TOKEN')
url = "https://app.terraform.io/api/v2/workspaces/ws-qam9e7EbmmEhKF6n/current-state-version?include=outputs"
headers = {
  'Authorization': f'Bearer {tf_api_token}'
}

try:
  response = requests.request("GET", url, headers=headers)
  response_json = response.json()
except:
  print("Cannot call Terraform Cloud API")

try:
  values = response_json['included']
except:
  print("Cannot find values within Terraform Cloud API")

env_file = os.getenv("GITHUB_ENV")
for x in values:
    name = x['attributes']['name']
    if 'cluster_name' in name:
        cluster_name = x['attributes']['value']

for x in values:
    name = x['attributes']['name']
    if 'region' in name:
        cluster_region = x['attributes']['value']


if (cluster_name) & (cluster_region):
  with open(env_file, "a") as myfile:
    myfile.write(f'CLUSTER_NAME={cluster_name}\n')
    myfile.write(f'CLUSETER_REGION={cluster_region}')
