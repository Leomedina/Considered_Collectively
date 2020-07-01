import requests, json
# from keys import API_KEY
import os

class APIUtils():
    """Utilities Class"""

    def get_recent_bills():
        """Get the latest 20 bills"""

        response = requests.get("https://api.propublica.org/congress/v1/116/both/bills/active.json", 
                    headers={"X-API-Key": os.environ.get('API_KEY')})

        res_json = response.json()
        cleaned = BillsUtils.getCleanedResults(res_json.get('results')[0]['bills'])

        return cleaned

    def search_bills(query):
        """Get 20 recent bills that match query"""

        response = requests.get(f"https://api.propublica.org/congress/v1/bills/search.json?query={query}", 
                    headers={"X-API-Key": os.environ.get('API_KEY')})
        
        res_json = response.json()
        cleaned = BillsUtils.getCleanedResults(res_json.get('results')[0]['bills'])

        return cleaned

    def get_bill_by_id(bill_id):
        """Get bill by Id"""
        
        response = requests.get(f"https://api.propublica.org/congress/v1/116/bills/{bill_id[:-4]}.json", 
                    headers={"X-API-Key": os.environ.get('API_KEY')})
    
        res_json = response.json().get('results')[0]
        return res_json


class BillsUtils():
    """Utilities for Bills"""

    def getCleanedResults(bills):
        cleanedBills = {}
        counter = 0

        for bill in bills:
            newBill = {
                'bill_id': bill.get("bill_id"),
                'short_title': bill.get("short_title"),
                'title': bill.get("title"),
                'congressdotgov_url': bill.get("congressdotgov_url"),
                'introduced_date': bill.get("introduced_date"),
                'committees': bill.get('committees'),
                'primary_subject': bill.get("primary_subject"),
                'sponsor_title': bill.get("sponsor_title"),
                'sponsor_name': bill.get('sponsor_name'),
                'sponsor_state': bill.get("sponsor_state"),
                'sponsor_id': bill.get('sponsor_id'),
                'sponsor_party': bill.get('sponsor_party'),
                'latest_major_action': bill.get("latest_major_action"),
                'latest_major_action_date': bill.get("latest_major_action_date"),
            }
            cleanedBills[counter] = newBill
            counter += 1

        return cleanedBills