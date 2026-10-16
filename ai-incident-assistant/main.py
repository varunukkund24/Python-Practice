
def analyze_log(log_message: str) -> str:
    if not log_message.strip():
        return "INVALID"

    message = log_message.upper()

    if "ERROR" in message:
        return "ERROR"
    elif "WARNING" in message:
        return "WARNING"
    elif "INFO" in message:
        return "INFO"
    else:
        return "UNKNOWN"


log = input("Enter a log message: ")

category = analyze_log(log)

print("Log category:", category)
