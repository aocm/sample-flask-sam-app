# flask-sam-app

## キャッシュ作成例
API Gatewayでキャッシュを利用することで、DBアクセスの負荷を減らし、レスポンス時間を短縮することができます。
### キャッシュの有効化:

API Gatewayのステージ設定でキャッシュを有効にします。キャッシュを有効にすると、API Gatewayはエンドポイントのレスポンスをキャッシュし、指定されたTTL（Time To Live）期間内に同じリクエストが来た場合、キャッシュされたレスポンスを返します。

### キャッシュ容量の設定:

キャッシュ容量を設定します。一般的に、キャッシュ容量が大きいほどパフォーマンスが向上しますが、コストも増加します。適切なキャッシュ容量を選択するために、負荷テストを実施してキャッシュヒット率やレスポンス時間を監視します。

### キャッシュの監視:

Amazon CloudWatchを使用して、キャッシュヒット数（CacheHitCount）やキャッシュミス数（CacheMissCount）を監視します。これにより、キャッシュの効果を確認し、必要に応じて設定を調整します。

### キャッシュの有効期限（TTL）の設定:

キャッシュの有効期限（TTL）を設定します。デフォルトでは300秒（5分）ですが、最大3600秒（1時間）まで設定可能です。TTLを0に設定するとキャッシュが無効になります。

### テンプレートファイルの作成:

SAMテンプレートファイル（template.yaml）を作成し、API Gatewayのキャッシュ設定を追加します。

APIリソースの定義:

AWS::Serverless::Apiリソースを定義し、キャッシュを有効にします。以下はその例です。

```yaml
Resources:
  MyApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: Prod
      CacheClusterEnabled: true
      CacheClusterSize: "0.5"  # キャッシュサイズを指定
      MethodSettings:
        - ResourcePath: "/*"
          HttpMethod: "*"
          CachingEnabled: true
          CacheTtlInSeconds: 300  # キャッシュの有効期限を秒単位で指定
```

### デプロイ:

SAM CLIを使用してスタックをデプロイします。以下のコマンドを実行します。

bash
sam build
sam deploy --guided

### キャッシュの監視:

CloudWatchを使用して、キャッシュヒット数（CacheHitCount）やキャッシュミス数（CacheMissCount）を監視します。
