#!/bin/bash
source ~/nomadik_systems/.env

echo "--- Nomadik Systems: Final Hardening Audit ---"

# 1. TLS Check
SETTINGS=$(curl -s -H "Authorization: Bearer $CF_API_TOKEN" \
  "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT_ID/gateway/settings")
TLS=$(echo "$SETTINGS" | jq -r '.. | .tls_decrypt? | .enabled? // "false"')
[[ "$TLS" == "true" ]] && echo "[OK] TLS Decryption: ACTIVE" || echo "[WARN] TLS Decryption: INACTIVE"

# 2. Tunnel/Connector Check
TUNNELS=$(curl -s -H "Authorization: Bearer $CF_API_TOKEN" \
  "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT_ID/tunnels")
ACTIVE_TUNNELS=$(echo "$TUNNELS" | jq -r '.result[] | select(.status=="healthy") | .name')
if [[ -z "$ACTIVE_TUNNELS" ]]; then
    echo "[WARN] Active Connectors: 0 (System is isolated)"
else
    echo "[OK] Active Connectors: $ACTIVE_TUNNELS"
fi

# 3. Application Check
APPS=$(curl -s -H "Authorization: Bearer $CF_API_TOKEN" \
  "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT_ID/access/apps")
COUNT=$(echo "$APPS" | jq -r '.result | length // 0')
echo "[INFO] Protected Applications: $COUNT"
