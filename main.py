import requests

# Get token from this link
# https://notify-bot.line.me/my/
TOKEN = "Ibcwb5WZ0SOJsKd40GYfdqN2O2KqSgIGHFUZ1FYFqIu"


def main():

    url = "https://notify-api.line.me/api/notify"

    ######

    dummy_price = doSCBPaymentLogic()

    text = "Payin " + str(dummy_price) + " บาท"

    print("Data to send : " + text)

    ######

    payload = {'message': text}
    files = []
    headers = {'Authorization': 'Bearer ' + TOKEN}

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=payload,
                                files=files)

    resBody = response.json()

    print("api response : " + str(resBody))

    if resBody.get("status") == 200:
        print("send data success reason")
    else:
        print("send data not success reason: " + resBody.get("message"))


def doSCBPaymentLogic():
    # mock price is 100
    return 100


if __name__ == "__main__":
    main()
