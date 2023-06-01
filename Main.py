from opcua import Client
from opcua.ua import NodeId, MonitoredItemCreateRequest


def data_change_handler(subscription, data):
    print("Data change from server:")
    for item in data.MonitoredItems:
        node_id = item.NodeId
        value = item.Value.Value
        print(f"Item {node_id}, Value = {value}")


if __name__ == '__main__':
    client = Client("opc.tcp://MYTSL02946.lnties.com:53530/OPCUA/SimulationServer")
    try:
        client.connect()
        print("Client connected")

        # Create a subscription with a data change handler
        subscription = client.create_subscription(2000, data_change_handler)

        # Create some monitored items
        items_to_create = [
            MonitoredItemCreateRequest(
                NodeId=NodeId(3, 1003),
                RequestedParameters=None
            ),
            MonitoredItemCreateRequest(
                NodeId=NodeId(3, 1008),
                RequestedParameters=None
            ),
            MonitoredItemCreateRequest(
                NodeId=NodeId(3, 1009),
                RequestedParameters=None
            ),
            MonitoredItemCreateRequest(
                NodeId=NodeId(3, 1010),
                RequestedParameters=None
            )
        ]
        monitored_items = subscription.create_monitored_items(items_to_create)

        # Write a value to a node
        node_id = NodeId(3, 1012)
        value = 20
        client.write_value(node_id, value)

        # Keep the script running to receive data change notifications
        while True:
            pass

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.disconnect()
        print("Client disconnected")
