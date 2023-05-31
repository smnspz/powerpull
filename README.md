You must have `leapp_cli` installed
Run `leapp integration list -x --output=json | grep -o '"integrationId": "[^"]*' | grep -o '[^"]*$'` to get the integrationId and paste it in your `.env` file.

