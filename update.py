import os 
import shutil

file = "find_smd.py"
to_move = ["find_smd.exe", "/dist", "/run file"]
to_delete = ["__pycache__", "build", "dist", "find_smd.spec"]


pos = os.getcwd().replace("\\", "/")

os.system("pyinstaller " + file + " --onefile")

try: os.remove(pos + "/" + "run file/" + "find_smd.exe")
except: pass
os.rename(pos + to_move[1] + "/" + to_move[0],\
			pos + to_move[2] + "/"+ to_move[0])

for k in to_delete:
	try: shutil.rmtree(pos + "/" + k)
	except: 
		try: os.remove(pos + "/" + k)
		except: pass

