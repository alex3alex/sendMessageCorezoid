#!/bin/sh

CONV_ID=136950
CONV_USER_ID='76793'
CONV_USER_PASS='3uaGMeL2WqXU5ptPOarhAgLH6Ff5Czfdds8oJtFlu0sJPlq9Lg'
API_URL='https://www.corezoid.com/api/1/json/'
TIME=$(echo $(($(date +%s))))

JSON="{
    \"ops\" : [{
   \"type\" : \"create\",
    \"obj\" : \"task\",
\"conv_id\" : ${CONV_ID},
   \"data\" : {\"day\":\"1\",\"email\":\"$2\",\"idTemplate\":\"$1\",\"key\":\"AxYXSJ92xN4ZEdLtLh0_4g\",\"user\":\"Igor\"}
  }]
}"

SIGNATURE=$(echo -n "${TIME}${CONV_USER_PASS}${JSON}${CONV_USER_PASS}" | openssl dgst -sha1 | awk '{print $NF}')

REQ=$(curl --silent -XPOST ${API_URL}${CONV_USER_ID}/${TIME}/${SIGNATURE} --data "${JSON}")
echo "Result: ${REQ}\n"
