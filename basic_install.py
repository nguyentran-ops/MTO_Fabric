#!/usr/bin/env python
from fabric.api import *
import getpass

#env.hosts = ['10.40.91.22']
##COCC #env.hosts = ['10.90.26.11','10.90.26.12','10.90.26.21','10.90.26.24','10.90.26.35','10.90.26.36','10.90.26.37','10.90.26.38','10.90.26.40','10.30.60.131','10.30.60.132']
##FarmeryMobile #env.hosts = ['10.30.81.31','10.30.81.32','10.30.81.34','10.30.60.110','10.30.60.33','10.30.60.34','10.30.60.35','10.30.60.36']
#env.hosts = ['10.13.39.2','10.13.39.3','10.13.39.5','10.30.60.48','10.30.60.152','10.30.60.105']
env.hosts = ['10.40.91.7']
env.key_filename = '/home/thinhnd2/.ssh/id_rsa'
env.user = 'thinhnd2'
env.password = getpass.getpass(prompt='Input passpharse: ')
#env.parallel = True
env.warn_only = True


# def g6repo():
# 	put('/home/thinhnd2/Documents/fabric/templates/repo_so6','/home/thinhnd2')
# 	run('mkdir /home/thinhnd2/repo_bk')
# 	sudo('mv /etc/yum.repos.d/* /home/thinhnd2/repo_bk/')
# 	sudo('cp -f /home/thinhnd2/repo_so6/* /etc/yum.repos.d/')
	#run('echo "10.30.70.55		g6repo.vng.com.vn" >> /etc/hosts')

def basic_install():
	put('/home/thinhnd2/Documents/fabric/templates/repo_so6','/home/thinhnd2')
	run('mkdir /home/thinhnd2/repo_bk')
	sudo('mv /etc/yum.repos.d/* /home/thinhnd2/repo_bk/')
	sudo('cp -f /home/thinhnd2/repo_so6/* /etc/yum.repos.d/')
	sudo('yum -y install vim-enhanced ntp telnet glibc.i686 tree lynx unzip nc')
	sudo('yum install -y so6-monitor')
	sudo("echo '\n# Monitor G6\n*/5 * * * * cd /G6Monitor/ClientSide && sh mon.sh  >/dev/null 2>&1' >> /var/spool/cron/root")
	sudo("echo '\n# Get listIP\n00 00 * * * cd /G6Monitor/webservice && /G6Monitor/ClientSide/php-app/bin/php getListIP.php >/dev/null 2>&1' >> /var/spool/cron/root")
	sudo("echo '\n# Server Type\n00 00 * * * cd /G6Monitor/ClientSide/ && /G6Monitor/ClientSide/php-app/bin/php G6MonitorClient_typeserver.php >/dev/null 2>&1' >> /var/spool/cron/root")
	sudo("echo '\n# Monitor log message\n00 * * * * cd /G6Monitor/ClientSide  && /G6Monitor/ClientSide/php-app/bin/php  G6MonitorSecure.php \"M j\" >/dev/null 2>&1' >> /var/spool/cron/root")
	sudo("echo '\n# Hardware Monitor\n*/5 * * * * cd /G6Monitor/ServiceMonitor && /G6Monitor/ClientSide/php-app/bin/php HardwareMon.php  >/dev/null 2>&1' >> /var/spool/cron/root")
	##sudo("echo -e '\n################web tunning##############\nnet.core.rmem_max=8388608\nnet.core.wmem_max=8388608\nnet.core.rmem_default=65536\nnet.core.wmem_default=65536\nnet.ipv4.tcp_rmem = 4096 87380 50331648\nnet.ipv4.tcp_wmem = 4096 65536 50331648\nnet.ipv4.tcp_mem = 8388608 16777216 25165824\nnet.ipv4.route.flush=1\nnet.core.somaxconn=65536\nnet.ipv4.tcp_fin_timeout = 1\nnet.ipv4.tcp_tw_reuse = 1\nnet.ipv4.tcp_tw_recycle = 1\nnet.core.netdev_max_backlog = 262144\nnet.ipv4.ip_local_port_range = 1024 65023\nnet.ipv4.udp_rmem_min=16384 \nnet.ipv4.udp_wmem_min=16384\nnet.ipv4.tcp_max_orphans = 262144\nnet.ipv4.tcp_max_syn_backlog = 262144\nnet.ipv4.tcp_synack_retries = 3\nnet.ipv4.tcp_syn_retries = 3' >> /etc/sysctl.conf")
	##sudo("sudo /sbin/sysctl -p")
	##sudo("echo -e '\n################web tunning##############\nnet.core.rmem_max=8388608\nnet.core.wmem_max=8388608\nnet.core.rmem_default=65536\nnet.core.wmem_default=65536\nnet.ipv4.tcp_rmem = 4096 87380 50331648\nnet.ipv4.tcp_wmem = 4096 65536 50331648\nnet.ipv4.tcp_mem = 8388608 16777216 25165824\nnet.ipv4.route.flush=1\nnet.core.somaxconn=65536\nnet.ipv4.tcp_fin_timeout = 1\nnet.ipv4.tcp_tw_reuse = 1\nnet.ipv4.tcp_tw_recycle = 1\nnet.core.netdev_max_backlog = 262144\nnet.ipv4.ip_local_port_range = 1024 65023\nnet.ipv4.udp_rmem_min=16384 \nnet.ipv4.udp_wmem_min=16384\nnet.ipv4.tcp_max_orphans = 262144\nnet.ipv4.tcp_max_syn_backlog = 262144\nnet.ipv4.tcp_synack_retries = 3\nnet.ipv4.tcp_syn_retries = 3' >> /etc/rc.local")
	##sudo("echo -e '###########Socket Tuning############\nnet.ipv4.tcp_fin_timeout = 10\nnet.ipv4.tcp_tw_reuse = 1\nnet.ipv4.tcp_tw_recycle = 1\nnet.ipv4.ip_default_ttl = 128\nnet.ipv4.icmp_echo_ignore_broadcasts = 1\nnet.ipv4.tcp_keepalive_time = 300\n#Maximal number of timewait sockets held by system simultaneously\nnet.ipv4.tcp_max_tw_buckets = 10024\n#Maximal number of TCP sockets not attached to any user file handle\nnet.ipv4.tcp_max_orphans = 262144\n#Number of times SYNACKs for a passive TCP connection\nnet.ipv4.tcp_synack_retries = 3\n#Number of times initial SYNs for an active TCP connection\nnet.ipv4.tcp_syn_retries = 2\nnet.core.rmem_max = 50331648\nnet.core.rmem_default = 50331648\n#syn queue\nnet.core.netdev_max_backlog = 262144\n#Concurrent syn\nnet.core.somaxconn = 262144\nnet.ipv4.tcp_rmem = 4096 87380 50331648\nnet.ipv4.tcp_wmem = 4096 65536 50331648\nnet.ipv4.tcp_mem = 8388608 16777216 25165824\n#Maximal number of remembered connection requests, which have not\n#received an acknowledgment from connecting client.\nnet.ipv4.tcp_max_syn_backlog = 10240\nfs.file-max = 4843582\nnet.ipv4.udp_rmem_min=16384\nnet.ipv4.udp_wmem_min=16384' >> /etc/sysctl.conf")
	##sudo("sudo /sbin/sysctl -p")
	##sudo("echo -e '###########Socket Tuning############\nnet.ipv4.tcp_fin_timeout = 10\nnet.ipv4.tcp_tw_reuse = 1\nnet.ipv4.tcp_tw_recycle = 1\nnet.ipv4.ip_default_ttl = 128\nnet.ipv4.icmp_echo_ignore_broadcasts = 1\nnet.ipv4.tcp_keepalive_time = 300\n#Maximal number of timewait sockets held by system simultaneously\nnet.ipv4.tcp_max_tw_buckets = 10024\n#Maximal number of TCP sockets not attached to any user file handle\nnet.ipv4.tcp_max_orphans = 262144\n#Number of times SYNACKs for a passive TCP connection\nnet.ipv4.tcp_synack_retries = 3\n#Number of times initial SYNs for an active TCP connection\nnet.ipv4.tcp_syn_retries = 2\nnet.core.rmem_max = 50331648\nnet.core.rmem_default = 50331648\n#syn queue\nnet.core.netdev_max_backlog = 262144\n#Concurrent syn\nnet.core.somaxconn = 262144\nnet.ipv4.tcp_rmem = 4096 87380 50331648\nnet.ipv4.tcp_wmem = 4096 65536 50331648\nnet.ipv4.tcp_mem = 8388608 16777216 25165824\n#Maximal number of remembered connection requests, which have not\n#received an acknowledgment from connecting client.\nnet.ipv4.tcp_max_syn_backlog = 10240\nfs.file-max = 4843582\nnet.ipv4.udp_rmem_min=16384\nnet.ipv4.udp_wmem_min=16384' >> /etc/rc.local")
	sudo("echo -e '########membase tunning##########\nnet.core.rmem_max=8388608\nnet.core.wmem_max=8388608\nnet.core.rmem_default=65536\nnet.core.wmem_default=65536\nnet.ipv4.tcp_rmem=4096 87380 838860\nnet.ipv4.tcp_wmem=4096 65536 8388608\nnet.ipv4.tcp_mem=8388608 8388608 8388608\nnet.ipv4.route.flush=1\nnet.core.somaxconn=65536\nnet.core.netdev_max_backlog=3000\nnet.core.optmem_max=10000000\nnet.ipv4.ip_local_port_range = 1024 65023' >> /etc/sysctl.conf")
	sudo("sudo /sbin/sysctl -p")
	sudo("echo -e '########membase tunning##########\nnet.core.rmem_max=8388608\nnet.core.wmem_max=8388608\nnet.core.rmem_default=65536\nnet.core.wmem_default=65536\nnet.ipv4.tcp_rmem=4096 87380 838860\nnet.ipv4.tcp_wmem=4096 65536 8388608\nnet.ipv4.tcp_mem=8388608 8388608 8388608\nnet.ipv4.route.flush=1\nnet.core.somaxconn=65536\nnet.core.netdev_max_backlog=3000\nnet.core.optmem_max=10000000\nnet.ipv4.ip_local_port_range = 1024 65023' >> /etc/rc.local")
	sudo("echo -e '*       soft    nofile  1000000\n*       hard    nofile  1000000' >> /etc/security/limits.conf")
	sudo("sudo ulimit -n 1000000")
	sudo("echo '\nrocommunity g6comm 10.30.70.12\ntrapsink 10.30.70.12 g6comm' >> /etc/snmp/snmpd.conf")
	sudo("/etc/init.d/snmpd restart")
	sudo('chkconfig snmpd --level 35 on')
	sudo('yum install -y so6-agent')	
	sudo('/bin/sh /SO6ServerAgent/Control.sh start')
	sudo('echo "\n/SO6ServerAgent/Control.sh start" >> /etc/rc.local')


def config_ssh():
	sudo("mv -fv /etc/ssh/sshd_config /etc/ssh/sshd_config.luu")
	#run("echo -e 'UseDNS no\nKerberosAuthentication no\nGSSAPIAuthentication no\nPermitRootLogin no\nPubkeyAuthentication yes\nPasswordAuthentication no\nAuthorizedKeysFile      .ssh/authorized_keys\n\n' | sudo tee -a /etc/ssh/sshd_config")
	sudo("echo -e 'UseDNS no\nKerberosAuthentication no\nGSSAPIAuthentication no\nPermitRootLogin no\nPubkeyAuthentication yes\nPasswordAuthentication no\nAuthorizedKeysFile      .ssh/authorized_keys\n\n' >> /etc/ssh/sshd_config")
	sudo("cat /etc/ssh/sshd_config")
	sudo("cat /etc/ssh/sshd_config.luu >> /etc/ssh/sshd_config")
	sudo("/etc/init.d/sshd restart")
