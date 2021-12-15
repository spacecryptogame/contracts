from brownie import MultiSigWallet, SPEMintableToken
from scripts.helpful_scripts import get_account
from web3 import Web3


def main():
    account = get_account()

    deployMultiSigWallet(account)


def deployMultiSigWallet(account):

    addresss = []
    _numConfirmationsRequired = 2
    contract = MultiSigWallet.deploy(
        addresss,
        _numConfirmationsRequired,
        {"from": account, "gas_limit": 2000000},
        publish_source=True,
    )
