import json
import boto3
import os

def lambda_handler(event, context):
    # 書き込み先ファイルを作成。
    fp = open('/tmp/tmp.json', 'w')
    # ファイルの書き込み。
    json.dump(event,fp,indent=4)
    
    # txtファイルのときの書き込みなら以下みたいな感じ。必要に応じてwhileして書き込んだり。
    # fp.write('test1\ntest2')
    
    # ファイルのクローズ。
    fp.close()
    
    # S3アップロード
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('/tmp/tmp.json', 'Bucket', 'tmp.json')
    
    # 立つ鳥跡を濁さず
    os.remove('/tmp/tmp.json')
