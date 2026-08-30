def analyze_logs(log_entries):
    if not log_entries:
        print("No log entries.")
        return

    log_counts = {}
    for log_type in log_entries:
        if log_type in log_counts:
            log_counts[log_type] += 1
        else:
            log_counts[log_type] = 1
            
    unique_log_types = list(log_counts.keys())

    frequency_list = list(log_counts.items())
    
    most_frequent_type = None
    highest_count = -1
    
    for log_type, count in frequency_list:
        if count > highest_count:
            highest_count = count
            most_frequent_type = log_type
            
    print("\n---Log Report---")
    print(f"Log types that appeared: {unique_log_types}")
    
    print("\nFrequency List:")
    for log_type, count in frequency_list:
        print(f" * {log_type}: {count} times")
        
    print(f"\nMost frequent log type: {most_frequent_type} ({highest_count} times)")

if __name__ == "__main__":
    sample_logs = ["INFO", "ERROR", "WARNING", "INFO", "ERROR", "INFO"]
    
    large_log_collection = sample_logs * 2000  
    
    analyze_logs(large_log_collection)
