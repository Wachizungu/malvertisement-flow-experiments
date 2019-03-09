from pymisp import PyMISP
from config.misp_config import MISP_URL, MISP_KEY


def url_in_misp(url):
    misp = PyMISP(MISP_URL, MISP_KEY)
    result = misp.search('attributes', values=[url])
    if len(result['response']['Attribute']) > 0:
        return True
    else:
        return False
