import logging

def main():
    # configure the logging system

    # logging.basicConfig(filename='app.log',
    #                     level=logging.ERROR)
    # #
    # # CRITICAL:root:Host www.python.org unknown
    # # ERROR:root:Couldn't find 'spam'
    # #

    logging.basicConfig(
        filename= 'app.log',
        level = logging.WARNING,
        format = '%(levelname)s:%(asctime)s:%(message)s'
    )
    #
    # CRITICAL:2022-09-24 05:12:15,767:Host www.python.org unknown
    # ERROR:2022-09-24 05:12:15,768:Couldn't find 'spam'
    # WARNING:2022-09-24 05:12:15,769:Feature is deprecated
    #

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
