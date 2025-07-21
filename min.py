import requests
from requests.auth import HTTPBasicAuth

def fetch_loan_terms(username, password):
    url = "https://partners.lend.com.au/api/configs/loanterms"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Version': '20190501',
        'Environment': 'live'
    }

    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password))
    response.raise_for_status()
    return response.json().get("loan_terms", [])

def int_to_letters(n):
    result = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result

def test_api_post(username, password, loan_term_id):
    url = "https://partners.lend.com.au/api/leads"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Version': '20190501',
        'Environment': 'live'        
    }

    tag = int_to_letters(loan_term_id)

    body = {
        'owner': {
            'first_name': f"Test{tag}",
            'last_name': 'Last',
            'contact_number': '012345678',
            'email': f'test{tag}@email.com',
        },
        'lead': {
            'organisation_name': 'TestCompany',
            'industry_id': '189',
            'purpose_id': '1',
            'amount_requested': 123,
            'sales_monthly': 456,
            'company_registration_date': '2000/01/01',
            'campaign': 'Test Campaign',
            'loan_term_requested': int(loan_term_id)
        },
    }

    try:
        response = requests.post(url, headers=headers, auth=HTTPBasicAuth(username, password), json=body)
        print(f"Loan Term ID {loan_term_id} → Status: {response.status_code}, Success: {response.ok}")
        if not response.ok:
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error with loan_term_id {loan_term_id}: {e}")

if __name__ == "__main__":
    username = "USERNAME"
    password = "PASS"

    loan_terms = fetch_loan_terms(username, password)

    for term in loan_terms:
        loan_term_id = term["loan_term_id"]
        loan_term_label = term["loan_term"]
        print(f"Testing: {loan_term_label} (ID: {loan_term_id})")
        test_api_post(username, password, int(loan_term_id))
