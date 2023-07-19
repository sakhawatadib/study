import os
import re
import json

# Load the GitHub event JSON
with open(os.environ['GITHUB_EVENT_PATH']) as f:
    event = json.load(f)

# Get the username of the PR submitter
pr_user = event['pull_request']['user']['login']

# Get the files modified in the PR
modified_files = [file['filename'] for file in event['pull_request']['files'] if file['status'] == 'added']

# Open the README.md file
with open('README.md', 'r+') as f:
    readme = f.read()

    # Update the README.md for each new file
    for file in modified_files:
        with open(file, 'r') as md_file:
            # Extract the first heading from the file
            first_heading = re.search('^# (.*)', md_file.read(), re.MULTILINE).group(1)
        # Update the README.md
        category = os.path.dirname(file)
        link = f"[{first_heading}](./{file}) - [{pr_user}](https://github.com/{pr_user})"
        readme = re.sub(f'## {category}(.*?)\n', f'## {category}\n\n{link}\n', readme, flags=re.DOTALL)

    # Write the updated README.md
    f.seek(0)
    f.write(readme)
    f.truncate()
