#!/bin/bash
echo "[DEBUG] Checking credentials..."
if [[ -z "$CF_ACCOUNT_ID" || "$CF_ACCOUNT_ID" == "your_actual_account_id_here" ]]; then
    echo "[!] ERROR: CF_ACCOUNT_ID is missing or still set to placeholder."
    exit 1
fi

echo "[EXECUTE] Enabling TLS Decryption..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X PUT \
     "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT_ID/gateway/settings" \
     -H "Authorization: Bearer $CF_API_TOKEN" \
     -H "Content-Type: application/json" \
     --data '{"settings": {"tls_decrypt": {"enabled": true}}}')

if [ "$STATUS" -eq 200 ]; then
    echo "[SUCCESS] TLS Decryption enabled (Status 200)."
else
    echo "[ERROR] API returned $STATUS. Check your Token permissions."
fi
