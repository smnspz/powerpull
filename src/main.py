import subprocess
import json

INTERNET_PASSWORD = "git-codecommit.eu-west-1.amazonaws.com"

def get_leapp_integrations():
    return subprocess.Popen(
        ["leapp", "integration", "list", "-x", "--output=json"],
        stdout=subprocess.PIPE,
    )

def get_integration_id():
    integrations = get_leapp_integrations()
    parsed = json.loads(integrations.stdout.read())
    return parsed[0]["integrationId"]

def login():
    delete_password()
    subprocess.run(
        ["leapp", "integration", "login", f"--integrationId={get_integration_id()}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
        )

def delete_password():
    return subprocess.run(
        ["security", "delete-internet-password", "-s", INTERNET_PASSWORD],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )

def main():
    login()

if __name__ == "__main__":
    main()
