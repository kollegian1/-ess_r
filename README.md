
# 📈 COINBASE-DEDICATED One-Time trade Profits
![Logo](https://media.discordapp.net/attachments/985242946880282634/1061344185787088996/th5xamgrr6se0x5ro4g612.png)
A brief description of what this project does and who it's for


## API Reference 
![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

```http
  **FEATURES**
  Onloss Sell to prevent losses bigger than a few cents (in the rare case of a sudden extreme sell.)
```

| Idempotence | Type     | Reason                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required** for small range trades. | **MANDATORY**
| `api_cret` | `string`| **Required** To only place sells for you.|**MANDATORY**

```http
  Interacts with $0.000 acurate price indicators to maximize benifits.
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id_curr`      | `automatic` | **Required** Id of profit to fetch |



## Required Python Composants

To install the required composants, run those commands.

```bash
  py -m pip install coinbase 
  py -m install requests
```
## Run the Product

Once those commands are ran, set your api kys in the setup.py file and then start trade.py from a terminal : py .\trade.py



