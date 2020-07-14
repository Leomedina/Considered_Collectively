import requests, json
# from keys import API_KEY
from utilities.bill_utils import BillsUtils
import os

class APIUtils():
    """Utilities Class"""

    def get_recent_bills():
        """Get the latest 20 bills"""

        response = requests.get("https://api.propublica.org/congress/v1/116/both/bills/active.json", 
                    headers={"X-API-Key": os.environ.get('API_KEY')})
                    # headers={"X-API-Key": API_KEY})

        res_json = response.json()
        cleaned = BillsUtils.getCleanedResults(res_json.get('results')[0]['bills'])

        return cleaned

    def search_bills(query):
        """Get 20 recent bills that match query"""

        response = requests.get(f"https://api.propublica.org/congress/v1/bills/search.json?query={query}", 
                    headers={"X-API-Key": os.environ.get('API_KEY')})
                    # headers={"X-API-Key": API_KEY})
        
        res_json = response.json()
        cleaned = BillsUtils.getCleanedResults(res_json.get('results')[0]['bills'])

        return cleaned

    def get_bill_by_id(bill_id):
        """Get bill by Id"""
        
        response = requests.get(f"https://api.propublica.org/congress/v1/116/bills/{bill_id[:-4]}.json", 
                    headers={"X-API-Key": os.environ.get('API_KEY')})
                    # headers={"X-API-Key": API_KEY})
    
        res_json = response.json().get('results')[0]
        return res_json

