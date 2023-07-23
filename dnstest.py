import csv
import datetime
import time
import dns.resolver

# DNS name to resolve
domain_name = "zscaler.com"
# Number of times to measure DNS response time
num_measurements = 100
counter = 0
delay = 1 

print("Tonys DNS response time utility")
print("Performing name lookups for", domain_name, num_measurements, "times with a ", delay, "second delay")


# Create CSV file and write header row
with open('dns_response_times.csv', mode='w') as csv_file:
    fieldnames = ['Date', 'Response Time (ms)']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Measure DNS response time multiple times and write results to CSV file
    for i in range(num_measurements):
        counter = counter+1
        start_time = time.time()
      # Perform DNS resolution
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8'] # Google DNS server
        answer = dns.resolver.resolve(domain_name)

        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000

        # Write result to CSV file
        writer.writerow({'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Response Time (ms)': response_time_ms})

        print("Testing", domain_name, "#", counter,response_time_ms,"ms")
        time.sleep(delay)