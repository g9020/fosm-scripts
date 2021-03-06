import os
from gtm import GTM

if __name__=="__main__":
	#Get the call in table file
	if 'gtm_access_ci' not in os.environ:
		print "Please set environment variable gtm_access_ci to the location of gtm_access.ci"
		exit(0)
	if not os.path.exists(os.environ['gtm_access_ci']):
		print "Error: {0} does not exist".format(os.environ['gtm_access_ci'])
		exit(0)
	os.environ['GTMCI'] = os.environ['gtm_access_ci']

	#Change working folder to database location
	if 'gtm_data_dir' not in os.environ:
		print "Please set environment variable gtm_data_dir to the data folder"
	if not os.path.exists(os.environ['gtm_data_dir']):
		print "Error: {0} does not exist".format(os.environ['gtm_data_dir'])
		exit(0)
	os.chdir(os.environ['gtm_data_dir'])

	db = GTM()

	print "Enter email"
	username = raw_input()

	print "Enter password"
	password = raw_input()

	db.execute('d loginLowLevel^user("{0}","{1}")'.format(username, password))

	print "authenticated=",db.get('%sess("authenticated")')
	print "uid=",db.get('%sess("uid")')

