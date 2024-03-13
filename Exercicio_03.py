# Exercicio 3 - Classification of log data
    
# read the data and select registers of log where the severity is "error"

error_logs = []


def validate_logs(logs):
    if logs["level"] == "error":
        error_logs.append(logs)

    return True

teste_logs = [
  {"timestamp": "2023-10-26 15:47:21", "level": "info", "message": "application started"},
  {"timestamp": "2023-10-26 15:48:12", "level": "warning", "message": "low disk space"},
  {"timestamp": "2023-10-26 15:53:15", "level": "error", "message" :"user authentication failed"},
  {"timestamp": "2023-10-26 16:10:02", "level": "info", "message": "purchase completed"},
  {"timestamp": "2023-10-26 16:10:03", "level": "error", "message": "payment processing failed"},
  {"timestamp": "2023-10-26 16:30:45", "level": "debug", "message": "function call successful"},
]

for log in teste_logs :
    validate_logs(log)

print(error_logs)




