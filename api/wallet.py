from web3 import Web3, HTTPProvider

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/465df29a11644bf791cd1d83faeb4f7f'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f'Your address: {address}\nYour key: {privateKey}')