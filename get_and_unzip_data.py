from multiprocessing import Pool,cpu_count
from os.path import abspath,dirname
from subprocess import call
from urllib import urlretrieve

basedir = abspath(dirname(__file__))
baseurl = 'http://unitedstates.sunlightfoundation.com/congress/data'


def getData(idx):
    thisurl = '%s/%s.zip' % (baseurl, idx)
    thiszip = '%s/%s/%s.zip' % (basedir, idx, idx)
    thisdir = '%s/%s' % (basedir, idx)
    call(['mkdir', thisdir])
    urlretrieve(thisurl, thiszip)
    call(['unzip', thiszip, '-d', thisdir])
    call(['rm', thiszip])
    print 'FINISHED: %s' % thiszip.split('/')[-1]

if __name__ == '__main__':
    pool = Pool(processes=cpu_count())
    pool.map(cleanfunc, range(93, 114))
    
