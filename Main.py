from opcua import Client, ua

def subscribe_to_values(subscription, data_change_notification):
    print("Data change from server:")
    for item in data_change_notification.MonitoredItems:
        node_id = item.ClientHandle
        data_value = item.Value.Value
        print(f"Item {node_id}, Value = {data_value}")

if __name__ == '__main__':
    client = Client("opc.tcp://MYTSL02946.lnties.com:53530/OPCUA/SimulationServer")
    
    try:
        client.connect()
        print("Client connected")
        
        # Create a subscription
        subscription = client.create_subscription(2000, 10, 30)
        
        # Create some monitored items
        items_to_create = [
            ua.MonitoredItemCreateRequest(
                NodeId(3, 1003), ua.AttributeIds.Value, subscription=subscription
            ),
            ua.MonitoredItemCreateRequest(
                NodeId(3, 1008), ua.AttributeIds.Value, subscription=subscription
            ),
            ua.MonitoredItemCreateRequest(
                NodeId(3, 1009), ua.AttributeIds.Value, subscription=subscription
            ),
            ua.MonitoredItemCreateRequest(
                NodeId(3, 1010), ua.AttributeIds.Value, subscription=subscription
            )
        ]
        client.create_monitored_items(subscription, items_to_create)
        
        # Write a value to a node
        node_id = ua.NodeId(3, 1012)
        value = ua.Variant(20, ua.VariantType.Int32)
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
