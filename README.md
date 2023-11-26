# Remote_Procedure_Call(RPC)
## システムの目標と実装詳細
- 異なるプログラミング言語で書かれたクライアントとサーバーが共通の方法で通信し、特定の関数を実行できるようにするシステムを作ることが求められています
  - クライアントが Python で書かれたサーバに対して、JavaScript（Node.js を使用）から命令を出す場面を想定しています。
- ライアントとサーバ間でデータをやりとりするために、ネットワークを通じてメッセージを送る「ソケット」を利用します。
  - 使うソケットファミリは、「AF_UNIX」
 
## リクエストとレスポンスの形式
- クライアントからサーバへの要求（リクエスト）と、サーバからクライアントへの返答（レスポンス）の形式を決めます。
- JSON 形式のメッセージが用いる。
  - リクエストには実行するメソッドの名前、その引数、引数の型
  - リクエストの ID が、レスポンスには結果、結果の型、同じリクエスト ID
- エラーが発生した場合、サーバはエラーメッセージを含むレスポンスをクライアントに返します。エラーの詳細はレスポンスの error 属性に格納されます。
- 
