import pandas as pd
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import requests
import bs4
import re
import logging
import collections
import csv
import time
import itertools
#from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 
from numpy import random
from time import sleep
from functools import partial


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wb')
logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(
    logging.WARNING)
HEADERS_LINK = ('Links')
