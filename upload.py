import boto
import boto.s3
import sys
from boto.s3.key import Key
import time
import datetime

AWS_ACCESS_KEY_ID = 'AKIAIEF6HHISM7IMQ2SA'
AWS_SECRET_ACCESS_KEY = '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'

#bucket_name = AWS_ACCESS_KEY_ID.lower() + '-dump'
bucket_name = "com.iotest"
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

testfile = "test.hi"
print 'Uploading %s to Amazon S3 bucket %s' % \
   (testfile, bucket_name)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H:%M:%S')

k = Key(bucket)
k.key = st
k.set_contents_from_filename(testfile,
    cb=percent_cb, num_cb=10)