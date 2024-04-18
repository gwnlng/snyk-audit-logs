![Snyk logo](https://snyk.io/style/asset/logo/snyk-print.svg)

# snyk-audit-logs

## Description
This script extracts org-scoped Audit Logs data from Snyk Audit Logs REST API endpoint and outputs it to a JSOn file

### **Note**

:exclamation: Not for Production deployment use.  

:memo: Set your environment variable SNYK_TOKEN

### Command-line Parameters

| Option/Argument   | Description                                         | Example            |
|-------------------|-----------------------------------------------------|--------------------|
| --from-date-param | The start date (inclusive) of the audit logs search | Start of yesterday |
| --to-date-param   | The end date (inclusive) of the audit logs search   | none               |
| --help            | Shows this message and exit                         |                    |
| ORG_ID            | Snyk Org ID                                         | uuid               |
| BASE_API_URL      | Snyk Base API url                                   |                    |

## Quick-start
```bash
pip install -r requirements.txt
```

### Example
To extract to `snyk_audit_log.json`, use command:

#### Yesterday log
```bash
python main.py "<ORG_ID>" "https://api.au.snyk.io/rest"
```
#### Custom date range using Optional parameters (YYYY-MM-DD)
```bash
python main.py --from-date-param "2024-04-02" --to-date-param "2024-04-03" "<ORG_ID>" "https://api.au.snyk.io/rest"
```
