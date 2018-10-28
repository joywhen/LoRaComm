import serial
import time

# ser = serial.Serial()
# ser.port = '/dev/tty.usbserial-1410'
# # ser.port = '/dev/tty.SLAB_USBtoUART'
# ser.baudrate = 115200
# ser.bytesize = serial.EIGHTBITS
# ser.stopbits = serial.STOPBITS_ONE
# ser.parity = serial.PARITY_NONE
# ser.xonxoff = False
# ser.timeout = 1
# ser.open()
# if ser.is_open:
#     # ser.write(b'at+reload\r\n')
#     # time.sleep(0.5)
#     # data = ser.read(100)
#     # print(data)
#     ser.write(b'at+reset=0\r\n')
#     time.sleep(0.5)
#     data = ser.read(100)
#     print(data)
#     ser.write(b'at+reload\r\n')
#     time.sleep(0.5)
#     data = ser.read(100)
#     print(data)
#     ser.write(b'at+mode=0\r\n')
#     time.sleep(0.5)
#     data = ser.read(100)
#     print(data)
#     # ser.write(b'at+get_config=ch_list\r\n')
#     # data = ser.read(10000)
#     # print(data)
#     ser.write(b'at+set_config=dev_addr:2604127F&nwks_key:6458B96076139234EAD79D7033C9A563&apps_key:444B3D2FDCD9C5F3D3E82BE86976F886&tx_power:20\r\n')
#     time.sleep(1)
#     data = ser.read(100)
#     print(data)
#     ser.write(b'at+join=abp\r\n')
#     time.sleep(1)
#     data = ser.read(100)
#     print(data)
#
#     ser.write(b'at+send=1,2,AABBCCDDEEFF\r\n')
#     time.sleep(1)
#     data = ser.read(100)
#     print(data)
#
#     ser.close()


import lora.lora as l

lo = l.LoRa()

lo.port = '/dev/tty.usbserial-14140'
lo.baudrate = 115200
lo.bytesize = serial.EIGHTBITS
lo.stopbits = serial.STOPBITS_ONE
lo.parity = serial.PARITY_NONE
lo.xonxoff = False

# connect
lo.connect()

# send message without gateway wait
lo.send_message(b'AABBCCDDEEFFAAAABBCCDD')

lo.get_signal()

# disconnect
lo.disconnect()
