
[![Build Status](https://travis-ci.org/prideout/heman-python.svg?branch=master)](https://travis-ci.org/prideout/heman-python)

## Building on AWS EC2

### Starting your workday

The `aws-setup.sh` script instances the **lambdadev** AMI and creates the `heman-bash` alias, which invokes ssh for you.

```
source aws-setup.sh
heman-bash
```

After you're in the machine's shell, you can build and run the heman project as follows.

```
source env/bin/activate
git clone https://github.com/prideout/heman-python.git && cd heman-python
git submodule init && git submodule update
python setup.py build_ext
python setup.py develop
heman-gen
^D
scp -i yoshi.pem ec2-user@$DNSNAME:/home/ec2-user/heman-python/island.png .
```

### Ending your workday

```
aws ec2 terminate-instances --instance-ids $INSTANCEID
aws ec2 describe-instances --query 'Reservations[].Instances[].[State.Name]'
```

### How the AMI was created

Here's how we created the **lambdadev** AMI.

First we typed `pip install awscli && aws configure` and selected the **us-west-2** region (Oregon) and **text** output.

After signing up for AWS:

```
aws ec2 create-key-pair --key-name yoshi --query 'KeyMaterial' > yoshi.pem
chmod 400 yoshi.pem

export SGROUP=`aws ec2 create-security-group --group-name heman_security --description "heman"`
aws ec2 authorize-security-group-ingress --group-id $SGROUP --protocol tcp --port 22 --cidr 0.0.0.0/0
```

Creating the AMI:

```
export SGROUP=`aws ec2 describe-security-groups --group-name heman_security --query 'SecurityGroups[*].[GroupId]'`
export IMAGEID=ami-e7527ed7 ; # Base machine for Amazon Lambda
export INSTANCEID=`aws ec2 run-instances --image-id $IMAGEID \
    --instance-type g2.2xlarge --key-name yoshi \
    --security-group-ids $SGROUP --query 'Instances[].[InstanceId]' `
aws ec2 describe-instances --query 'Reservations[].Instances[].[State.Name,PublicDnsName]' \
    --instance-ids $INSTANCEID
sleep 60
export DNSNAME=`aws ec2 describe-instances --query 'Reservations[].Instances[].[PublicDnsName]' \
    --instance-ids $INSTANCEID`
ssh -i yoshi.pem ec2-user@$DNSNAME


sudo yum install git emacs gcc-c++ swig -y
sudo yum install libjpeg-devel zlib-devel -y
virtualenv env
source env/bin/activate
pip install numpy pillow pytest
^D


aws ec2 create-image --instance-id $INSTANCEID --name lambdadev --query 'ImageId'
sleep 60
aws ec2 terminate-instances --instance-ids $INSTANCEID
```
