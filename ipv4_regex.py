# CHECK FOR A VALID IP ADDRESS
# 255 ---> 250-255 ---> 25[0-5]
# 249 ---> 200-249 ---> 2[0-4][0-9]
# 199 ---> 100-199 ---> 1[0-9][0-9]
# 99 ---> 10-99    --->
# 9 ---> 0-9

import re


class Check_ip:
    def __init__(self):
        self.pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    def check_if_valid_ip(self, ip):
        res = re.match(self.pattern, ip)
        if res:
            print("PASS: It's a VALID IP address")
        else:
            print("FAIL: It's NOT a VALID IP address")


check_ip = Check_ip()
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Enter 1 to check if an IP is valid or not")
    print("Enter 2 to Exit")
    choice = int(input())
    if choice is 1:
        print("Enter the IP address to check if it's valid: ")
        ip = input()
        check_ip.check_if_valid_ip(ip)
    if choice is 2:
        quit()
    print()
