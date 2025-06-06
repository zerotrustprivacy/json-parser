import json

log_file_path = 'app_logs.txt'

parsed_logs = []
error_log_lines = []

print(f"Starting to parse log file: {log_file_path}\n")

try:
    with open(log_file_path, 'r') as file:
        for line_num, line in enumerate(file, 1): # enumerate to get line number
            line = line.strip() # Remove leading/trailing whitespace including newlines
            if not line: # Skip empty lines
                continue

            try:
                # Attempt to parse the line as JSON
                log_entry = json.loads(line)
                parsed_logs.append(log_entry)
                print(f"Line {line_num}: Successfully parsed JSON: {log_entry.get('event_type')}")
            except json.JSONDecodeError as e:
                # This block runs if json.loads() fails (i.e., not valid JSON)
                error_log_lines.append((line_num, line, str(e)))
                print(f"Line {line_num}: ERROR - Invalid JSON: {line} - Reason: {e}")
            except Exception as e:
                # Catch any other unexpected errors
                error_log_lines.append((line_num, line, str(e)))
                print(f"Line {line_num}: UNEXPECTED ERROR - {line} - Reason: {e}")

except FileNotFoundError:
    print(f"Error: The file '{log_file_path}' was not found. Make sure it's in the same directory.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")

print("\n--- Parsing Summary ---")
print(f"Total lines processed: {len(parsed_logs) + len(error_log_lines)}")
print(f"Successfully parsed JSON entries: {len(parsed_logs)}")
print(f"Lines with parsing errors: {len(error_log_lines)}")

if error_log_lines:
    print("\nDetails of lines with errors:")
    for num, content, reason in error_log_lines:
        print(f"  Line {num}: '{content}' (Reason: {reason})")

# Practice, print the first few parsed entries:
print("\nFirst 3 successfully parsed entries:")
for i, entry in enumerate(parsed_logs[:3]):
    print(f"  {i+1}. {entry}")
