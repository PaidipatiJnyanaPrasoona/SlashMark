import boto3

iam = boto3.client('iam')

iam.create_user(UserName='credit_card_user')

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAccessToCreditCardInfo",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/credit_card_info.txt"
        }
    ]
}
iam.create_policy(PolicyName='credit_card_policy', PolicyDocument=json.dumps(policy))

iam.attach_user_policy(UserName='credit_card_user', PolicyArn='arn:aws:iam::123456789012:policy/credit_card_policy')