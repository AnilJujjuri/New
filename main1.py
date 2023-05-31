from opcua import Client, ua

def subscribe_to_values(subscription, data_change_notification):
    print("Data change from server:")
    for item in data_change_notification.MonitoredItems:
        node_id = item.ClientHandle
        data_value = item.Value.Value
        print(f"Item {node_id}, Value = {data_value}")

if __name__ == '__main__':
    try:
        # Create a client and connect to the OPC UA server
        client = Client("opc.tcp://MYTSL02946.lnties.com:53530/OPCUA/SimulationServer")
        client.connect()
        print("Client connected")

        # Create a subscription
        subscription = client.create_subscription(2000, ua.SubscriptionDiagnosticsDataType())

        # Create some monitored items
        items_to_create = [
            ua.MonitoredItemCreateRequest(
                ClientHandle=1,
                NodeId="ns=3;i=1003",
                AttributeId=ua.AttributeIds.Value,
                MonitoringMode=ua.MonitoringMode.Reporting,
                RequestedParameters=ua.MonitoringParameters()
            ),
            ua.MonitoredItemCreateRequest(
                ClientHandle=2,
                NodeId="ns=3;i=1008",
                AttributeId=ua.AttributeIds.Value,
                MonitoringMode=ua.MonitoringMode.Reporting,
                RequestedParameters=ua.MonitoringParameters()
            ),
            ua.MonitoredItemCreateRequest(
                ClientHandle=3,
                NodeId="ns=3;i=1009",
                AttributeId=ua.AttributeIds.Value,
                MonitoringMode=ua.MonitoringMode.Reporting,
                RequestedParameters=ua.MonitoringParameters()
            ),
            ua.MonitoredItemCreateRequest(
                ClientHandle=4,
                NodeId="ns=3;i=1010",
                AttributeId=ua.AttributeIds.Value,
                MonitoringMode=ua.MonitoringMode.Reporting,
                RequestedParameters=ua.MonitoringParameters()
            )
        ]

        # Request creation of monitored items
        result = subscription.create_monitored_items(items_to_create)
        if result:
            # Check for errors in the response
            for response in result:
                if response.StatusCode.is_bad():
                    raise Exception(f"Failed to create monitored item: {response.StatusCode}")

        # Write a value to a node
        node_id = "ns=3;i=1012"
        value = ua.Variant(20, ua.VariantType.Int32)
        client.write_attribute_value(node_id, ua.AttributeIds.Value, value)
        print("Value written successfully")

        # Subscribe to data change notifications
        subscription.subscribe_data_change(subscribe_to_values)

        # Keep the script running
        while True:
            pass

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.disconnect()
        print("Client disconnected")
