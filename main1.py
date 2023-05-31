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
            ua.CreateMonitoredItemsRequest(
                SubscriptionId=subscription.subscription_id,
                TimestampsToReturn=ua.TimestampsToReturn.Neither,
                ItemsToCreate=[
                    ua.MonitoredItemCreateRequest(
                        ItemToMonitor=ua.ReadValueId(
                            NodeId=ua.NodeId(3, 1003),
                            AttributeId=ua.AttributeIds.Value
                        ),
                        MonitoringMode=ua.MonitoringMode.Reporting,
                        RequestedParameters=ua.MonitoringParameters(
                            ClientHandle="1",
                            SamplingInterval=0,
                            QueueSize=1,
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
                            ClientHandle="2",
                            SamplingInterval=0,
                            QueueSize=1,
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
                            ClientHandle="3",
                            SamplingInterval=0,
                            QueueSize=1,
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
                            ClientHandle="4",
                            SamplingInterval=0,
                            QueueSize=1,
                            DiscardOldest=True
                        )
                    )
                ]
            )
        ]

        # Request creation of monitored items
        result = client.uaclient.service.create_monitored_items(items_to_create)
        if result:
            # Check for errors in the response
            for response in result.Results:
                if response.StatusCode.is_bad():
                    raise Exception(f"Failed to create monitored item: {response.StatusCode}")

        # Write a value to a node
        node_id = ua.NodeId(3, 1012)
        value = ua.Variant(20, ua.VariantType.Int32)
        client.write_attribute_value(node_id, ua.AttributeIds.Value, value)
        print("Value written successfully")

        # Subscribe to data change
