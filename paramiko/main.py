import paramiko

# Define a list of dictionaries, each dictionary represents a device
devices = [
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.10',
        'username': 'admin',
        'password': 'secret',
    },
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.1.11',
        'username': 'admin',
        'password': 'secret',
    }
]

# Loop through each device
for device in devices:
    try:
        # Create a new SSH client
        client = paramiko.SSHClient()
        # Automatically add the server's SSH key (without this, the first time you connect to a server you will get a warning)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect to the device
        client.connect(device['ip'], username=device['username'], password=device['password'])
        # Execute the show version command
        stdin, stdout, stderr = client.exec_command("show version")
        # Get the output of the command
        output = stdout.read().decode()
        # Print the output
        print("\n" + "=" * 50)
        print(f"Device: {device['ip']}")
        print(output)
    except Exception as e:
        # Catch any exceptions and print an error message
        print(f"Error connecting to {device['ip']}: {e}")
    finally:
        # Close the connection
        client.close()
