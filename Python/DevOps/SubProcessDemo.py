import subprocess
a=subprocess.run("dir",shell=True)
print(a)
print(a.returncode)
b=subprocess.run(["ipconfig","/all"])
print(b)
print(b.returncode)

c=subprocess.Popen("notepad")
# subprocess.call()
# subprocess.check_call()
# subprocess.check_output()