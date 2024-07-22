def update_fir_status(firs, fir_id, new_status):
    if fir_id in firs:
        firs[fir_id]['status']=new_status
        print(f"FIR Status updated successfully for FIR ID {fir_id}")
    else:
        print(f"FIR ID {fir_id} not found.")