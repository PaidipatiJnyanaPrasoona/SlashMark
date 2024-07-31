import boto3

s3 = boto3.client('s3')

s3.put_object(Body=encrypted_data, Bucket='my-bucket', Key='credit_card_info.txt')