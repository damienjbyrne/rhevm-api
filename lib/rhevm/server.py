#
# This file is part of RHEVM-API. RHEVM-API is free software that is made
# available under the MIT license. Consult the file "LICENSE" that is
# distributed together with this file for the exact licensing terms.
#
# RHEVM-API is copyright (c) 2010 by the RHEVM-API authors. See the file
# "AUTHORS" for a complete overview.

import re
import sys
import logging
from optparse import OptionParser

from rest import make_server
from rhevm.application import RhevmApp

re_listen = re.compile('([-A-Za-z.]+):([0-9]+)')


def _setup_logging(debug):
    """Set up logging."""
    if debug:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    format = '%(levelname)s [%(name)s] %(message)s'
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)


def main():
    """Command-line integration. Start up the API based on the built-in
    wsgiref web server."""
    parser = OptionParser()
    parser.add_option('-l', '--listen', dest='listen',
                      help='listen on interface:port')
    parser.add_option('-d', '--debug', action='store_true')
    parser.set_default('listen', 'localhost:8080')
    parser.set_default('debug', False)
    opts, args = parser.parse_args()
    mobj = re_listen.match(opts.listen)
    if not mobj:
        parser.error('specify --listen as host:port')
    address = mobj.group(1)
    port = int(mobj.group(2))
    _setup_logging(opts.debug)
    server = make_server(address, port, RhevmApp)
    print 'Listening on %s:%s' % (address, port)
    print 'Press CTRL-C to quit'
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
