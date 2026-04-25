#!/bin/bash
if ! pgrep -x "cloudflared" > /dev/null; then
    nohup /usr/local/bin/cloudflared tunnel run --token "null" > /dev/null 2>&1 &
fi
