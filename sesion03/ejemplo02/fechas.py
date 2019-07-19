from datetime import datetime

help(datetime)

print(datetime.now())

print(datetime(2019, 7, 10))

import os

print(os.path.getmtime("readme.md"))  # Fecha de modificacion, estilo C

print(datetime.fromtimestamp(os.path.getmtime("readme.md")))