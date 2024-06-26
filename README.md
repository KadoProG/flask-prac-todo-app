# Flask 練習

簡単な ToDo アプリを Flask で作成。

- `.scss` ファイルに対応
- RDB の挿入・更新に対応
- 多分 REST API

## 起動方法

### 自身の python で実施する場合

```shell
cp .env.example .env
pip install -r requirements.txt
python run.py # localhost:5000 または 127.0.0.1:5000で起動
```

### Docker で起動する場合

docker を使用の場合は postqres の DB が立ち上がります。

```shell
cp .env.docker.example .env
docker-compose up --build -d
```
