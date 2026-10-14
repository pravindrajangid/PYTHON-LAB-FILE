
import os
import sys

# Display current working directory
print("Current Directory:", os.getcwd())

# List files and directories
print("\nContents of Current Directory:")
for item in os.listdir():
    print(item)

# Create a workspace directory
workspace = "workspace"

if not os.path.exists(workspace):
    os.mkdir(workspace)
    print("\nWorkspace folder created.")
else:
    print("\nWorkspace folder already exists.")

# Navigate to workspace
os.chdir(workspace)
print("Current Directory:", os.getcwd())

# Create a text log file
log_file = "system_log.txt"

with open(log_file, "a") as file:
    file.write("System utility executed successfully.\n")

print("\nLog file created/updated:", log_file)

# Display text files in the current directory
print("\nText Files:")
for file_name in os.listdir():
    if file_name.endswith(".txt"):
        print(file_name)

# Read the log file safely
print("\nLog File Content:")
with open(log_file, "r") as file:
    content = file.read()

print(content)

# Return to parent directory
os.chdir("..")

print("Returned to:", os.getcwd())

# Display command-line arguments
print("\nCommand-line Arguments:")
for argument in sys.argv:
    print(argument)
