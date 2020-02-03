import os
import sys
import time
from apps.ChinaUnicom import ChinaUnicomApp

username = os.getenv('utv_mobile')
userid = os.getenv('utv_id')

def utvCheckin():
    content_utv = utvAPP().utv(username, userid)
    return content_utv

if __name__=='__main__':
    try:
        msg = utvCheckin()
        exitCode = 0
    except Exception as e:
        print('Error: ' + msg)
        exitCode = 1

    sys.exit(exitCode)