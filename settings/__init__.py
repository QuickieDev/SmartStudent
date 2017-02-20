# -*- coding: utf-8 -*-
"""Smart student app settings package.
"""

import os
import sys


if os.environ.get('APP_ENV') == 'DEV':

    from settings import dev
    sys.modules['settings'] = dev

else:
    from settings import prod
    sys.modules['settings'] = prod
