from opcua import Client, ua
from opcua.common.callback import DataChangeCallback
from opcua.common.subscription import Subscription
from opcua.common.node import NodeId


def main():
    client = Client("opc.tcp://MYTSL02946.lnties.com:53530/OPCUA/SimulationServer")
    client.application_name = "PYTHON-OPCUA-Client"
    client.application_uri = "urn:PythonClient"
    client.set_security_string("None")
    client.session_timeout = 60000
    client.connect()
    print("Client created")
    # Create a subscription and monitored items
    if subscribe_to_values(client).is_ok():
        print("Subscribed")
        client.create_subscription(2000.0, 10, 30)
    else:
        print("Error creating subscription")

def subscribe_to_values(client):
    # Create a subscription polling every 2s with a callback
    subscription = Subscription(client, 2000.0)
    subscription.subscribe_data_change(DataChangeCallback(print_value))
    subscription.create()
    # Create some monitored items
    items_to_create = [1003, 1008, 1009, 1010]
    nodes_to_monitor = [NodeId(3, item) for item in items_to_create]
    subscription.create_monitored_items(0, ua.TimestampsToReturn.Both, nodes_to_monitor)
    # Write a value to a node
    node_id = NodeId(3, 1012)
    value = ua.Variant(20, ua.VariantType.UInt16)
    client.write_value(node_id, value)
    print("Created")
    return True

def print_value(node, val, data):
    print("Data change from server:")
    print(f"Item \"{node}\" Value = {val}")

if __name__ == "__main__":
    main()

    
    Traceback (most recent call last):
  File "d:\OneDrive - LTTS\Desktop\opc\opcrust.py", line 2, in <module>
    from opcua.common.callback import DataChangeCallback
ImportError: cannot import name 'DataChangeCallback' from 'opcua.common.callback' (C:\Users\40020507\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\opcua\common\callback.py)
