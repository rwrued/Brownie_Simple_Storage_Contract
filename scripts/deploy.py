from brownie import accounts, config, SimpleStorage, network

# import os


def deploy_simple_storage():
    # MOST SECURE TTP
    # Using my metamask ACCOUNT after adding to brownie via CLI
    # account = accounts.load("test-account")

    # Using my metamask ACCOUNT details within .env
    # account = accounts.add(os.getenv("PRIVATE_KEY"))

    # Using my metamask ACCOUNT details within .env
    # without using "import os". instead using brownie-config.yaml
    # account = accounts.add(config["wallets"]["from_key"])

    # using the brownie generated account
    # account = accounts[0]

    # using the get_account function
    account = get_account()

    # Deploy contract ** ALWAYS NEEDS A FROM
    simple_storage = SimpleStorage.deploy({"from": account})
    # retrieve the inital store value from the block chain
    stored_value = simple_storage.retrieve()
    print(stored_value)
    # updating the stored value ** ALWAYS NEEDS A FROM
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    # retieved updated value
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
