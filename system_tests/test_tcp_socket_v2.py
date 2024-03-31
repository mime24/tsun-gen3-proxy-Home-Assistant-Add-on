# test_with_pytest.py and scapy
#
import pytest, socket, time, os
from dotenv import load_dotenv

#from scapy.all import *
#from scapy.layers.inet import IP, TCP, TCP_client

load_dotenv()

SOLARMAN_SNR = os.getenv('SOLARMAN_SNR', '00000080')

def get_sn() -> bytes:
    return bytes.fromhex(SOLARMAN_SNR)

def get_inv_no() -> bytes:
    return b'T170000000000001'

def get_invalid_sn():
    return b'R170000000000002'


@pytest.fixture
def MsgContactInfo(): # Contact Info message
    msg  = b'\xa5\xd4\x00\x10\x41\x00\x01' +get_sn()  +b'\x02\xba\xd2\x00\x00'
    msg += b'\x19\x00\x00\x00\x00\x00\x00\x00\x05\x3c\x78\x01\x64\x01\x4c\x53'
    msg += b'\x57\x35\x42\x4c\x45\x5f\x31\x37\x5f\x30\x32\x42\x30\x5f\x31\x2e'
    msg += b'\x30\x35\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x40\x2a\x8f\x4f\x51\x54\x31\x39\x32\x2e'
    msg += b'\x31\x36\x38\x2e\x38\x30\x2e\x34\x39\x00\x00\x00\x0f\x00\x01\xb0'
    msg += b'\x02\x0f\x00\xff\x56\x31\x2e\x31\x2e\x30\x30\x2e\x30\x42\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xfe\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x41\x6c\x6c\x69\x75\x73\x2d\x48\x6f'
    msg += b'\x6d\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3c'
    msg += b'\x15'
    return msg

@pytest.fixture
def MsgContactResp(): # Contact Response message
    msg  = b'\xa5\x0a\x00\x10\x11\x01\x01' +get_sn()  +b'\x02\x01\x6a\xfd\x8f'
    msg += b'\x65\x3c\x00\x00\x00\x75\x15'
    return msg

@pytest.fixture
def MsgDataInd(): 
    msg  = b'\xa5\x99\x01\x10\x42\x59\x84' +get_sn()  +b'\x01\xb0\x02\x2c\x87'
    msg += b'\x22\x32\xb7\x29\x00\x00\xd6\xcf\xe1\x33\x01\x00\x0c\x05\x00\x00'
    msg += b'\x59\x31\x37\x45\x37\x41\x30\x46\x30\x31\x30\x42\x30\x31\x33\x45'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x01\x12\x02\x12\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x40\x10\x08\xd8\x00\x09\x13\x84\x00\x35\x00\x00\x02\x58\x00\xd8'
    msg +=  b'\x01\x3f\x00\x17\x00\x4d\x01\x44\x00\x14\x00\x43\x01\x45\x00\x18'
    msg += b'\x00\x52\x00\x12\x00\x01\x00\x00\x00\x7c\x00\x00\x24\xed\x00\x2c'
    msg += b'\x00\x00\x0b\x10\x00\x26\x00\x00\x0a\x0f\x00\x30\x00\x00\x0b\x76'
    msg += b'\x00\x00\x00\x00\x06\x16\x00\x00\x00\x00\x55\xaa\x00\x01\x00\x00'
    msg += b'\x00\x00\x00\x00\xff\xff\x07\xd0\x00\x03\x04\x00\x04\x00\x04\x00'
    msg += b'\x04\x00\x00\x01\xff\xff\x00\x01\x00\x06\x00\x68\x00\x68\x05\x00'
    msg += b'\x09\xcd\x07\xb6\x13\x9c\x13\x24\x00\x01\x07\xae\x04\x0f\x00\x41'
    msg += b'\x00\x0f\x0a\x64\x0a\x64\x00\x06\x00\x06\x09\xf6\x12\x8c\x12\x8c'
    msg += b'\x00\x10\x00\x10\x14\x52\x14\x52\x00\x10\x00\x10\x01\x51\x00\x05'
    msg += b'\x04\x00\x00\x01\x13\x9c\x0f\xa0\x00\x4e\x00\x66\x03\xe8\x04\x00'
    msg += b'\x09\xce\x07\xa8\x13\x9c\x13\x26\x00\x00\x00\x00\x00\x00\x00\x00'
    msg += b'\x00\x00\x00\x00\x04\x00\x04\x00\x00\x00\x00\x00\xff\xff\x00\x00'
    msg += b'\x00\x00\x00\x00\x24\x15'
    return msg

@pytest.fixture
def MsgDataResp(): # Contact Response message
    msg  = b'\xa5\x0a\x00\x10\x12\x80\x84' +get_sn()  +b'\x01\x01\xd1\x96\x04'
    msg += b'\x66\x3c\x00\x00\x00\xed\x15'
    return msg




@pytest.fixture(scope="session")
def ClientConnection():
    #host = '172.16.30.7'
    host = 'logger.talent-monitoring.com'
    #host = 'iot.talent-monitoring.com'
    #host = '127.0.0.1'
    port = 10000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.settimeout(1)
        yield s
        s.close()

def checkResponse(data, Msg):
    check = bytearray(data)
    check[5]= Msg[5]            # ignore seq
    check[13:17]= Msg[13:17]    # ignore timestamp
    check[21]= Msg[21]          # ignore crc
    assert check == Msg


def tempClientConnection():
    #host = '172.16.30.7'
    host = 'logger.talent-monitoring.com'
    #host = 'iot.talent-monitoring.com'
    #host = '127.0.0.1'
    port = 10000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.settimeout(1)
        yield s
        time.sleep(2.5)
        s.close()

def test_open_close():
    try:
        for s in tempClientConnection():
            pass
    except:
        assert False
    assert True

def test_conn_msg(ClientConnection,MsgContactInfo, MsgContactResp):
    s = ClientConnection
    try:
        s.sendall(MsgContactInfo)
        # time.sleep(2.5)
        data = s.recv(1024)
    except TimeoutError:
        pass
    # time.sleep(2.5)
    checkResponse(data, MsgContactResp)

def test_data_ind(ClientConnection,MsgDataInd, MsgDataResp):
    s = ClientConnection
    try:
        s.sendall(MsgDataInd)
        # time.sleep(2.5)
        data = s.recv(1024)
    except TimeoutError:
        pass
    # time.sleep(2.5)
    checkResponse(data, MsgDataResp)