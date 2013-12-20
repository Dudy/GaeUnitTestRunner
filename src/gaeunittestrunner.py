#!/usr/bin/python

import optparse
import sys
import unittest2

SDK_PATH = '/usr/local/google_appengine'

USAGE = """%prog TEST_PATH [SDK_PATH]
Run unit tests for App Engine apps.

TEST_PATH   Path to package containing test modules
SDK_PATH    Path to the SDK installation (defaults to /usr/local/google_appengine)"""


def main(sdk_path, test_path):
    sys.path.insert(0, sdk_path)
    import dev_appserver
    dev_appserver.fix_sys_path()
    suite = unittest2.loader.TestLoader().discover(test_path)
    unittest2.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    parser = optparse.OptionParser(USAGE)
    options, args = parser.parse_args()
    
    for a in args:
        print a
    
    if len(args) == 0:
        print "Error: no arguments given"
        parser.print_help()
        sys.exit(1)
    if len(args) == 1:
        TEST_PATH = args[0]
    elif len(args) == 2:
        SDK_PATH = args[0]
        TEST_PATH = args[1]
    else:
        print 'Error: too many arguments given'
        parser.print_help()
        sys.exit(1)
    
    main(SDK_PATH, TEST_PATH)