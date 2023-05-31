Error: MonitoredItemCreateRequest.__init__() got an unexpected keyword argument 'subscription'
ServiceFault from server received while waiting for publish response
exception calling callback for <Future at 0x20606c23310 state=finished returned Buffer>
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\concurrent\futures\_base.py", line 342, in _invoke_callbacks
    callback(self)
  File "C:\Users\40020507\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\opcua\client\ua_client.py", line 493, in _call_publish_callback
    self._uasocket.check_answer(data, "while waiting for publish response")
  File "C:\Users\40020507\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\opcua\client\ua_client.py", line 93, in check_answer
    hdr.ServiceResult.check()
  File "C:\Users\40020507\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\opcua\ua\uatypes.py", line 218, in check
    raise UaStatusCodeError(self.value)
opcua.ua.uaerrors._auto.BadSessionClosed: "The session was closed by the client."(BadSessionClosed)
Client disconnected
from opcua import Client, ua, uamethod
from opcua.ua import NodeId, ua_binary as uabin

def subscribe_to_values(subscription, data_change_notification):
    print("Data change from server:")
    for item in data_change_notification.MonitoredItems:
        node_id = item.ClientHandle
        data_value = item.Value.Value
        print(f"Item {node_id}, Value = {data_value}")

def on_session_closed(session, reason):
    print(f"Session closed: {reason}")
    # Add any necessary handling here

if __name__ == '__main__':
    client = Client("opc.tcp://MYTSL02946.lnties.com:53530/OPCUA/SimulationServer")
    
    try:
        client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate.pem,private-key.pem")
        client.application_uri = "urn:RustClient"
        
        client.on_session_closed = on_session_closed
        
        client.connect()
        print("Client connected")
        
        # Create a subscription
        subscription = client.create_subscription(2000, ua.SubscriptionDiagnosticsDataType())
        
        # Create some monitored items
        items_to_create = [
            ua.MonitoredItemCreateRequest(
                NodeId(3, 1003), ua.AttributeIds.Value, client_handle=1
            ),
            ua.MonitoredItemCreateRequest(
                NodeId(3, 1008), ua.AttributeIds.Value, client_handle=2
            ),
            ua.MonitoredItemCreateRequest(
                NodeId(3, 1009), ua.AttributeIds.Value, client_handle=3
            ),
            ua.MonitoredItemCreateRequest(
                NodeId(3, 1010), ua.AttributeIds.Value, client_handle=4
            )
        ]
        client.create_monitored_items(subscription, items_to_create)
        
        # Write a value to a node
        node_id = NodeId(3, 1012)
        value = uabin.Variant(20, uabin.VariantType.Int32)
        client.write_attribute_value(node_id, ua.AttributeIds.Value, value)
        print("Value written successfully")
        
        # Subscribe to data change notifications
        subscription.subscribe_data_change(subscribe_to_values)
        
        # Keep the script running to receive data change notifications
        while True:
            pass
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client.disconnect()
        print("Client disconnected")
