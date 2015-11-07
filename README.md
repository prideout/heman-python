
[![Build Status](https://travis-ci.org/prideout/heman-python.svg?branch=master)](https://travis-ci.org/prideout/heman-python)

### OS X

If you're building this for the first time, here are the prerequisites:

```
brew install swig
virtualenv env
source env/bin/activate
pip install numpy pillow pytest
git submodule init && git submodule update
```

After that, you just do this in a fresh terminal:

```
source env/bin/activate
python setup.py build_ext
python setup.py develop
py.test test/test_heman.py
```

The above command sequence is also in `bin/mac-setup.sh`.

## Building on AWS EC2

### Starting your workday

The `bin/aws-setup.sh` script instances the **lambdadev** AMI and creates the `heman-bash` alias, which invokes ssh for you.

```
source bin/aws-setup.sh
heman-bash
```

After you're in the machine's shell, you can build the heman project like this.

```
source env/bin/activate
git clone https://github.com/prideout/heman-python.git && cd heman-python
git submodule init && git submodule update
python setup.py build_ext
python setup.py develop
```

Finally, you can now generate a terrain, leave the remote machine, and copy over the resulting image for inspection.

```
heman-gen
^D
scp -i yoshi.pem ec2-user@$DNSNAME:/home/ec2-user/heman-python/island.png .
open island.png
```

### Ending your workday

Make sure you don't have any expensive instances still running:

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
