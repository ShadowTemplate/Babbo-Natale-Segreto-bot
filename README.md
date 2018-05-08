# Babbo Natale Segreto Bot

A Telegram bot to arrange a spicy Secret Santa. This bot randomly matches 
members of a group and randomly assigns a couple of categories between those 
available to each present. It then sends privately the result with a message to 
each person. The bot is designed to be executed offline.

---
## Information

**Status**: `Actively maintained`

**Type**: `Personal project`

**Development year(s)**: `2016+`

**Authors**: [ShadowTemplate](https://github.com/ShadowTemplate)

---
## Getting Started

Feel free to customize the bot and reuse it by creating a *secrets.py* file and 
setting these values:

```
bns_bot_token = "your_telegram_bot_token"
users = {'telegram_id_user_1': 'Name 1',
         'telegram_id_user_2': 'Name 2',
         'telegram_id_user_3': 'Name 3',
         'telegram_id_user_4': 'Name 4',
         ...}

exceptions = [('telegram_id_user_1', 'telegram_id_user_3'),
              ('telegram_id_user_2', 'telegram_id_user_4'),
              ...]
```

You can add as many exception pairs as you want. Make sure that each group 
member has authorized your bot to send him messages. 

### Prerequisites

Clone the repository and install the required Python dependencies:

```
$ git clone https://github.com/ShadowTemplate/Babbo-Natale-Segreto-bot.git
$ cd Babbo-Natale-Segreto-bot
$ pip install --user -r requirements.txt
```

---
## Building tools

* [Python 2.7](https://www.python.org/downloads/release/python-270/) - 
Programming language
* [python-telegram-bot](https://python-telegram-bot.org/) - Telegram API 
wrapper 

---
## Contributing

Any contribution is welcome. Feel free to open issues or submit pull requests.

---
## License

This project is licensed under the GNU GPLv3 license.
Please refer to the [LICENSE.md](LICENSE.md) file for details.

---
*This README.md complies with [this project template](
https://github.com/ShadowTemplate/project-template). Feel free to adopt it
and reuse it.*
