import opcua
from opcua import ua

def subscribe_to_values(session):
    # Create a subscription
    subscription = session.create_subscription(100, ua.SubscriptionDiagnosticsDataType())
    # Create a monitored item
    node = session.get_node("ns=2;s=Temperature")
    handle = subscription.subscribe_data_change(node)
    return subscription, handle

if __name__ == "__main__":
    client = opcua.Client("opc.tcp://MYTSL02946.lnties.com:53530/OPCUA/SimulationServer")
    client.set_security_string("None")
    client.connect()
    print("Client created")
    session = client.create_session()
    print("Session created")
    subscription, handle = subscribe_to_values(session)
    print("Subscribed")
    try:
        while True:
            pass
    finally:
        subscription.unsubscribe(handle)
        session.close()
        client.disconnect()
        
        Traceback (most recent call last):
  File "d:\OneDrive - LTTS\Desktop\opc\opcrust.py", line 14, in <module>
    client.set_security_string("None")
  File "C:\Users\40020507\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\opcua\client\client.py", line 188, in set_security_string
    raise ua.UaError('Wrong format: `{0}`, expected at least 4 comma-separated values'.format(string))
opcua.ua.uaerrors._base.UaError: Wrong format: `None`, expected at least 4 comma-separated values
        
        
        Traceback (most recent call last):
  File "d:\OneDrive - LTTS\Desktop\opc\opcrust.py", line 14, in <module>
    client.set_security_string("Basic256,None,None,None")
  File "C:\Users\40020507\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\opcua\client\client.py", line 190, in set_security_string
    mode = getattr(ua.MessageSecurityMode, parts[1])
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\enum.py", line 437, in __getattr__
    raise AttributeError(name) from None
AttributeError: None. Did you mean: 'None_'?

