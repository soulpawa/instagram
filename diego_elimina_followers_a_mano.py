# diego_elimina_followers_a_mano

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random
import time

from diego_util import login
from diego_util import bloquear
from diego_util import pitar

api = login()
lista = [
]

for l in lista:
    time.sleep(1 + random.randint(3, 6))
    bloquear(api, l)

pitar()