from opcua import Client, ua


def data_change_handler(subscription, data):
    print("Data change from server:")
    for item in data.MonitoredItems:
        node_id = item.MonitoredItemId
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
            ua.MonitoredItemCreateRequest(
                ItemToMonitor=ua.ReadValueId(
                    NodeId=ua.NodeId(3, 1003),
                    AttributeId=ua.AttributeIds.Value
                ),
                MonitoringMode=ua.MonitoringMode.Reporting,
                RequestedParameters=ua.MonitoringParameters(
                    ClientHandle=1,
                    SamplingInterval=1000,
                    QueueSize=10,
                    DiscardOldest=True
                )
            ),
            ua.MonitoredItemCreateRequest(
                ItemToMonitor=ua.ReadValueId(
                    NodeId=ua.NodeId(3, 1008),
                    AttributeId=ua.AttributeIds.Value
                ),
                MonitoringMode=ua.MonitoringMode.Reporting,
                RequestedParameters=ua.MonitoringParameters(
                    ClientHandle=2,
                    SamplingInterval=1000,
                    QueueSize=10,
                    DiscardOldest=True
                )
            ),
            ua.MonitoredItemCreateRequest(
                ItemToMonitor=ua.ReadValueId(
                    NodeId=ua.NodeId(3, 1009),
                    AttributeId=ua.AttributeIds.Value
                ),
                MonitoringMode=ua.MonitoringMode.Reporting,
                RequestedParameters=ua.MonitoringParameters(
                    ClientHandle=3,
                    SamplingInterval=1000,
                    QueueSize=10,
                    DiscardOldest=True
                )
            ),
            ua.MonitoredItemCreateRequest(
                ItemToMonitor=ua.ReadValueId(
                    NodeId=ua.NodeId(3, 1010),
                    AttributeId=ua.AttributeIds.Value
                ),
                MonitoringMode=ua.MonitoringMode.Reporting,
                RequestedParameters=ua.MonitoringParameters(
                    ClientHandle=4,
                    SamplingInterval=1000,
                    QueueSize=10,
                    DiscardOldest=True
                )
            )
        ]

        # Create the monitored items
        monitored_items = subscription.create_monitored_items(items_to_create)

        # Keep the script running to receive data change notifications
        while True:
            pass

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.disconnect()
        print("Client disconnected")

