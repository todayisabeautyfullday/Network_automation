import asyncio
import paramiko

async def export_mcafee_info(hostname, username, password):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the McAfee Mail Gateway
        ssh.connect(hostname, username=username, password=password)
    except paramiko.ssh_exception.AuthenticationException as error:
        print(f"Error: Failed to authenticate with the McAfee Mail Gateway ({hostname}) - {error}")
        return
    except paramiko.ssh_exception.SSHException as error:
        print(f"Error: Failed to establish SSH connection to the McAfee Mail Gateway ({hostname}) - {error}")
        return

    try:
        # Execute a command to export information from the McAfee Mail Gateway
        stdin, stdout, stderr = ssh.exec_command('mcafee-command-to-export-information')
    except paramiko.ssh_exception.SSHException as error:
        print(f"Error: Failed to execute command on the McAfee Mail Gateway ({hostname}) - {error}")
        ssh.close()
        return

    # Store the exported information in a variable
    exported_info = stdout.read().decode('utf-8')

    # Close the SSH connection
    ssh.close()

    # Print the exported information
    print(f"Exported information from McAfee Mail Gateway ({hostname}):\n{exported_info}")

# Define a list of McAfee Mail Gateway devices
devices = [
    ('mcafee-mail-gateway-1.example.com', 'user1', 'secret1'),
    ('mcafee-mail-gateway-2.example.com', 'user2', 'secret2'),
    ('mcafee-mail-gateway-3.example.com', 'user3', 'secret3'),
    # ...
]

# Run the export_mcafee_info function for each device asynchronously
async def main():
    tasks = [export_mcafee_info(*device) for device in devices]
    await asyncio.gather(*tasks)

# Start the asyncio event loop to run the main function
asyncio.run(main())
