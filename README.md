# github-release-bot
![](https://github.com/Ivan-Feofanov/github-release-bot/workflows/check/badge.svg)

Deploy hook usage example:
```shell script
PROJECT_NAME="my_project_name"
GIT_TAG=$(git describe --tags --abbrev=0)
HOST="http://example.com"
PORT="80"
CHAT_ID="my_chat_id"
KEY="my_secret_key"

PAYLOAD="{\"project_name\":\"$PROJECT_NAME\",\"tag\":\"$GIT_TAG\"}"
SIGN="sha1="$(echo -n $PAYLOAD | openssl sha1 -hmac $KEY | sed -e 's/^.* //')

curl -X POST "http://$HOST:$PORT/deploy/?chat_id=$CHAT_ID" \
  -H "X-Hub-Signature: $SIGN" \
  -d $PAYLOAD
```
