import subprocess
import os

integration_id = os.environ.get("INTEGRATION_ID", "git-codecommit.eu-west-1.amazonaws.com")
internet_password = os.environ.get("INTERNET_PASSWORD", "ed8ce96a-892c-4efa-86f7-01ff719e5e11")

def login():
    return subprocess.run(
        ["leapp", "integration", "login", f"--integrationId={integration_id}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
        )

def delete_password():
    return subprocess.run(
        ["security", "delete-internet-password", "-s", internet_password],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )


def main():
    if login().returncode != 0:
        delete_password()

if __name__ == "__main__":
    main()
