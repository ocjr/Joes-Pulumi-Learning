"""An AWS Python Pulumi program"""

import mimetypes
import pulumi
from pulumi_aws import s3

import os

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('joes-pulumi-bucket', website={"index_document": "index.html"})

web_dir = "src"

for file in os.listdir(web_dir):

    filepath = os.path.join(web_dir,file)
    mime_type, _ = mimetypes.guess_type(filepath)

    obj = s3.BucketObject(file,
        bucket=bucket.id,
        source=pulumi.FileAsset(filepath),
        acl="public-read",
        content_type=mime_type)

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
pulumi.export('bucket_endpoint', pulumi.Output.concat("http://", bucket.website_endpoint))
