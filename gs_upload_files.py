"""
	Based on http://code.google.com/apis/storage/docs/gspythonlibrary.html
"""
import os, boto, tempfile

def findFilesWithExt(dir, files_list, ext, body = None):
    """ Returns a list of the paths of all files in 'files_list' in and under 'dir' with 
        extension 'ext' and body containing 'body' """
    all_files = []
    for f in files_list:
        if os.path.splitext(f)[1] == ext and (body == None or body in os.path.splitext(f)[0]):
            all_files.append(os.path.join(dir, f))
    return all_files    
   
def findAllFilesWithExt(dir, ext, body = None): 
    """ Returns a list of the paths of all files in and under 'dir' with 
        extension 'ext' and body containing 'body' """
    all_files = []
    for root, dirs, files_list in os.walk(dir):
		if not '.git' in root and not 'gsuti' in root and not './' in root:
			#print '\t', root #, dirs, files_list
			all_files = all_files + findFilesWithExt(root, files_list, ext, body)
    return all_files  

def printList(name, the_list):
	llist = the_list[:]
	llist.sort()
	print '%3d'%len(llist), name
	for i,entry in enumerate(llist):
		print ' ', i, entry
		
def getPythonFileList():
	""" Returns a list of python files from Peter's Windows laptop """
	# root = '/cygdrive/c/dev'
	root = '/cygdrive/c/Users/peter/workspace/exercises'
	ext = '.py'
	print 'findAllFilesWithExt', root, ext
	all_py = findAllFilesWithExt(root, ext)
	printList('all python files under ' + root, all_py)
	return all_py
		
if __name__ == '__main__':
	"Get your developer keys from the .boto config file."
	config = boto.config

	"Create a list of files to upload."
	file_names = getPythonFileList()

	"Specify the bucket you are uploading to."
	bucket_name = 'peter_python'

	print 'uploading files to ', bucket_name
	"Upload the files."
	for name in file_names:
		"Create source and destination URIs."
		print '  uploading', name
		src_uri = boto.storage_uri(name, 'file')
		dst_uri = boto.storage_uri(bucket_name, 'gs')

		"Create a new destination URI with the source file name as the object name."
		new_dst_uri = dst_uri.clone_replace_name(src_uri.object_name)
		print '    destination uri =', new_dst_uri

		"Create a new destination key object."
		dst_key = new_dst_uri.new_key()

		"Retrieve the source key and create a source key object."
		src_key = src_uri.get_key()

		"Create a temporary file to hold your copy operation."
		tmp = tempfile.TemporaryFile()
		src_key.get_file(tmp)
		tmp.seek(0)

		"Upload the file."
		dst_key.set_contents_from_file(tmp)
		
	print len(file_names), 'new files in ', bucket_name
		