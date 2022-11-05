import logging
import os

class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exec_info):
        result = super().formatException(exec_info)
        return repr(result)
    
    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace('\n', '')
            return result
        
handler = logging.StreamHandler()
formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
root = logging.getLogger()
root.setLevel(os.environ.get('LOGLEVEL', 'INFO'))
root.addHandler(handler)

try:
    exit(main())
except Exception:
    logging.exception('Exception in main (): ')
    exit(1)
