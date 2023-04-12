import requests, json, os
from kubernetes import client, config


# Use kube package to get hostname of service
config.load_kube_config()
v1 = client.CoreV1Api()

services = v1.list_service_for_all_namespaces(watch=False)

for svc in services.items:
    if svc.status.load_balancer.ingress:
        hostname = svc.status.load_balancer.ingress[0].hostname
        print(svc.status.load_balancer.ingress[0].hostname)

# Call env variables required
if "ZONE_ID" or "DNS_RECORD" or "CLOUDFLARE_API" in os.environ:
    zone_id = os.getenv("ZONE_ID")
    dns_record = os.getenv("DNS_RECORD")
    cloudflare_api = os.getenv("CLOUDFLARE_API")



    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record}?Content-Type=application%2Fjson'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {cloudflare_api}'
        }
    body = json.dumps({
        'content': f'{hostname}',
        'name': 'devops',
        'proxied': False,
        'type': 'CNAME'
    })
else: 
    print("CloudFlare credentials are not present. Will not DNS.")
# set hostname as env var
env_file = os.getenv("GITHUB_ENV")
with open(env_file, "a") as myfile:
  myfile.write(f'HOSTNAME={hostname}')
  
# call cloudflare api and set dns
response = requests.put(url, headers=headers, data=body)
print(response.text)




