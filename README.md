# MuckRock Lambda

A short AWS Lambda to automate our FOIA requests. We wrote this so that we can schedule some reoccuring requests we sent.

# What you need to know

A working knowledge of AWS lambda, triggers and Python. 

# Deployments

Bundle up the python `requests` library into your lamba zip file before you upload it to AWS. For this to happen, in the top level directory (the one with your `.py` files), execute a `pip install -t . requests`. You can leave out this README from the zip. 

# Environment Variables

This script depends on your lambda setting your MuckRock username and password as environment variables. This is probably not ideal, so consider using a KMS for storing your keys.

# Triggers

You should configure a trigger that executes ever X months for each lambda you deploy. For our example, we send one FOIA request every month that the "1505" program for checks. You are free to configure your triggers as often as you need to send a request in AWS.


# Contibute

Ping us on [Twitter](https://twitter.com/lucyparsonslabs) or send us a PR on here. 
