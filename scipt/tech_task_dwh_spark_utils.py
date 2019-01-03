import os
import sys
import logging
import inspect
from requests import get

def mkdirs(dir):

    """ Function: mkdir -p dir """

    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)

def lineno():

    """ Returns the current line number in the program """

    return inspect.currentframe().f_back.f_lineno

class Logger:

    """
    Logging class

    :param logfile: string - path where to write log into
    :param kill: boolean - shall the script be interrupted
    """

    def __init__(self, logfile, kill=True):

        self.kill = kill

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename=logfile,
                            filemode='a+')
        self.logger = logging.getLogger('logs')

    def send(self, msg, info=False, kill=True, state=1):

        """
        Function to send the message to a log file

        :param msg: string - message to log
        :param info: boolean - is info message?
        :param kill: boolean - shall the script be interrupted
        :param state: [1,0] - error interruption state
        """

        if info:
            self.logger.info(f"{msg}")
        else:
            self.logger.error(f"{msg}")

            # kill the process
            if self.kill and kill:
                sys.exit(state)

class Fetcher:

    """ Data fetching class """

    def get_flat_ids(token):

        """
        Function to fetch flat IDs from immobilienscout24.de using search API end-point
        see details: https://api.immobilienscout24.de/our-apis/search/queryparameters.html

        :param token: API access OAuth1 token

        :return: tuple (dict, ex), dict is the API responce json, ex - exception
        """

        def _get_search_data(page_number=1, flats_per_page=200):

            """ Function to get seach API data for Berlin """

            try:

                search_data = get(f"https://rest.immobilienscout24.de/restapi/api/search/v1.0/search/region?realestatetype=ApartmentRent&geocodes=1276003&pagesize={flats_per_page}&pagenumber={page_number}",
                                  auth=token,
                                  headers={'accept': 'application/json'})

                if search_data.ok:
                    return search_data.json()['resultlist.resultlist'], None

                return None, f"HTTP status: {search_data.status_code}"

            except Exception as ex:

                return None, ex

        def _get_n_pages():

            """ Function to fetch number of pages and number of flats in Berlin on the immobilienscout24.de """

            dat, ex = _get_search_data()

            if ex:
                return None, None, ex

            return dat['paging']['numberOfPages'], dat['paging']['numberOfHits'], None

        # get the number of pages with flats and number of flats in Berlin available on immobilienscout24
        n_pages, n_flats, ex = _get_n_pages()

        if ex:
            return None, ex

        # get flat IDs
        flat_ids = []

        # loop over pages and fetch data for all flats on each page
        for iPage in range(1, n_pages + 1):

            # get the flats data on one page
            data_on_page, ex = _get_search_data(page_number=iPage)

            if ex:
                continue

            data_on_page = data_on_page['resultlistEntries'][0]['resultlistEntry']

            # flat IDs on one page
            flat_ids_on_page = [int(data_on_page[i]['@id']) for i in range(len(data_on_page))]

            # add to the list of all flat IDs
            flat_ids.extend(flat_ids_on_page)

        return flat_ids, None


    def get_flat_info(token, flat_id):

        """
        Function to fetch flat's data using immobilienscou24 API exposé end-point
        See details here: https://api.immobilienscout24.de/our-apis/expose/web-content.html

        :param token: API access OAuth1 token
        :param flat_id: immobilienscou24.de ad's ID

        :return: tuple (dict, ex), dict is the API responce json, ex - exception
        """

        try:

            p = get(f"https://rest.immobilienscout24.de/restapi/api/search/v1.0/expose/{flat_id}",
                    auth=token,
                    headers={'accept': 'application/json'})

            if p.ok:
                return p.json(), None

            return None, f"HTTP status: {p.status_code}"

        except Exception as ex:
            return None, ex
