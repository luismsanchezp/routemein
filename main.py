from Library.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.RmiIPv4Lib import IPv4 as ip
from Library.RmiDeviceLib import device
from Library.RmiNetworkLib import network
from Library.RmiAddressingLib import addressing

print(bnh.int_to_bin(255))

print(bnh.sum('10000', '10000'))

for i in range(256):
    print(ip(i, i, i, i))

print(ip(254, 254, 254, 254).get_binary_string())
one = ip(32, 64, 32, 0)
one.set_ip_value_binary_str('11111100111111001111110011111100')
print(one)
one = ip(32, 64, 32, 0)
print(one)
print(one.get_binary_string())

router = device('Cisco 1')
router1 = device('Cisco 2')
host = device('Apple TV')

wan = network(0, 4)
lan = network(1, 200)

wan.network_ip = ip(200, 10, 4, 24)
wan.mask = ip(255, 255, 255, 248)

print('wan ip: '+wan.get_network_ip())
print('wan mask: '+wan.get_mask())

wan.add_device(router)
router.serial.append(wan)
print('router ip: '+wan.get_device_ip('Cisco 1')+' in serial '+router.get_interface_port(0))
wan.add_device(router1)
router1.serial.append(wan)
print('router ip: '+wan.get_device_ip('Cisco 2')+' in serial '+router1.get_interface_port(1))

print(network.create_network_mask_reserved_bits(12))

lan1 = network(1, 3850)
lan2 = network(1, 1900)
lan3 = network(1, 50)
lan4 = network(1, 11)

nets = [lan1,lan2,lan3,lan4]

addressing.address_list(nets)

i = 1
for n in nets:
    print('net '+str(i)+' - ip: '+str(n.network_ip)+' | mask: '+str(n.mask))
    i=i+1

print('\n')

wan1 = network(0, 4)
wan2 = network(0, 4)
wan3 = network(0, 4)
wan4 = network(0, 4)

nets1 = [wan1,wan2,wan3,wan4]

addressing.address_list(nets1)

i = 1
for n in nets1:
    print('net '+str(i)+' - ip: '+str(n.network_ip)+' | mask: '+str(n.mask))
    i=i+1