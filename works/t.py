import pandas as pd
import datetime
import sys
import os

from utils.combine import Combine
from bases.logs import Logs
from bases.base import Base
from bases.date import Date
from bases.config import Config

#


import sys

a = ''
b = []
print(sys.getsizeof(a))
print(sys.getsizeof(a))

import numpy as np
a=np.random.random(4)
print(a)
print(a.dtype)
print(a.shape)
# a.dtype = 'int'
# print(a)
# print(a.dtype)
a = a.astype('int32')
print(a)
print(a.dtype)