import typer
import requests
import os
import json


SNYK_TOKEN = os.getenv("SNYK_TOKEN")
version = "2024-03-12"


def main(org_id, base_api_url, from_date_param: str = None, to_date_param: str = None):
    """
    Calls Snyk org-scoped Audit-logs API
    :param:
    :return:
    """
    request_param = ""
    if from_date_param:
        request_param = f"&from={from_date_param}"
    if to_date_param:
        request_param = request_param + f"&to={to_date_param}"
    api_link = f"/orgs/{org_id}/audit_logs/search?size=100&version={version}{request_param}"
    header_auth = f"token {SNYK_TOKEN}"
    payload = {}
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'Authorization': header_auth
    }
    has_next_link = True
    response_http_error = False
    response_error_code = 0
    response_error_text = ""
    audit_file_log_json = []

    while has_next_link:
        api_url = f"{base_api_url}{api_link}"
        response = requests.request("GET", api_url, headers=headers, data=payload)
        if response.status_code == 200:
            response_json = response.json()
            # check for next page link
            if 'links' in response_json and 'next' in response_json["links"]:
                has_next_link = True
                api_link = response_json['links']['next']
                print(api_link)
            else:
                has_next_link = False

            audit_data_items = response_json["data"]["items"]
            audit_file_log_json.extend(audit_data_items)
        else:
            # deal with response error later
            has_next_link = False
            response_http_error = True
            response_error_code = response.status_code
            response_error_text = response.text

    try:
        # dump all the audit log data we have extracted
        with open("snyk_audit_log.json", 'w+') as log_file:
            json.dump(audit_file_log_json, log_file, indent=2)
            # for chunk in audit_file_log_json:
            #     json.dump(chunk, log_file)

        if response_http_error:
            raise Exception(f"encountered http response {response_error_code} error:\n{response_error_text}")
    except FileNotFoundError as fnfe:
        raise Exception("unable to create file", fnfe)


if __name__ == "__main__":
    typer.run(main)
