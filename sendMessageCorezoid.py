import time
import os
import json


def sendMessageCorezoid(message):
    """
    Send message, using Corezoid backend.
    Arguments is object with keys: day, email, idTemplate, key, user.
    """
    conv_id = 136950
    conv_user_id = "76793"
    conv_user_pass = '3uaGMeL2WqXU5ptPOarhAgLH6Ff5Czfdds8oJtFlu0sJPlq9Lg'
    time_secund = int(time.time())
    url = 'https://www.corezoid.com/api/1/json/'
    data = {}
    data["type"] = "create"
    data["obj"] = "task"
    data["conv_id"] = 136950
    data["data"] = message
    json_data = json.dumps({"ops": [data]})
    openssl = os.popen("echo '%s%s%s%s' \
                        | openssl dgst -sha1 | awk '{print $NF}'"
                       % (time_secund, conv_user_pass, json_data,
                          conv_user_pass)).read()[:-1]
    os.popen("curl --silent -XPOST %s%s/%s/%s --data %s"
             % (url, conv_user_id, time_secund, openssl, json_data))


# example

# sendMessageCorezoid(
#     {"day": "1", "email": "igor.sizon@dataroot.co", "idTemplate":
#      "telegram", "key": "AxYXSJ92xN4ZEdLtLh0_4g", "user": "Igor"})
