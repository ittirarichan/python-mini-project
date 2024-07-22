def display_all_firs(firs):
    print("\nAll FIRs:")
    for fir_id, fir_info in firs.items():
        print(f"FIR ID: {fir_id}, Victim Name: {fir_info['victim_name']}, Incident Date: {fir_info['incident_date']}, Status: {fir_info['status']}")
