def add_fir(firs, fir_id, victim_name, incident_date, description):
    firs[fir_id]={'victim_name': victim_name,'incident_date': incident_date,'description': description,'status': 'Registered'}
    print(f"FIR registered successfully: {firs[fir_id]}")
