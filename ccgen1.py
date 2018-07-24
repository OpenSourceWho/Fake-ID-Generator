import random
import string
print(" $$$$$$\                        $$\                        $$\ $$\                           $$$$$$\ $$$$$$$\         $$$$$$\                                                    $$\                         ")
print("$$  __$$\                       $$ |                       $$ |\__|                          \_$$  _|$$  __$$\       $$  __$$\                                                   $$ |                        ")
print("$$ /  $$ |$$\   $$\  $$$$$$$\ $$$$$$\    $$$$$$\  $$$$$$\  $$ |$$\  $$$$$$\  $$$$$$$\          $$ |  $$ |  $$ |      $$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  ")
print("$$$$$$$$ |$$ |  $$ |$$  _____|\_$$  _|  $$  __$$\ \____$$\ $$ |$$ | \____$$\ $$  __$$\         $$ |  $$ |  $$ |      $$ |$$$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \____$$\\_$$  _|  $$  __$$\ $$  __$$\ ")
print("$$  __$$ |$$ |  $$ |\$$$$$$\    $$ |    $$ |  \__|$$$$$$$ |$$ |$$ | $$$$$$$ |$$ |  $$ |        $$ |  $$ |  $$ |      $$ |\_$$ |$$$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|$$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|")
print("$$ |  $$ |$$ |  $$ | \____$$\   $$ |$$\ $$ |     $$  __$$ |$$ |$$ |$$  __$$ |$$ |  $$ |        $$ |  $$ |  $$ |      $$ |  $$ |$$   ____|$$ |  $$ |$$   ____|$$ |     $$  __$$ | $$ |$$\ $$ |  $$ |$$ |      ")
print("$$ |  $$ |\$$$$$$  |$$$$$$$  |  \$$$$  |$$ |     \$$$$$$$ |$$ |$$ |\$$$$$$$ |$$ |  $$ |      $$$$$$\ $$$$$$$  |      \$$$$$$  |\$$$$$$$\ $$ |  $$ |\$$$$$$$\ $$ |     \$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      ")
print("\__|  \__| \______/ \_______/    \____/ \__|      \_______|\__|\__| \_______|\__|  \__|      \______|\_______/        \______/  \_______|\__|  \__| \_______|\__|      \_______|  \____/  \______/ \__|      ")
confrimation=input("Ready to generate?")
if confrimation=="Yes"or"yes":print("Generating...")
fname=['Sophia','Jackson','Emma','Aiden','Lucas','Liam','Ava','Mia','Noah','Isabella','Ethan','Riley','Mason','Aria','Caden','Zoe','Oliver','Charlotte','Elijah','Lily','Jacob','John','Lachlan','Georgia']
lname=['Smith','Johnson','Williams','Brown','Jones','Miller','Davis','Garcia','Rodriguez','Wilson','White','Martin','Anderson','Thompson','Nguyen','Turner','Walker',]
secure_random=random.SystemRandom()
stname=['Alder','Browning','Guthrie','High','Druid','Folland','Main','Lockwood','Queen','MacKenzie','King','Mistletoe','First','Second','Third','Angas','Fosters','Regency','Newbon','Percy','Bruce','Pirie','Currie','Gilbert','Waymouth','Flinders','Turner','Melrose','Silver','Turnbull','Orana','Briens','Wright','Davies','Church','Chapel','Hill','Robins']
sttype=['St','Rd','Ct','Ave','Ln','Cres']
secure_random=random.SystemRandom()
city=['Adelaide, SA','Melbourne, VIC','Sydney, NSW','Perth, WA','Hobart, TAS','Brisbane, QLD','Surfers Paradise, QLD','Bendigo, VIC','Ballarat, VIC','Newcastle, NSW','Cairns, QLD','Townsville, QLD','Wollongong, NSW','Alice Springs, NT','Canberra, ACT','Darwin, NT','Toowoomba, QLD','Riverton, SA''Adelaide, SA','Melbourne, VIC','Sydney, NSW','Perth, WA','Adelaide, SA','Melbourne, VIC','Sydney, NSW','Perth, WA','Adelaide, SA','Melbourne, VIC','Sydney, NSW','Perth, WA','Brisbane, QLD','Brisbane, QLD','Brisbane, QLD',]
secure_random=random.SystemRandom()
ccn=['4448-8637-3225-7970','4755-8490-8118-3724','4019-1219-4794-6914','4157-1447-4760-4063','4188-9273-0003-7178']
secure_random=random.SystemRandom()
expm=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
expy=['2020','2021','2022','2023','2024','2025','2026','2027','2028','2029',]
secure_random=random.SystemRandom()
typ=['Visa']
secure_random=random.SystemRandom()
bank=['Australia and New Zealand Banking Group','Commonwealth Bank','National Australia Bank','Westpac','Bank of Melbourne','BankSA','Bank of Australia','ME Bank','ING Direct','AMP','Beyond Bank','Peoples Choice Credit Union','Suncorp Bank']
secure_random=random.SystemRandom()
bt=['O-','O+','B-','B+','A-','A+','AB+','AB-','O-','O+','B-','B+','A-','A+','AB+']
secure_random=random.SystemRandom()
print("Done!")
print("Name:",secure_random.choice(fname),secure_random.choice(lname))
print("Address:",random.randint(1,75),secure_random.choice(stname),secure_random.choice(sttype),)
print("City:",secure_random.choice(city))
print("Age:",random.randint(18,68))
print("Credit Card Number:",secure_random.choice(ccn))
print("Expiry:",secure_random.choice(expm),secure_random.choice(expy))
print("CCV:",random.randint(211,982))
print("Card Type:",secure_random.choice(typ))
print("Bank:",secure_random.choice(bank))
print("Blood Type:",secure_random.choice(bt))
print("Weight:",random.randint(45,90),"kg")
print("Height:",random.randint(140,168),"cm")
else:print("Invaild Parameter")
