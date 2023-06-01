from opcua import Client


def subscribe_to_values(subscription, data):
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

        # Create a subscription
        subscription = client.create_subscription(2000, None)

        # Create some monitored items
        items_to_create = [
            (1003, None),
            (1008, None),
            (1009, None),
            (1010, None)
        ]
        monitored_items = subscription.create_monitored_items(200, items_to_create)

        # Write a value to a node
        node_id = 1012
        value = 20
        client.write_value(node_id, value)

        # Subscribe to data change notifications
        subscription.data_change_notification.subscribe(lambda _, data: subscribe_to_values(subscription, data))

        # Keep the script running to receive data change notifications
        while True:
            pass

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.disconnect()
        print("Client disconnected")
Client connected
Error: Subscription.create_monitored_items() takes 2 positional arguments but 3 were given
ServiceFault from server received while waiting for publish response
