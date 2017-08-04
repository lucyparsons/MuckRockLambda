# MuckRock Lambda

A short AWS Lambda to automate our FOIA requests.

# What you need to know

A working knowledge of AWS lambda and python

# Deployments

Bundle up the python `requests` library into your lamba zip file before you upload it to AWS. For this to happen, in the top level directory (the one with your `.py` files), execute a `pip install -t . requests`. You can leave out this README from the zip. 

# Environment Variables

This script depends on your lambda setting your MuckRock username and password as environment variables. This is probably not ideal, so consider using a KMS for storing your keys.

# Contibute

Ping us on [Twitter](https://twitter.com/lucyparsonslabs) or send us a PR on here. 
