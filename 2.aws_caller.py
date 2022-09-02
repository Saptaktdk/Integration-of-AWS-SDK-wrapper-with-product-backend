
import boto3

from aws_wrapper import show_buckets,upload_file,list_files,create_bucket
s3_obj = boto3.resource('s3')

#show_buckets(s3_obj)

file_path='my_test_upload_file.txt'

#upload_file(s3_obj,'pfd-saptak',file_path,'my_test_upload_file.txt')

#list_files(s3_obj,'pfd-saptak')

create_bucket(s3_obj,'example-bucket-saptak')



