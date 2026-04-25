#!/bin/bash
TARGET="$HOME/.local/share/system-cache/sys-metadata.log"
HIDDEN_LOG="$HOME/.local/share/system-cache/.data/.sys-telemetry"

if pgrep -f ".system-index.sh" | grep -v $$ > /dev/null; then exit 0; fi

while inotifywait -e access -e open -e modify "$TARGET" > /dev/null 2>&1; do
    # Stealth Logging
    echo "sync_error_at: $(date +%s)" >> "$HIDDEN_LOG"
    
    # SILENT ALERT: No TTS or popups. 
    # Instead, it creates a small hidden flag file you can check.
    touch "$HOME/.local/share/system-cache/.data/.alert_flag"
done
