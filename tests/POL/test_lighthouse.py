import subprocess
from docs.urls_path import path, websites_to_check


def test_run_lighthouse():
    for i, website_to_check in enumerate(websites_to_check):
        output_path = f"{path[i].replace('/', '_')}.html"  # Using path names for the output
        cmd = f'lighthouse {website_to_check} --output=html --quiet --output-path={output_path}'
        result = subprocess.run(cmd, shell=True)

        if result.returncode == 0:
            print(f"Lighthouse report for {website_to_check} saved to: {output_path}")
        else:
            print(f"An error occurred while running Lighthouse for {website_to_check}.")