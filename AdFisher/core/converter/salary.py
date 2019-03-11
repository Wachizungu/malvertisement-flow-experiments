import re
from datetime import datetime


class Salary:

    def __init__(self, value, treatment_id, separator='@|'):
        chunks = re.split(separator, value)
        print(chunks)
        self.time = datetime.strptime(chunks[0], "%Y-%m-%d %H:%M:%S.%f")
        self.title = chunks[1]
        print(self.title)
