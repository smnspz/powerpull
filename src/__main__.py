import subprocess
import os

integration_id = os.environ.get("INTEGRATION_ID")
internet_password = os.environ.get("INTERNET_PASSWORD")

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
