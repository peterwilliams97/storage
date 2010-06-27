import os
import boto
import tempfile

"Load your developer keys from the .boto config file."
config = boto.config
	
"Create a URI, but don't specify a bucket or object because you are listing buckets."
uri = boto.storage_uri('', 'gs')

print 'List all my buckets'
buckets = uri.get_all_buckets()
for bucket in buckets:
	print '', bucket.name
	
print 'List all my buckets in detail'
buckets = uri.get_all_buckets()
for bucket in buckets:
	print '', bucket