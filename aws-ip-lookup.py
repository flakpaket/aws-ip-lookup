#! /usr/bin/env python3
import requests
import json
from ipaddress import ip_address, ip_network
import argparse



parser = argparse.ArgumentParser(
    description="Which AWS service an IP address belongs to.")
parser.add_argument('ip', type=str)

args = parser.parse_args()
ip = ip_address(args.ip)
aws_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
ip_ranges = requests.get(aws_url).json()['prefixes']

for ip_range in ip_ranges:
    if 'ip_prefix' in ip_range:
        ip_range['network'] = ip_network(ip_range['ip_prefix'])
    elif 'ipv6_prefix' in ip_range:
        ip_range['network'] = ip_network(ip_range['ipv6_prefix'])
    if ip in ip_range['network']:
        if 'service' in locals():
            if service['network'].netmask > ip_range['network'].netmask:
                continue
            else:
                service = ip_range
        else:
            service = ip_range

if 'service' in locals():
    
    for key in service:
        print('{}: {}'.format(key, service[key]))
else:
    print('\n{} does not appear to be an AWS IP.\n'.format(ip))
