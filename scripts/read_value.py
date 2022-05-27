from brownie import accounts, config, SimpleStorage


def read_contract():
    # get the most recent deployment
    simple_storage = SimpleStorage[-1]
    # ABI (brownie already knows)
    # Address (brownie already knows)
    # retrieve the lastest value store to the blockchain
    print(simple_storage.retrieve())


def main():
    read_contract()
