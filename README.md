# s3-to-mysql-lambda
This lambda function retrieves the uploaded csv file from S3 and loads the data into RDS mysql. The function is triggered by an S3 Put trigger.



Permissions:
- S3: Get*, List*
- AWSLambdaVPCAccessExecutionRole -> because in my case the RDS was in a VPC, although it was publicly available, the lambda needs the role so it can create and delete ENI's.  
-"logs:CreateLogGroup",
-"logs:CreateLogStream",
-"logs:PutLogEvents",
-"ec2:CreateNetworkInterface",
-"ec2:DescribeNetworkInterfaces",
-"ec2:DeleteNetworkInterface"
