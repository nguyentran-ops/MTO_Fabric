#!/usr/bin/env python
from fabric.api import *
import getpass

#env.hosts = ['10.30.67.3','10.30.67.30','10.30.67.32','10.30.67.17','10.30.67.9'] #Dao Rong
env.hosts = ['10.30.60.33','10.30.60.34','10.30.60.35','10.30.60.36','10.30.60.110']
env.key_filename = '/home/thinhnd2/.ssh/id_rsa'
#env.password = getpass.getpass(prompt='Input passpharse: ')
#env.parallel = True

#def addkey():
#	put('/home/thinhnd2/test_addkey.py','/home/thinhnd2/')
#	with cd('/home/thinhnd2'):
#		run('python test_addkey.py')

def install_splunk():
	#with cd('/home/thinhnd2'):
	#	run('sudo rm -rfv linux_log_install')
	#	run('sudo rm -fv linux_log_install.zip')
	#	run('wget --no-check-certificate  https://10.30.49.2/splunk/download/linux_log_install.zip')
	#	run('unzip linux_log_install.zip')
	with cd('/home/thinhnd2/linux_log_install'):
		run('sudo /bin/sh install_splunkforwarder.sh -int')
		
def test_splunk():
	with cd('/home/thinhnd2/linux_log_install'):
		run('sudo /bin/sh test_splunkforwarder.sh -int')


