# sumologic-duo-security
Serverless collection solution for Duo security

### Sumo Logic App for Duo Security
Duo provides two-factor authentication, endpoint remediation, and secure single sign-on tools. The Sumo Logic App for Duo Security helps you monitor your Duo account’s authentication logs, administrator logs, and telephony logs. The dashboards provide insight into failed and successful authentications, events breakdown by applications, factors, and users, geo-location of events, admin activities, outliers, threat analysis of authentication, and administrator events.

### Log Types
Sumo Logic App for Duo Security uses following logs. See Duo's [documentation](https://duo.com/docs/adminapi#logs) for details of the log schema.

- Authentication Logs
- Administrator Logs
- Telephony Logs

### Collect Logs for Duo Security
1. Create an HTTP Logs and Metrics Source.
2. Download the Lambda Function code, and upload it to AWS Lambda Console and create a Lambda function.
3. Define Environment Variables for the Lambda Function.
4 .Add a time-based trigger for the Lambda function.

Detailed instructions [here](https://help.sumologic.com/07Sumo-Logic-Apps/22Security_and_Threat_Detection/Duo_Security/Collect_Logs_for_Duo_Security).

### Install the Duo Security App and View the Dashboards
Login in to your Sumo Logic account and install the App from App Catalog
