# Autoclip-Python-Script
The script to automatically remove the spacing of a image

**Instructions**:
```
tool_autoclip.py [-ext <type of image:jpg|png...>] <path of image>
```

# Add the script into terminal(Ubuntu)

1. Find out where your python is in terminal:
```
which python3.7
/usr/bin/python3.7
```
_Here, I use the python3.7_
2. Put this code in the first line of the `tool_autoclip.py`:
```
/usr/bin/python3.7
```
3.Add the file path of the python file to the $PATH
```
vi ~/.bashrc
```
Add the file:
```
export PATH=$PATH: <path of the script>
```
Save it out, re apply the .bashrc, and retry
```
source ~/.bashrc
```
