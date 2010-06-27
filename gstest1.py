import os
import boto
import tempfile

"Load your developer keys from the .boto config file."
config = boto.config

"Create our bucket names."
bucket_names = ['peter_python'] # 'peter_dogs', 'peter_cats']

"Create a bucket URI for each bucket, and create the bucket with the bucket URI."
for bucket in bucket_names:
	print 'creating', bucket, 
	bucket_uri = boto.storage_uri(bucket, 'gs')
	print bucket_uri
	bucket_uri.create_bucket()
	
