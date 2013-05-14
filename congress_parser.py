from glob import glob
from json import loads,dumps
from pandas import datetools
import subprocess

datafiles = glob('./*/bills/hr/*/data.json')
datafiles.extend(glob('./*/bills/s/*/data.json'))

subprocess.call(['mkdir', 'metadata'])
subprocess.call(['mkdir', 'texts'])
subprocess.call(['mkdir', 'texts/raw'])

log = open('logs.txt', 'w')
meta = open('metadata/jsoncatalog.txt', 'w')
for datafile in datafiles:
    try:
        f = open(datafile, 'r')
        data = loads(f.read())
        f.close()
    
        tmpdct = {}
        tmpdct['filename'] = data['bill_id']
        tmpdct['chamber'] = [data['bill_type']]
        tmpdct['title'] = data['summary']['text'].encode('utf-8')
        tmpdct['official_title'] = data['official_title']
        tmpdct['enacted'] = [str(data['history']['enacted'])]
        tmpdct['vetoed'] = [str(data['history']['vetoed'])]
        tmpdct['awaiting_signature'] = [str(data['history']['awaiting_signature'])]
        tmpdct['status'] = [data['status']]
        tmpdct['sponsor_state'] = [data['sponsor']['state']]
        tmpdct['sponsor_name'] = [data['sponsor']['name']]

        tmpdct['cosponsors_state'] = [i['state'] for i in data['cosponsors']]
        tmpdct['cosponsors_name'] = [i['name'] for i in data['cosponsors']]

        dt = datetools.parse(data['summary']['date'])
        tmpdct['date'] = '%s-%s-%s' % (int(dt.year+1), dt.month, dt.day)

        url = 'http://www.govtrack.us/congress/bills/%s/%s' % (data['bill_type'], datafile.split('/')[-2])
        tmpdct['searchstring'] = '<a href="%s" target="_blank">%s</a>' % (url, tmpdct['official_title'])
        meta.write('%s\n' % dumps(tmpdct))
        filepath = 'texts/raw/%s.txt' % tmpdct['filename']
        f = open(filepath, 'w')
        f.write(tmpdct['title'])
        f.close()
    except:
        log.write('%s\n' % datafile)
        pass
meta.close
log.close()
