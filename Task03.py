def process_transactions(transaction_ids):
    if not transaction_ids:
        return []
    
    unique_transactions = set(transaction_ids)

    return list(unique_transactions)

def display(transcations_ids):
    if not transcations_ids:
        return

    for ids in transcations_ids:
        print(ids,end=" ")

if __name__=="__main__":
    raw_transactions = ["TX101", "TX102", "TX101", "TX103", "TX102", "TX104"]
    clean_transactions = process_transactions(raw_transactions)

    display(clean_transactions)
