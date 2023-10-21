import psutil

# Define the threshold for CPU usage
threshold = 80

print("Monitoring CPU usage...")

try:
    while True:
        # Get the current CPU usage as a percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        print(f"CPU usage is {cpu_usage}%")
        # Check if the CPU usage exceeds the threshold
        if cpu_usage > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
except KeyboardInterrupt:
    # Handle the interruption (e.g., Ctrl+C) to exit the program gracefully
    print("Monitoring stopped.")
except Exception as e:
    print(f"An error occurred: {e}")

