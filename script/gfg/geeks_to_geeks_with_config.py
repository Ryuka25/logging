import logging
import logging.config

def main():
    # configure the logging system
    logging.config.fileConfig('logconfig.ini')

    # variable (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error('Couldn\'t find %r', item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode = %r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()
