#!/usr/bin/env python3

import json
import requests

r = requests.get('https://httpbin.org/json')
out = json.loads(r.content)

print(out['slideshow']['title'])
