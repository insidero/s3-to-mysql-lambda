import logging
import boto3
import botocore

import csv
import pymysql

logger = logging.getLogger()
logger.setLevel(logging.INFO)


rds_host  = 'HOST'
name = 'NAME'
password = 'PASS'
db_name = 'NAME'
port='3306'


s3 = boto3.client('s3')
try:
    conn = pymysql.connect(rds_host, user=name,passwd=password, db=db_name, connect_timeout=5,local_infile=1)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

   
logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def lambda_handler(event, context):
    # retrieve bucket name and file_key from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    logger.info('Reading {} from {}'.format(file_key, bucket_name))
    # get the object
    obj=s3.download_file(bucket_name, file_key,'/tmp/file.csv')
    
    with conn.cursor() as cur:
        cur.execute('LOAD DATA LOCAL INFILE \'/tmp/file.csv\' INTO table TABLE_NAME fields terminated by \',\' enclosed by \'"\' lines terminated by \'\n\' ignore 1 rows;')
        conn.commit()


   
    
        
