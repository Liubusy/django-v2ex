# coding=utf-8

import re
import os
import logging

def detect(request):
    user_agent = request.META['HTTP_USER_AGENT']
    result = {}
    result['ua'] = user_agent
    if (re.search('iPod|iPhone|Android|Opera Mini|BlackBerry|webOS|UCWEB|Blazer|PSP|IEMobile', user_agent)):
        result['ios'] = True
    else:
        result['ios'] = False
    return result