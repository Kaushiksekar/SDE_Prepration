import subprocess

print("List with -l")
completed = subprocess.run(['ls', '-l'])
print('returncode:',completed.returncode)

print("echo with shell=True") #shell=True cause subprocess to spawn an intermediate shell process.
completed = subprocess.run("echo $HOME", shell=True)
print("returncode:",completed.returncode)

print("Error handling")
try:
    subprocess.run(['false'], check=True) # without check=True, error is not detected
except subprocess.CalledProcessError as err:
    print("ERROR:",err)

print("Capturing output")
completed = subprocess.run(
    ['ls', '-l'],
    stdout=subprocess.PIPE,
)
print("returncode:", completed.returncode)
print("output:",completed.stdout.decode("utf-8"))
