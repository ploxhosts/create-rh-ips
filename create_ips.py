# Seperate IPs by a comma
node_ips = [
'123.123.123.2',
'123.123.123.3'
]
gateway = "123.123.123.1"
network_device = "eno1"
prefix_size = "24"

# do not edit
count = 0

for ips in node_ips:
    print("Creating config for " + ips)

    # write file
    f = open("/etc/sysconfig/network-scripts/ifcfg-{0}:{1}".format(network_device,count), "a")
    f.write("DEVICE={0}:{1}\nONBOOT=yes\nIPADDR={2}\nPREFIX={3}\nGATEWAY={4}".format(network_device,count,ips,prefix_size,gateway))
    f.close()

    count = count + 1
