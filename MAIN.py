import requests

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
onlyletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
other = ['-', '_']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for char1 in alphabet:
    for char2 in alphabet:
        for char3 in alphabet:
            user = char1 + char2 + char3
            if (not (char1 in onlyletters and char2 in onlyletters and char3 in onlyletters)) and not (char1 in other and char2 in other and char3 in other) and not (char1 in nums and char2 in nums and char3 in nums):
                x = requests.get('https://api.scratch.mit.edu/accounts/checkusername/'+user)
                if x.text == '{"username":"'+user+'","msg":"valid username"}':
                    print(user)
