
def testtest():
    print("yoyo")


from pylogix import PLC

def discoverTags():
    with PLC() as comm:
        comm.IPAddress = '192.168.100.103'
        tags = comm.GetTagList()
        print(tags)
discoverTags()

# with open('tag_list.txt', 'w') as f:
#     for t in tags.Value:
#         f.write('%s %d \n'.format(t.TagName, t.DataType))


def devices():
    with PLC() as comm:
        devices = comm.Discover()
        for device in devices.Value:
            print(device.IPAddress)
            print('  Product Code: ' + device.ProductName + " " + str(device.ProductCode))
            print('  Vendor/Device ID:' + device.Vendor + " " + str(device.DeviceID))
            print('  Revision/Serial:' + device.Revision + " " + device.SerialNumber)
            print('')



def discover():
    with PLC() as comm:
        devices = comm.Discover()
        return(devices)

