from hashlib import md5
from itertools import count
print next(i for i in count(1)
           if md5('iwrupvqb{}'.format(i)).hexdigest().startswith('000000'))