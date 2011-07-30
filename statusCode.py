# coding: utf-8

###
## Script to reveal which http status code urls from a file give
## usage: statusCode.py urlfile statuscodeseries (1,2,3,4 or 5)
## author: Thomas Gøytil
###

import httplib2
import sys

if(len(sys.argv) != 3):
    print "usage: statusCode.py urlfile statuscodeseries (1,2,3,4 or 5)"

else:
    filename = sys.argv[1]
    statusCodeExtension = sys.argv[2]

    urlFile = open(filename, "r")
    urls = urlFile.readlines()

    for url in urls:
        url = url.strip()
        http = httplib2.Http()
        http.force_exception_to_status_code = True

        resp, content = http.request(url, "HEAD")
        httpStatusCode = str(resp.status)
        if(httpStatusCode[0] == statusCodeExtension):
            print "Url: " + url + "Gave status: " , resp.status

      