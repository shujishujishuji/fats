access:
127.0.0.1:5042

tasks:
make user database
streaming error
login setting
make stream
connect database
grapql
make template
user authlization
insert logs
error handling


directory	file	説明
(root)	main.py	ルーティングを定義
apps	app.py	Responder、ログなどの生成
commons.py	プロジェクトの共通クラスや関数を定義
db.py	データベースのオブジェクト生成とDB用のfunctionを定義
dbproperties.py	DB接続用のプロパティを管理
properties.py	configファイルを読んで、アプリケーションの設定を管理
settings	app.conf	プロジェクトの各種プロパティを定義
logging.conf	loggingのconfig