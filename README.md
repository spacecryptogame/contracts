# tokenErc20

Setup Brownie follow: 
https://github.com/eth-brownie/brownie


Create .env file in root folder

###### ADD KEYS in .env file:

 * export PRIVATE_KEY={YOUR WALLET PRIVATE KEY}

 * export BSCSCAN_TOKEN={YOUR BSCSCAN KEY}

 *** IMPORTANT: NEVER COMMIT .env FILE.

###### Run scripts: 

 * brownie compile

###### Deploy:
 *  brownie run scripts/1_deploy_token.py --network networkName

*networkName:
enter: brownie networks list
or check in
 - https://github.com/eth-brownie/brownie/blob/1f06e6420f949b20002cadec8dcf7c1e86051374/brownie/data/network-config.yaml
