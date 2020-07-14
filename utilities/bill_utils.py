import os
import requests, json

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