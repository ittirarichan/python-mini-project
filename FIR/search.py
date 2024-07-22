def search_fir_by_id(firs, fir_id):
    if fir_id in firs:
        return firs[fir_id]
    else:
        return None