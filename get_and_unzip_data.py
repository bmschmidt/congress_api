import multiprocessing
import os
import subprocess
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))
baseURL = 'http://unitedstates.sunlightfoundation.com/congress/data'


def getCongressData(congress_num):
    zip_path = '%s/%s/%s.zip' % (basedir, congress_num, congress_num)
    outdir = '%s/%s' % (basedir, congress_num)
    subprocess.call(['mkdir', outdir])
    urllib.urlretrieve('%s/%s.zip' % (baseURL, congress_num), zip_path)
    subprocess.call(['unzip', '-qq', zip_path, '-d', outdir])
    subprocess.call(['rm', zip_path])
    print 'DONE: %s' % zip_path.split('/')[-1]

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.map(getCongressData, range(93, 114))
    pool.close()
