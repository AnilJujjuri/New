import opcua

def subscribe_to_values(session):
    # Create a subscription
    subscription = session.create_subscription(100, opcua.subscription.SubscriptionDiagnosticsDataType())
    # Create a monitored item
    node = session.get_node("ns=2;s=Temperature")
    handle = subscription.subscribe_data_change(node)
    return subscription, handle

if __name__ == "__main__":
    client = opcua.Client("opc.tcp://MYTSL02946.lnties.com:53530/OPCUA/SimulationServer")
    #client.set_security_string("None,Basic256,None,None")
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
  File "d:\OneDrive - LTTS\Desktop\opc\opcrust.py", line 18, in <module>
    subscription, handle = subscribe_to_values(session)
  File "d:\OneDrive - LTTS\Desktop\opc\opcrust.py", line 5, in subscribe_to_values
    subscription = session.create_subscription(100, opcua.subscription.SubscriptionDiagnosticsDataType())
AttributeError: 'CreateSessionResult' object has no attribute 'create_subscription'
