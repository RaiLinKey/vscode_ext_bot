# vscode_ext_bot
Telegram bot for download VSIX files for VS Code

Сборка контейнера:
```shell
docker build -t vscode_ext_bot:latest .
```

Запуск контейнера:
```shell
docker run --env-file ./.env --name vscode_ext_bot -d vscode_ext_bot:latest
```

Удаление контейнера с остановкой:
```shell
docker rm -f vscode_ext_bot
```

Удаление образа:
```shell
docker rmi vscode_ext_bot:latest
```

Сохранение образа в архив:
```shell
docker save vscode_ext_bot > vscode_ext_bot.tar
```

Загрузка образа (или образов) из архива:
```shell
docker load -i vscode_ext_bot.tar
```
