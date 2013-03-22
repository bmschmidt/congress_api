from glob import glob
from multiprocessing import Pool
from os.path import abspath,dirname
from subprocess import call
from urllib import urlretrieve

basedir = abspath(dirname(__file__))
baseurl = 'http://unitedstates.sunlightfoundation.com/congress/data'


def cleanfunc(i):
    thisurl = '%s/%s.zip' % (baseurl, i)
    thiszip = '%s/%s/%s.zip' % (basedir, i, i)
    thisdir = '%s/%s' % (basedir, i)
    call(['mkdir', thisdir])
    urlretrieve(thisurl, thiszip)
    call(['unzip', thiszip, '-d', thisdir])
    call(['rm', thiszip])
    print 'FINISHED: %s' % thiszip.split('/')[-1]

if __name__ == '__main__':
    pool = Pool(processes=8)
    pool.map(cleanfunc, range(93, 114))
    
