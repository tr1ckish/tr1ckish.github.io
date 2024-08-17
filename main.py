import requests
import json

def generate_link(*args):
    url = 'https://api.monobank.ua/api/merchant/invoice/create'
    headers = {
        'X-Token': 'm4v6yuSwgobiXvTW72e6Vfg',
        'Content-Type': 'application/json'
    }

    data = {
      "amount": 9900,
      "ccy": 980,
      "merchantPaymInfo": {
        "reference": "84d0070ee4e44667b31371d8f8813947",
        "destination": "Покупка",
        "comment": "Покупка",
        "customerEmails": []
      },
      "redirectUrl": "https://tr1ckish.github.io/",
      "validity": 3600,
      "paymentType": "debit",
      "saveCardData": {
        "saveCard": True,
        "walletId": "69f780d841a0434aa535b08821f4822c"
      },
      "agentFeePercent": 1.42
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    a=response.json()
    print(a['pageUrl'])
    if response.status_code == 200:
        response_data = response.json()
        # Assuming the response contains a URL in 'paymentUrl'
        payment_url = response_data['pageUrl'].get("paymentUrl")
        if payment_url:
            # Redirect to the payment URL
            window.location.href = payment_url
        else:
            print("Payment URL not found in the response.")
    else:
        print(f"Error: {response.status_code}")

# Bind the Python function to the button click event
Element("generate-button").element.onclick = generate_link
