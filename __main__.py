"""A Linode Python Pulumi program"""

import pulumi
import pulumi_linode

from pulumi_docker import Image, DockerBuild



# Create a Linode resource (Linode Instance)
instance = pulumi_linode.Instance('my-instance', 
                                type='g6-nanode-1', 
                                region='us-east', 
                                image='linode/ubuntu18.04',
                                root_pass='pulumi_test')

# Export the Instance label of the instance
pulumi.export('instance_label', instance.label)
pulumi.export('instance_ip', instance.ip_address)