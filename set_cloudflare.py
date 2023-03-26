import requests, os

zone_id = os.getenv("ZONE_ID")
dns_record = os.getenv("DNS_RECORD")
cloudflare_api = os.getenv("CLOUDFLARE_API")
hostname = os.getenv("HOSTNAME")

url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record}?Content-Type=application%2Fjson'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {cloudflare_api},'
    }
body = json.dumps({
    'content': f'{output}',
    'name': 'liatrio',
    'proxied': false,
    'type': 'CNAME'
})

response = requests.post(url, headers=headers, data=body)
print(response.text)