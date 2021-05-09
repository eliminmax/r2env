import os
import sys

# Detect git, meson, ninja, patch, unzip make, gcc, ...

def host_platform():
	if os.name == "nt":
		return "w64"
	return "unix"

def user_home():
	if int(sys.version[0]) < 3:
		return os.environ['HOME']
	from pathlib import Path
	return str(Path.home())

def env_path():
	oldcwd = os.getcwd()
	while True:
		envdir = os.path.join(oldcwd, ".r2env")
		if os.path.isdir(envdir):
			return envdir
		os.chdir("..")
		cwd = os.getcwd()
		if oldcwd == cwd:
			return None
		oldcwd = cwd
	
	# walk directories up
	return None

def git_clone(url):
	os.system("git clone " + url + " " + dstdir)

# XXX this is not going to work on windows
def check_tool(tool):
	if tool == "git":
		return os.system("git --help > /dev/null") == 0
	elif tool == "unzip":
		return os.system("unzip -h > /dev/null") == 0
	return False

def check(tools):
	for tool in tools:
		found = check_tool(tool)
		if found:
			print("found " + tool)
		else:
			print("oops  " + tool)
