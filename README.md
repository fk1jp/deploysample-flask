コンテナ動作確認くん
===

## できる(ようになるはずの)こと

ALBからECSに繋いで、そこからRDSに接続する。

- 2020/01/02 ローカルで動くところまで確認。

## 使い方

### ローカルにて

- 必要なミドルウェア等

docker
docker-compose

- 使い方

コンテナ外
```
git clone https://github.com/fk1jp/deploysample-flask.git
cd deploysample-flask

docker-compose build
docker-compose up -d
docker-compose exec app sh
```

コンテナ内
```
/app # pip install -r requirements.txt 

> migrateions/を削除したり models/models.pyを更新した時など
> FLASK_APP=run.py flask db init
> FLASK_APP=run.py flask db migrate

FLASK_APP=run.py flask db upgrade

FLASK_APP=run.py flask run --port 3000 --host '0.0.0.0'
```

## 動機

AWSとかの(ECSの)CIやCDをしてみたい！  
ただ、物を作るだけじゃなくてアプリケーション層まで動作確認したい。  
インフラエンジニャーだからアプリは苦手。だからとりあえずで動くやつ欲しい。  

## 参考資料

Flask + SQLAlchemy + SQLAlchemy migrate 周りを参考にしました。  
https://qiita.com/shirakiya/items/0114d51e9c189658002e

templateやview周りを参考にしました。  
https://study-flask.readthedocs.io/ja/latest/02.html

postがうまくできなかった -> secret_keyが設定できていなかった。  
https://ja.stackoverflow.com/questions/46766/runtimeerror-the-session-is-unavailable-because-no-secret-key-was-set

絵文字が入力できなかった  
mysqlコンテナ側修正  https://qiita.com/neko-neko/items/de8ea13bbad32140de87  
flask側修正  https://blog.amedama.jp/entry/2016/06/07/234106  
