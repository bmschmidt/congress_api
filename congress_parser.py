from glob import glob
from json import loads,dumps

datafiles = glob('./*/bills/hr/*/data.json')
datafiles.extend(glob('./*/bills/s/*/data.json'))

meta = open('../metadata/jsoncatalog.txt', 'w')
for datafile in datafiles:
    try:
        f = open(datafile, 'r')
        data = loads(f.read())
        f.close()
    
        tmpdct = {}
        tmpdct['bill_id'] = data['bill_id']
        tmpdct['chamber'] = data['bill_type']
        tmpdct['date'] = data['summary']['date']
        tmpdct['summary'] = data['summary']['text'].encode('utf-8')
        tmpdct['official_title'] = data['official_title']
        tmpdct['enacted'] = str(data['history']['enacted'])
        tmpdct['vetoed'] = str(data['history']['vetoed'])
        tmpdct['awaiting_signature'] = str(data['history']['awaiting_signature'])
        tmpdct['status'] = data['status']
        tmpdct['sponsor_state'] = data['sponsor']['state']
        tmpdct['sponsor_name'] = data['sponsor']['name']
        tmpdct['sponsor_type'] = data['sponsor']['type']
    
        meta.write('%s\n' % dumps(tmpdct))
        filepath = '../texts/raw/%s.txt' % tmpdct['bill_id']
        f = open(filepath, 'w')
        f.write(tmpdct['summary'])
        f.close()
    except:
        print 'Parsing Failed: %s' % datafile
        pass
