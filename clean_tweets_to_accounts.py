tweets_file = 'tweets.txt'
accounts_file = 'accounts.txt'

# Open tweets file for reading and accounts file for writing
with open(tweets_file, 'r') as tf, open(accounts_file, 'w') as af:
    # Iterate through each line in the tweets file (each tweet URL)
    for line in tf:
        # Strip whitespace characters like newlines at both ends of string
        url = line.strip()
        
        if url:  # Check if there's any content after stripping
        
            # Split on '/' to get parts of the URL. The username will be right before "status"
            parts = url.split('/')
            
            if len(parts) >= 5: 
                account_url = '/'.join(parts[:4]) + '/'
                
                # Write cleaned up account URL to accounts file.
                af.write(account_url + '\n')
                

# Clean the file from duplicates.
with open(accounts_file, 'r') as file:
    lines = file.readlines()

# Remove duplicates by converting the list to a set
unique_lines = set(lines)

# Write the unique lines back to the file
with open(accounts_file, 'w') as file:
    file.writelines(sorted(unique_lines))

print("Done!")
