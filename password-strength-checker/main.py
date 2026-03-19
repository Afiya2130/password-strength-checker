import re
password = input("Enter password: ")
score = 0
if len(password) >= 8: score += 1
if re.search("[A-Z]", password): score +=1
if re.search("[a-z]", password): score +=1
if re.search("[0-9]", password): score +=1
if re.search("[!@#$%^&*]", password): score +=1

if score <= 2: print("WEAK❌")
elif score <= 4: print("MEDIUM⚠️")
else: print("STRONG✅")