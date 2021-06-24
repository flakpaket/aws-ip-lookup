# aws-ip-lookup
```
$ python aws-ip-lookup.py -h
usage: aws-ip-lookup.py [-h] ip

Which AWS service an IP address belongs to.

positional arguments:
  ip

optional arguments:
  -h, --help  show this help message and exit
```

## Usage
```
$ python3 aws-ip-lookup.py 54.239.28.85
ip_prefix: 54.239.16.0/20
region: us-east-1
service: AMAZON
network_border_group: us-east-1
network: 54.239.16.0/20
```
