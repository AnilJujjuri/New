from opcua import Client, ua

def main():

    client = Client("opc.tcp://MYTSL02946.lnties.com:53530/OPCUA/SimulationServer")

    client.set_security_string("None")

    client.connect()

    print("Client created")

    subscription = client.create_subscription(2000, ua.SubscriptionDiagnosticsDataType())

    subscription.subscribe_data_change(print_value)

    print("Subscribed")

    try:

        while True:

            pass

    finally:

        subscription.unsubscribe_data_change(print_value)

        client.disconnect()

def print_value(node, val, data):

    print("Data change from server:")

    print(f"Item \"{node}\" Value = {val}")

if __name__ == "__main__":

    main()

