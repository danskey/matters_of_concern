import os
from os.path import join
import datetime
import time

##############   Angel of History   ##############


def watch(archive, cycle_length, start_time):
    print "Watching... the current time is %s" % time.time() #printing out time to check functioning.
    try:
        while time.time() < start_time + cycle_length:
            theNow = time.time() - 5.5

            def modification_date(filename):
                    t = os.path.getmtime(filename)
                    return t

            def access_date(filename):
                     t = os.path.getatime(filename)
                     return t

            for root, dirs, files in os.walk(archive):
                    for name in files:
                        if access_date(join(root, name)) > theNow:
                            r = join(root, name), "MODIFIED:", modification_date(join(root, name)), "ACCESSED:", access_date(join(root, name))
                            result = str(r)
                            print result
                            f = open('ArchiveLOG.txt','a')
                            f.write(result+"\n")
                            print "-- result saved --"

            #print "Watching... the current time is %s" % time.time() #printing out time to check functioning.
            time.sleep(5)
    except KeyboardInterrupt:
        raise


def forget(archive, start_time):
    print "Looking for files to forget" #printing out time to check functioning.

    def modification_date(filename):
            t = os.path.getmtime(filename)
            return t

    def access_date(filename):
             t = os.path.getatime(filename)
             return t

    for root, dirs, files in os.walk(archive):
            for name in files:
                if access_date(join(root, name)) < start_time:
                    r = join(root, name), "MODIFIED:", modification_date(join(root, name)), "ACCESSED:", access_date(join(root, name))
                    result = str(r)
                    f = open('ArchiveNeglectedLOG.txt','a')
                    f.write(result+"\n")
                    print "-- result saved --"
                else:
                    pass
