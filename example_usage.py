from client import AutonomousSupportTicketResolutionActionExecutorClient

def main():
    client = AutonomousSupportTicketResolutionActionExecutorClient()
    res = client.resolve_ticket("Why did our billing webhook fail on invoice inv_4401?", "Enterprise")
    print(f"Resolution State: {res['resolution_state']}")
    print(f"Confidence Score: {res['confidence_score']*100:.1f}%")
    print(f"Executed Action: {res['executed_action']}")
    print(f"Response: {res['customer_response_markdown']}")

if __name__ == "__main__":
    main()
