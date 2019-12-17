# github-release-bot
![](https://github.com/Ivan-Feofanov/github-release-bot/workflows/lint-and-test/badge.svg)

#### Creating telegram bot:
Just follow [instruction](https://core.telegram.org/bots#3-how-do-i-create-a-bot)

#### Fill environment variables:
.env file example:
```shell script
ENVIRONMENT=production
TOKEN=your_bot_token
PROXY_URL=socks5://socks5_proxy_url:socks5_proxy_port
PROXY_USERNAME=socks5_proxy_username
PROXY_PASSWORD=socks5_proxy_url
SECRET_TOKEN=you_secret_token
```
If you don't need proxy just ignore proxy settings.  
If you set ENVIRONMENT value not eqal to "production" bot will ignore security settings.  

You can generate strong token with terminal command:
```shell script
openssl rand -hex 32
```
#### Start your bot:
```shell script
docker run --env-file .env -p 80:80 --name release-bot feofanov/github-release-bot
```
---
### Release webhook example:

* Open you github project settings and find **Webhook** section
* Add new webhook with params:
  * Payload URL = you bot url
  * Content type = application/json
  * Secret = you_secret_token
* Choose *Let me select individual events*
* Unselect **Pushes** and select **Releases**
* Press **Add webhook**

Congratulations, you're perfect!

---
### Deploy hook usage example:
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
