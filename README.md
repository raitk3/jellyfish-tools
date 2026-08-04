# jellyfish-tools
Just testing making a bot for the server, that's all.

## Development

Enable the project commit-message template after cloning:

```shell
git config --local commit.template .gitmessage
```

## Running the bot
- Create .env file in root directory
- Add bot token as `DISCORD_BOT`
- Run following command.
```shell
python bot.py --env-file .env
```
- For extra development features run following instead:
```shell
python bot.py --env-file .env --dev
```