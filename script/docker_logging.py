'''Logging inside a docker container.'''

import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

exit(main())
