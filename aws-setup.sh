# Please invoke this by typing: "source aws-setup.sh"
#
# This script assumes:
#   1. That you've got the AWS CLI installed and configured.
#   2. That you have an AWS key-pair named "yoshi".
#   3. That you have a cert file named "yoshi.pem".
#
# If any of these are untrue, look at README.

export SGROUP=`aws ec2 describe-security-groups --group-name heman_security --query 'SecurityGroups[*].[GroupId]'`
export IMAGEID=`aws ec2 describe-images --owners self --filters="Name=name,Values=lambdadev" --query Images[].[ImageId]`
export INSTANCEID=`aws ec2 run-instances --image-id ${IMAGEID} --instance-type g2.2xlarge --key-name yoshi --security-group-ids ${SGROUP} --query 'Instances[].[InstanceId]'`

sleep 60
export DNSNAME=`aws ec2 describe-instances --query 'Reservations[].Instances[].[PublicDnsName]' --instance-ids ${INSTANCEID}`
alias heman-bash="ssh -i yoshi.pem ec2-user@${DNSNAME}"
