import luna
#net = luna.Network(create = True, name = 'internal', NETWORK = '192.168.1.0', PREFIX = 24)
net = luna.Network('internal')
print net.absnum_to_ip(3232235776)
print net.ip_to_absnum('192.168.3.3')
print net.ip_to_absnum('192.168.3.300')
print net.ip_in_net('10.10.10.10')
print net.ip_in_net('192.168.1.300')
net.set('NETWORK', '192.168.1.0')
print net.get('NETWORK')
print net.get('PREFIX')
net.set('NETWORK', '10.10.10.10')
print net.get('NETWORK')
print net.get('PREFIX')
net.set('PREFIX', 16)
print net.get('NETWORK')
print net.get('PREFIX')
net.set('PREFIX', 24)
print net.get('NETWORK')
print net.get('PREFIX')
print net.get_used_ips()