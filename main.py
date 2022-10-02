import tempfile
import subprocess
from netmiko import ConnectHandler

# Cisco IOS-XE connection details
device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.2",
    "username": "cisco",
    "password": "cisco",
}
# Git repository details
git_repo_url = "https://github.com/linoyzoaretz/backup_ios_to_github.git"
commit_message = "Automatic config update"

# ------ Connect to device and get device config ------

# Connect to IOS-XE device
net_connect = ConnectHandler(**device)

# Run show command on device
device_config = net_connect.send_command("show run")

# Disconnect from Device
net_connect.disconnect()

# ------ Clone git repo in temporary directory, replace files with new config file and push changes back to git repo  ------

# Create temporary directory
temporary_folder = tempfile.TemporaryDirectory()
print("temp folder: ", temporary_folder)

print("git clone---------->")
# Clone Git Repo
subprocess.call(
    f"cd {temporary_folder.name} && git clone {git_repo_url} . && del *.*", shell=True
)





# print("write file---------->")
# # Write all config to file
# with open(f"{temporary_folder.name}/{device['host']}_config.txt", "w") as outfile:
#     outfile.write(device_config)
#
# # Git commit all changes
# print("git add---------->")
# subprocess.call(
#     f"cd {temporary_folder.name} && git add -A",
#     shell=True,
# )
# print("git commit---------->")
# subprocess.call(f"cd {temporary_folder.name} && git commit -m '{commit_message}'",
#                 shell=True,
#                 )
# print("git push---------->")
# subprocess.call(f"cd {temporary_folder.name} && git push",
#                 shell=True,
#                 )
#
# # Delete temporary directory
# #temporary_folder.cleanup()
