import time

import paramiko

# Define the script file you want to execute on the remote devices
SCRIPT_TO_EXECUTE = "/path/to/your_script.sh"  # Change this to the path of your script

# List of devices (IP addresses or hostnames)
DEVICES = ["10.49.75.122", "10.49.75.124", "10.49.75.99","10.49.75.50", "10.49.75.47", "10.49.75.110", "10.49.75.136"]  # Update with your devices

ipfetch_file = """
#!/bin/bash

# Create or update /etc/rc.local
echo "Creating /etc/rc.local with necessary content..."
cat << 'EOF' | sudo tee /etc/rc.local > /dev/null
#!/bin/sh -e
# Start DHCP client on enp1s0
/sbin/dhclient enp1s0
exit 0
EOF

# Make rc.local executable
echo "Setting execute permissions on /etc/rc.local..."
sudo chmod +x /etc/rc.local

# Create or update /etc/systemd/system/rc-local.service
echo "Creating /etc/systemd/system/rc-local.service with necessary content..."
cat << 'EOF' | sudo tee /etc/systemd/system/rc-local.service > /dev/null
[Unit]
Description=/etc/rc.local Compatibility
ConditionPathExists=/etc/rc.local

[Service]
Type=forking
ExecStart=/etc/rc.local
TimeoutSec=0
StandardOutput=journal

[Install]
WantedBy=multi-user.target
EOF

# Enable and start rc-local service
echo "Enabling and starting rc-local service..."
sudo systemctl enable rc-local
sudo systemctl start rc-local

# Verify the service status
echo "Checking rc-local service status..."
sudo systemctl status rc-local

echo "Setup complete. Reboot to confirm the changes."
"""

# Remote user (replace 'username' with your actual username on the remote devices)
USER = "viavi"  # Update with your username

# Prompt for sudo password securely
sudo_password = 'viavi'


# Function to execute the script on a remote device
def execute_script(device):
    print(f"Connecting to {device}...")

    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote device
        client.connect(device, username=USER, password="viavi")
        sftp = client.open_sftp()
        with sftp.file("/home/viavi/ipfetch.sh", 'w') as remote_file:
            remote_file.write(ipfetch_file)

        # Command to execute the script with sudo
        shell = client.invoke_shell()
        time.sleep(0.2)
        shell.send("su\n")
        time.sleep(0.2)
        shell.send("password\n")
        time.sleep(0.2)
        time.sleep(0.2)
        shell.send("chmod +x ipfetch.sh\n")
        time.sleep(0.2)
        shell.send("./ipfetch.sh\n")
        time.sleep(3)
        time.sleep(0.2)
        time.sleep(0.2)
        output = shell.recv(100000).decode("utf-8")
        print(output)

        print(f"Script executed successfully on {device}")

    except Exception as e:
        print(f"Failed to execute script on {device}: {e}")

    finally:
        client.close()


# Loop through each device and execute the script
for device in DEVICES:
    execute_script(device)
