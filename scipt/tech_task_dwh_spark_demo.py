# Spark Networks GbmH - Tech Task Demo
# D.Kisler <dmitry.kisler@affinitas.de>

import os
import json
import time
from requests_oauthlib import OAuth1
from tech_task_dwh_spark_utils import (mkdirs,
                                       Logger,
                                       lineno,
                                       Fetcher)

### settings ###
# path where file is located
DIR2FILE = os.path.dirname(__file__)
# output dir
DIRout = os.path.join(DIR2FILE, 'flats_data', time.strftime('%Y/%m'))
# output file
FILEout = os.path.join(DIRout, "immobilienscout24_berlin_{}.json".format(time.strftime('%Y%m%d')))
# immobilienscou24.de API credentials location
FILEcredentials = os.path.join(DIR2FILE, 'token.json')
# logs directory
DIRlog = os.path.join(DIR2FILE, 'logs', time.strftime('%Y/%m'))
# create logs dir if it doesn't exist
mkdirs(DIRlog)
# logger
log = Logger(logfile=os.path.join(DIRlog,  "immobilienscout24_berlin_{}.log".format(time.strftime('%Y%m%d'))))

def main():

    # get OAuth1 token(s)
    api_credentials = json.load(open(FILEcredentials, 'r'))
    token = {k: OAuth1(api_credentials[k]['KEY'], api_credentials[k]['SECRET'], api_credentials[k]['TOKEN_key'], api_credentials[k]['TOKEN_secret']) for k in api_credentials.keys()}

    # fetch the list of flats
    flat_ids, ex = Fetcher.get_flat_ids(token['search'])

    if ex:
        log.send(f"exception: {ex}. line: {lineno()}")

    # create output dir if it doesn't exist
    mkdirs(DIRout)

    # loop over flat IDs
    for flat in flat_ids:
        try:
            # fetch data for a flat
            msg, ex = Fetcher.get_flat_info(token['expose'], flat)

            # write message by message into fout
            if not ex:
                with open(FILEout, 'a+') as f:
                    f.write(json.dumps(msg) + '\n')

            else:
                log.send(f"exception: {ex}. line: {lineno()}", kill=False)

        except Exception as ex:
            log.send(f"flat_id: {flat}. except: {ex}. line: {lineno()}", kill=False)

if __name__ == "__main__":

    start = time.time()

    log.send(f"Start immobilienscou24.de data fetching", info=True)

    main()

    log.send(f"Done! Elapsed time: {round(time.time()-start, 1)} sec.", info=True)
