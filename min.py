import requests
from requests.auth import HTTPBasicAuth

def test_api_post(username, password, loan_term_id):
    url = "https://partners.lend.com.au/api/leads"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Version': '20190501',
        'Environment': 'live'        
    }
    body = {
        'owner': {
            'first_name': f"LoanTermTest",
            'last_name': 'IdTwo',
            'contact_number': '012345678',
            'email': f'test@email.com',
        },
        'lead': {
            'organisation_name': 'TestCompany',
            'industry_id': '189',
            'purpose_id': '15',
            'amount_requested': 123,
            'sales_monthly': 456,
            'company_registration_date': '2000-01-01',
            'campaign': 'Test Campaign',
            'product_type_id': '1',
            'loan_term_requested': loan_term_id
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
    username = ""
    password = ""
    
    test_api_post(username, password, 4)
