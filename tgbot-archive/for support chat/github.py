import json
import requests

def get_latest_commit(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    try:
        res = requests.get(url)
        if not res.status_code == 200:
            return res.text
        
        commits_data = res.json()
        latest_commit = commits_data[0]
        return latest_commit
    except Exception as e:
        print(e)


def send_message(bot_token, chat_id, text, pin_message=None):
    api_url = f"https://api.telegram.org/bot{bot_token}"
    method = "sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    try:
        res = requests.get(f"{api_url}/{method}", data)
        if res.status_code != 200:
            print(res.text)
        else:
            if pin_message:
                data = {
                    "chat_id": chat_id,
                    "message_id": json.loads(res.text)["result"]["message_id"]
                }
                res = requests.get(f"{api_url}/pinChatMessage", data)
                if res.status_code != 200:
                    print(res.text)
    except Exception as e:
        print(e)


# Variables 
owner = "bishalqx980"
repo = "tgbot"
bot_token = ""
chat_id = 000


# call func's
res = get_latest_commit(owner, repo)
if not res:
    print("Error: error getting lastest commit.")
    exit(1)

committer = res['commit']['committer']
lastest_commit_url = res['html_url']
commit_message = res['commit']['message']

msg = (
    f"New commit? | {repo}\n\n"
    f"Commited by: <code>{committer['name']}</code>\n"
    f"Time: <code>{committer['date']}</code>\n"
    f"Comment: <code>{commit_message}</code>\n"
    f"Link: <a href='{lastest_commit_url}'>{res['sha'][:7]}</a>"
)

send_message(bot_token, chat_id, msg, True)
