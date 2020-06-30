import requests, json
from keys import API_KEY

class APIUtils():
    """Utilities Class"""

    def get_recent_bills():
        """Get the latest 20 bills"""

        response = requests.get("https://api.propublica.org/congress/v1/116/both/bills/active.json", 
                    headers={"X-API-Key": API_KEY})

        res_json = response.json()

        cleaned = BillsUtils.getCleanedResults(res_json.get('results')[0]['bills'])

        return cleaned

    def search_bills(query):
        """Get recent 20 bills that match query"""

        response = requests.get(f"https://api.propublica.org/congress/v1/bills/search.json?query={query}", 
                    headers={"X-API-Key": API_KEY})
        
        return response.json()

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
                'sponsor_title': bill.get("sponsor_title"),
                'sponsor_name': bill.get('sponsor_name'),
                'sponsor_state': bill.get("sponsor_state"),
                'sponsor_id': bill.get('sponsor_id'),
                'latest_major_action': bill.get("latest_major_action"),
                'latest_major_action_date': bill.get("latest_major_action_date"),
                'congressdotgov_url': bill.get("congressdotgov_url"),
            }
            cleanedBills[counter] = newBill
            counter += 1

        return cleanedBills