import boto
import boto.s3
import sys
import boto3
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAIEF6HHISM7IMQ2SA'
AWS_SECRET_ACCESS_KEY = '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'

#bucket_name = AWS_ACCESS_KEY_ID.lower() + '-dump'
bucket_name = "com.iotest"
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)

#conn = boto.connect_s3('ap-southeast-2')
bucket = conn.get_bucket(bucket_name)

#Print out all buckets

for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )

k = Key(bucket)
'''
if not sys.argv[1]:
    k.key = '20170619-23:55:15'
else:
    k.key = sys.argv[1]
print "key = " , k.key
'''
#Print all files in the bucket
for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )

#key = bucket.get_key('20170619-23:55:15')
key = bucket.get_key('test1.jpg')
key.get_contents_to_filename('test.jpg')

# Create an SNS client

client = boto3.client(
    "sns",
    aws_access_key_id= 'AKIAIEF6HHISM7IMQ2SA',
    aws_secret_access_key='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',
    region_name="us-east-1"    
)

topic = client.create_topic(Name="IoTSNSTopic")

TopicArn='arn:aws:sns:us-east-1:207996986548:IoTSNSTopic'  # set its Amazon Resource Name
# Publish a message.
client.publish(Message="Good news everyone!", TopicArn=TopicArn)