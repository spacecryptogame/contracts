from brownie import SPGToken, SPEMintableToken
from scripts.helpful_scripts import get_account
from web3 import Web3


def main():
    account = get_account()

    deploySPG(account)


def verifyContractOnBSC(account):
    token = SPGToken.at("0xb7d3de92aea5ede7d7c3482db17c52f4163f63ae")
    SPGToken.publish_source(token)


def deploySPG(account):
    initial_supply = Web3.toWei(1000000000, "ether")
    spg = SPGToken.deploy(
        initial_supply, {"from": account, "gas_limit": 2000000}, publish_source=True
    )


def deploySPE(account):
    initial_supply = Web3.toWei(1000000000, "ether")
    spe = SPEMintableToken.deploy(
        initial_supply, {"from": account, "gas_limit": 3000000}, publish_source=True
    )
