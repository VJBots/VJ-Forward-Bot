# VJ Forward Bot

<b>Auto Restart All User Forwarding After Bot Restarted.</b>

![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Welcome+To+VJ+Forward+Bot+!)

## How To Deploy [Video Tutorial](https://youtu.be/A-iIh_5WAlk)

## Features

- [x] Public Forward (Bot)
- [x] Private Forward (User Bot)
- [x] Custom Caption 
- [x] Custom Button
- [x] Skip Duplicate Messages
- [x] Skip Messages Based On Extensions & Keywords & Size
- [x] Filter Type Of Messages
- [x] Auto Restart Pending Task After Bot Restart 


<b>To Know About All Features, Join My <a href='https://t.me/VJ_Botz'>Update Channel</a>.</b>

## Commands

```
start - check I'm alive 
forward - forward messages
unequify - delete duplicate media messages in chats
settings - configure your settings
stop - stop your ongoing tasks
reset - reset your settings
restart - restart server (owner only)
resetall - reset all users settings (owner only)
broadcast - broadcast a message to all your users (owner only)
```

## Variables

### Required
* `API_ID` API Id from my.telegram.org
* `API_HASH` API Hash from my.telegram.org
* `BOT_TOKEN` Bot token from @BotFather
* `BOT_OWNER` Telegram Account Id of Owner.
* `DATABASE_URI` Database uri from [MongoDB](https://mongodb.com) Watch [Video Tutorial](https://youtu.be/DAHRmFdw99o)

### Optional
* `DATABASE_NAME` MongoDB database name (default: `vj-forward-bot`)
* `BOT_SESSION` Pyrogram session name (default: `vjbot`)
* `PORT` HTTP health-check port injected by Koyeb (default: `8000`)

## Deploy on Koyeb

This repository supports both **Dockerfile** and **Buildpack** deployments on Koyeb out of the box:

1. Create a new **Web Service** on [Koyeb](https://app.koyeb.com) and connect your GitHub repository.
2. **Builder**: Choose either **Dockerfile** (recommended) or **Buildpack** (uses `.python-version`, `requirements.txt`, and `Procfile`).
3. **Run Command**: Leave as default (`bash start.sh` is already configured in both `Dockerfile` and `Procfile`).
4. **Environment Variables**: Add `API_ID`, `API_HASH`, `BOT_TOKEN`, `BOT_OWNER`, and `DATABASE_URI`.
5. **Exposed Ports & Health Check**: Expose port `8000` (`HTTP`) with health check path `/` or `/health`.
6. Click **Deploy**.

## Credits

* <b>[Tech VJ](https://youtube.com/@Tech_VJ)</b>
