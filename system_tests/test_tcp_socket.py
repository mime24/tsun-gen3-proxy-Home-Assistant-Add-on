# test_with_pytest.py and scapy
#
import pytest, socket, time

def get_sn() -> bytes:
    return b'R170000000000001'

def get_inv_no() -> bytes:
    return b'T170000000000001'

def get_invalid_sn():
    return b'R170000000000002'


@pytest.fixture
def msg_contact_info(): # Contact Info message
    return b'\x00\x00\x00\x2c\x10'+get_sn()+b'\x91\x00\x08solarhub\x0fsolarhub\x40123456'

@pytest.fixture
def msg_contact_resp(): # Contact Response message
    return b'\x00\x00\x00\x14\x10'+get_sn()+b'\x91\x00\x01'

@pytest.fixture
def msg_contact_info2(): # Contact Info message
    return b'\x00\x00\x00\x2c\x10'+get_invalid_sn()+b'\x91\x00\x08solarhub\x0fsolarhub\x40123456'

@pytest.fixture
def msg_contact_resp2(): # Contact Response message
    return b'\x00\x00\x00\x14\x10'+get_invalid_sn()+b'\x91\x00\x01'

@pytest.fixture
def msg_timestamp_req(): # Get Time Request message
    return b'\x00\x00\x00\x13\x10'+get_sn()+b'\x91\x22'           

@pytest.fixture
def msg_timestamp_resp(): # Get Time Resonse message
    return b'\x00\x00\x00\x1b\x10'+get_sn()+b'\x99\x22\x00\x00\x01\x89\xc6\x63\x4d\x80'

@pytest.fixture
def msg_controller_ind(): # Data indication from the controller
    msg  =  b'\x00\x00\x01\x2f\x10'+ get_sn() + b'\x91\x71\x0e\x10\x00\x00\x10'+get_sn()
    msg +=  b'\x01\x00\x00\x01\x89\xc6\x63\x55\x50'
    msg +=  b'\x00\x00\x00\x15\x00\x09\x2b\xa8\x54\x10\x52\x53\x57\x5f\x34\x30\x30\x5f\x56\x31\x2e\x30\x30\x2e\x30\x36\x00\x09\x27\xc0\x54\x06\x52\x61\x79\x6d\x6f'
    msg +=  b'\x6e\x00\x09\x2f\x90\x54\x0b\x52\x53\x57\x2d\x31\x2d\x31\x30\x30\x30\x31\x00\x09\x5a\x88\x54\x0f\x74\x2e\x72\x61\x79\x6d\x6f\x6e\x69\x6f\x74\x2e\x63\x6f\x6d\x00\x09\x5a\xec\x54'
    msg +=  b'\x1c\x6c\x6f\x67\x67\x65\x72\x2e\x74\x61\x6c\x65\x6e\x74\x2d\x6d\x6f\x6e\x69\x74\x6f\x72\x69\x6e\x67\x2e\x63\x6f\x6d\x00\x0d\x00\x20\x49\x00\x00\x00\x01\x00\x0c\x35\x00\x49\x00'
    msg +=  b'\x00\x00\x64\x00\x0c\x96\xa8\x49\x00\x00\x00\x1d\x00\x0c\x7f\x38\x49\x00\x00\x00\x01\x00\x0c\xfc\x38\x49\x00\x00\x00\x01\x00\x0c\xf8\x50\x49\x00\x00\x01\x2c\x00\x0c\x63\xe0\x49'
    msg +=  b'\x00\x00\x00\x00\x00\x0c\x67\xc8\x49\x00\x00\x00\x00\x00\x0c\x50\x58\x49\x00\x00\x00\x01\x00\x09\x5e\x70\x49\x00\x00\x13\x8d\x00\x09\x5e\xd4\x49\x00\x00\x13\x8d\x00\x09\x5b\x50'
    msg +=  b'\x49\x00\x00\x00\x02\x00\x0d\x04\x08\x49\x00\x00\x00\x00\x00\x07\xa1\x84\x49\x00\x00\x00\x01\x00\x0c\x50\x59\x49\x00\x00\x00\x4c\x00\x0d\x1f\x60\x49\x00\x00\x00\x00'
    return msg

@pytest.fixture
def msg_inv_data(): # Data indication from the controller
    msg  =  b'\x00\x00\x00\x8b\x10'+ get_sn() + b'\x91\x04\x01\x90\x00\x01\x10'+get_inv_no()
    msg +=  b'\x01\x00\x00\x01\x89\xc6\x63\x61\x08'
    msg +=  b'\x00\x00\x00\x06\x00\x00\x00\x0a\x54\x08\x4d\x69\x63\x72\x6f\x69\x6e\x76\x00\x00\x00\x14\x54\x04\x54\x53\x55\x4e\x00\x00\x00\x1E\x54\x07\x56\x35\x2e\x30\x2e\x31\x31\x00\x00\x00\x28'
    msg +=  b'\x54\x10\x54\x31\x37\x45\x37\x33\x30\x37\x30\x32\x31\x44\x30\x30\x36\x41\x00\x00\x00\x32\x54\x0a\x54\x53\x4f\x4c\x2d\x4d\x53\x36\x30\x30\x00\x00\x00\x3c\x54\x05\x41\x2c\x42\x2c\x43'
    return msg

@pytest.fixture
def msg_inverter_ind(): # Data indication from the inverter
    msg  = b'\x00\x00\x05\x02\x10'+ get_sn() + b'\x91\x04\x01\x90\x00\x01\x10'+get_inv_no()
    msg +=  b'\x01\x00\x00\x01\x89\xc6\x63\x61\x08'
    msg +=  b'\x00\x00\x00\xa3\x00\x00\x00\x64\x53\x00\x01\x00\x00\x00\xc8\x53\x00\x02\x00\x00\x01\x2c\x53\x00\x00\x00\x00\x01\x90\x49\x00\x00\x00\x00\x00\x00\x01\x91\x53\x00\x00'
    msg +=  b'\x00\x00\x01\x92\x53\x00\x00\x00\x00\x01\x93\x53\x00\x00\x00\x00\x01\x94\x53\x00\x00\x00\x00\x01\x95\x53\x00\x00\x00\x00\x01\x96\x53\x00\x00\x00\x00\x01\x97\x53\x00'
    msg +=  b'\x00\x00\x00\x01\x98\x53\x00\x00\x00\x00\x01\x99\x53\x00\x00\x00\x00\x01\x9a\x53\x00\x00\x00\x00\x01\x9b\x53\x00\x00\x00\x00\x01\x9c\x53\x00\x00\x00\x00\x01\x9d\x53'
    msg +=  b'\x00\x00\x00\x00\x01\x9e\x53\x00\x00\x00\x00\x01\x9f\x53\x00\x00\x00\x00\x01\xa0\x53\x00\x00\x00\x00\x01\xf4\x49\x00\x00\x00\x00\x00\x00\x01\xf5\x53\x00\x00\x00\x00'
    msg +=  b'\x01\xf6\x53\x00\x00\x00\x00\x01\xf7\x53\x00\x00\x00\x00\x01\xf8\x53\x00\x00\x00\x00\x01\xf9\x53\x00\x00\x00\x00\x01\xfa\x53\x00\x00\x00\x00\x01\xfb\x53\x00\x00\x00'
    msg +=  b'\x00\x01\xfc\x53\x00\x00\x00\x00\x01\xfd\x53\x00\x00\x00\x00\x01\xfe\x53\x00\x00\x00\x00\x01\xff\x53\x00\x00\x00\x00\x02\x00\x53\x00\x00\x00\x00\x02\x01\x53\x00\x00'
    msg +=  b'\x00\x00\x02\x02\x53\x00\x00\x00\x00\x02\x03\x53\x00\x00\x00\x00\x02\x04\x53\x00\x00\x00\x00\x02\x58\x49\x00\x00\x00\x00\x00\x00\x02\x59\x53\x00\x00\x00\x00\x02\x5a'
    msg +=  b'\x53\x00\x00\x00\x00\x02\x5b\x53\x00\x00\x00\x00\x02\x5c\x53\x00\x00\x00\x00\x02\x5d\x53\x00\x00\x00\x00\x02\x5e\x53\x00\x00\x00\x00\x02\x5f\x53\x00\x00\x00\x00\x02'
    msg +=  b'\x60\x53\x00\x00\x00\x00\x02\x61\x53\x00\x00\x00\x00\x02\x62\x53\x00\x00\x00\x00\x02\x63\x53\x00\x00\x00\x00\x02\x64\x53\x00\x00\x00\x00\x02\x65\x53\x00\x00\x00\x00'
    msg +=  b'\x02\x66\x53\x00\x00\x00\x00\x02\x67\x53\x00\x00\x00\x00\x02\x68\x53\x00\x00\x00\x00\x02\xbc\x49\x00\x00\x00\x00\x00\x00\x02\xbd\x53\x00\x00\x00\x00\x02\xbe\x53\x00'
    msg +=  b'\x00\x00\x00\x02\xbf\x53\x00\x00\x00\x00\x02\xc0\x53\x00\x00\x00\x00\x02\xc1\x53\x00\x00\x00\x00\x02\xc2\x53\x00\x00\x00\x00\x02\xc3\x53\x00\x00\x00\x00\x02\xc4\x53'
    msg +=  b'\x00\x00\x00\x00\x02\xc5\x53\x00\x00\x00\x00\x02\xc6\x53\x00\x00\x00\x00\x02\xc7\x53\x00\x00\x00\x00\x02\xc8\x53\x00\x00\x00\x00\x02\xc9\x53\x00\x00\x00\x00\x02\xca'
    msg +=  b'\x53\x00\x00\x00\x00\x02\xcb\x53\x00\x00\x00\x00\x02\xcc\x53\x00\x00\x00\x00\x03\x20\x53\x00\x00\x00\x00\x03\x84\x53\x50\x11\x00\x00\x03\xe8\x46\x43\x61\x66\x66\x00'
    msg +=  b'\x00\x04\x4c\x46\x3e\xeb\x85\x1f\x00\x00\x04\xb0\x46\x42\x48\x14\x7b\x00\x00\x05\x14\x53\x00\x17\x00\x00\x05\x78\x53\x00\x00\x00\x00\x05\xdc\x53\x02\x58\x00\x00\x06'
    msg +=  b'\x40\x46\x42\xd3\x66\x66\x00\x00\x06\xa4\x46\x42\x06\x66\x66\x00\x00\x07\x08\x46\x3f\xf4\x7a\xe1\x00\x00\x07\x6c\x46\x42\x81\x00\x00\x00\x00\x07\xd0\x46\x42\x06\x00'
    msg +=  b'\x00\x00\x00\x08\x34\x46\x3f\xae\x14\x7b\x00\x00\x08\x98\x46\x42\x36\xcc\xcd\x00\x00\x08\xfc\x46\x00\x00\x00\x00\x00\x00\x09\x60\x46\x00\x00\x00\x00\x00\x00\x09\xc4'
    msg +=  b'\x46\x00\x00\x00\x00\x00\x00\x0a\x28\x46\x00\x00\x00\x00\x00\x00\x0a\x8c\x46\x00\x00\x00\x00\x00\x00\x0a\xf0\x46\x00\x00\x00\x00\x00\x00\x0b\x54\x46\x3f\xd9\x99\x9a'
    msg +=  b'\x00\x00\x0b\xb8\x46\x41\x8a\xe1\x48\x00\x00\x0c\x1c\x46\x3f\x8a\x3d\x71\x00\x00\x0c\x80\x46\x41\x1b\xd7\x0a\x00\x00\x0c\xe4\x46\x3f\x1e\xb8\x52\x00\x00\x0d\x48\x46'
    msg +=  b'\x40\xf3\xd7\x0a\x00\x00\x0d\xac\x46\x00\x00\x00\x00\x00\x00\x0e\x10\x46\x00\x00\x00\x00\x00\x00\x0e\x74\x46\x00\x00\x00\x00\x00\x00\x0e\xd8\x46\x00\x00\x00\x00\x00'
    msg +=  b'\x00\x0f\x3c\x53\x00\x00\x00\x00\x0f\xa0\x53\x00\x00\x00\x00\x10\x04\x53\x55\xaa\x00\x00\x10\x68\x53\x00\x00\x00\x00\x10\xcc\x53\x00\x00\x00\x00\x11\x30\x53\x00\x00'
    msg +=  b'\x00\x00\x11\x94\x53\x00\x00\x00\x00\x11\xf8\x53\xff\xff\x00\x00\x12\x5c\x53\xff\xff\x00\x00\x12\xc0\x53\x00\x02\x00\x00\x13\x24\x53\xff\xff\x00\x00\x13\x88\x53\xff'
    msg +=  b'\xff\x00\x00\x13\xec\x53\xff\xff\x00\x00\x14\x50\x53\xff\xff\x00\x00\x14\xb4\x53\xff\xff\x00\x00\x15\x18\x53\xff\xff\x00\x00\x15\x7c\x53\x00\x00\x00\x00\x27\x10\x53'
    msg +=  b'\x00\x02\x00\x00\x27\x74\x53\x00\x3c\x00\x00\x27\xd8\x53\x00\x68\x00\x00\x28\x3c\x53\x05\x00\x00\x00\x28\xa0\x46\x43\x79\x00\x00\x00\x00\x29\x04\x46\x43\x48\x00\x00'
    msg +=  b'\x00\x00\x29\x68\x46\x42\x48\x33\x33\x00\x00\x29\xcc\x46\x42\x3e\x3d\x71\x00\x00\x2a\x30\x53\x00\x01\x00\x00\x2a\x94\x46\x43\x37\x00\x00\x00\x00\x2a\xf8\x46\x42\xce'
    msg +=  b'\x00\x00\x00\x00\x2b\x5c\x53\x00\x96\x00\x00\x2b\xc0\x53\x00\x10\x00\x00\x2c\x24\x46\x43\x90\x00\x00\x00\x00\x2c\x88\x46\x43\x95\x00\x00\x00\x00\x2c\xec\x53\x00\x06'
    msg +=  b'\x00\x00\x2d\x50\x53\x00\x06\x00\x00\x2d\xb4\x46\x43\x7d\x00\x00\x00\x00\x2e\x18\x46\x42\x3d\xeb\x85\x00\x00\x2e\x7c\x46\x42\x3d\xeb\x85\x00\x00\x2e\xe0\x53\x00\x03'
    msg +=  b'\x00\x00\x2f\x44\x53\x00\x03\x00\x00\x2f\xa8\x46\x42\x4d\xeb\x85\x00\x00\x30\x0c\x46\x42\x4d\xeb\x85\x00\x00\x30\x70\x53\x00\x03\x00\x00\x30\xd4\x53\x00\x03\x00\x00'
    msg +=  b'\x31\x38\x46\x42\x08\x00\x00\x00\x00\x31\x9c\x53\x00\x05\x00\x00\x32\x00\x53\x04\x00\x00\x00\x32\x64\x53\x00\x01\x00\x00\x32\xc8\x53\x13\x9c\x00\x00\x33\x2c\x53\x0f'
    msg +=  b'\xa0\x00\x00\x33\x90\x53\x00\x4f\x00\x00\x33\xf4\x53\x00\x66\x00\x00\x34\x58\x53\x03\xe8\x00\x00\x34\xbc\x53\x04\x00\x00\x00\x35\x20\x53\x00\x00\x00\x00\x35\x84\x53'
    msg +=  b'\x00\x00\x00\x00\x35\xe8\x53\x00\x00\x00\x00\x36\x4c\x53\x00\x00\x00\x01\x38\x80\x53\x00\x02\x00\x01\x38\x81\x53\x00\x01\x00\x01\x38\x82\x53\x00\x01\x00\x01\x38\x83'
    msg +=  b'\x53\x00\x00'     
    return msg

@pytest.fixture
def msg_ota_update_req(): # Over the air update request from talent cloud
    msg  = b'\x00\x00\x01\x16\x10'+ get_sn() + b'\x70\x13\x01\x02\x76\x35'
    msg += b'\x70\x68\x74\x74\x70'
    msg += b'\x3a\x2f\x2f\x77\x77\x77\x2e\x74\x61\x6c\x65\x6e\x74\x2d\x6d\x6f'
    msg += b'\x6e\x69\x74\x6f\x72\x69\x6e\x67\x2e\x63\x6f\x6d\x3a\x39\x30\x30'
    msg += b'\x32\x2f\x70\x72\x6f\x64\x2d\x61\x70\x69\x2f\x72\x6f\x6d\x2f\x75'
    msg += b'\x70\x64\x61\x74\x65\x2f\x64\x6f\x77\x6e\x6c\x6f\x61\x64\x3f\x76'
    msg += b'\x65\x72\x3d\x56\x31\x2e\x30\x30\x2e\x31\x37\x26\x6e\x61\x6d\x65'
    msg += b'\x3d\x47\x33\x2d\x57\x69\x46\x69\x2b\x2d\x56\x31\x2e\x30\x30\x2e'
    msg += b'\x31\x37\x2d\x4f\x54\x41\x26\x65\x78\x74\x3d\x30\x60\x68\x74\x74'
    msg += b'\x70\x3a\x2f\x2f\x77\x77\x77\x2e\x74\x61\x6c\x65\x6e\x74\x2d\x6d'
    msg += b'\x6f\x6e\x69\x74\x6f\x72\x69\x6e\x67\x2e\x63\x6f\x6d\x3a\x39\x30'
    msg += b'\x30\x32\x2f\x70\x72\x6f\x64\x2d\x61\x70\x69\x2f\x72\x6f\x6d\x2f'
    msg += b'\x75\x70\x64\x61\x74\x65\x2f\x63\x61\x6c\x6c\x62\x61\x63\x6b\x3f'
    msg += b'\x71\x69\x64\x3d\x31\x35\x30\x33\x36\x32\x26\x72\x69\x64\x3d\x32'
    msg += b'\x32\x39\x26\x64\x69\x64\x3d\x31\x33\x34\x32\x32\x35\x20\x36\x35'
    msg += b'\x66\x30\x64\x37\x34\x34\x62\x66\x33\x39\x61\x62\x38\x32\x34\x64'
    msg += b'\x32\x38\x62\x38\x34\x64\x31\x39\x65\x64\x33\x31\x31\x63\x06\x34'
    msg += b'\x36\x38\x36\x33\x33\x01\x31\x01\x30\x00'
    return msg


@pytest.fixture(scope="session")
def client_connection():
    host = 'logger.talent-monitoring.com'
    port = 5005
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.settimeout(1)
        yield s
        time.sleep(2.5)
        s.close()

def tempclient_connection():
    host = 'logger.talent-monitoring.com'
    port = 5005
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.settimeout(1)
        yield s
        s.close()

def test_open_close():
    try:
        for _ in tempclient_connection():
            pass  # test side effect of generator 
    except Exception:
        assert False

def test_send_contact_info1(client_connection, msg_contact_info, msg_contact_resp):
    s = client_connection
    try:
        s.sendall(msg_contact_info)
        data = s.recv(1024)
    except TimeoutError:
        pass
    assert data == msg_contact_resp


def test_send_contact_info2(client_connection, msg_contact_info2, msg_contact_info, msg_contact_resp):
    s = client_connection  
    try:
        s.sendall(msg_contact_info2)
        data = s.recv(1024)
    except TimeoutError:
        pass
    else: 
        assert False

    try:
        s.sendall(msg_contact_info)
        data = s.recv(1024)
    except TimeoutError:
        pass
    assert data == msg_contact_resp

def test_send_contact_info3(client_connection, msg_contact_info, msg_contact_resp, msg_timestamp_req):
    s = client_connection
    try:
        s.sendall(msg_contact_info)
        data = s.recv(1024)
    except TimeoutError:
        pass
    assert data == msg_contact_resp
    try:
        s.sendall(msg_timestamp_req)
        data = s.recv(1024)
    except TimeoutError:
        pass
 

def test_send_contact_resp(client_connection, msg_contact_resp):
    s = client_connection  
    try:
        s.sendall(msg_contact_resp)
        data = s.recv(1024)
    except TimeoutError:
        pass
    else:
        assert data == b''

def test_send_ctrl_data(client_connection, msg_timestamp_req, msg_timestamp_resp, msg_controller_ind):
    s = client_connection  
    try:
        s.sendall(msg_timestamp_req)
        _ = s.recv(1024)
    except TimeoutError:
        pass
  #  time.sleep(2.5)
  #  assert data == msg_timestamp_resp
    try:
        s.sendall(msg_controller_ind)
        _ = s.recv(1024)
    except TimeoutError:
        pass

def test_send_inv_data(client_connection, msg_timestamp_req, msg_timestamp_resp, msg_inv_data, msg_inverter_ind):
    s = client_connection  
    try:
        s.sendall(msg_timestamp_req)
        _ = s.recv(1024)
    except TimeoutError:
        pass
  #  time.sleep(32.5)
  #  assert data == msg_timestamp_resp
    try:
        s.sendall(msg_inv_data)
        _ = s.recv(1024)
        s.sendall(msg_inverter_ind)
        _ = s.recv(1024)
    except TimeoutError:
        pass

def test_ota_req(client_connection, msg_ota_update_req):
    s = client_connection  
    try:
        s.sendall(msg_ota_update_req)
        _ = s.recv(1024)
    except TimeoutError:
        pass
