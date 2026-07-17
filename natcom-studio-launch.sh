#!/bin/bash
# natcom-studio-launch.sh
# NATCOM Studio launcher — kills old instance, starts fresh, opens browser

NATCOM_DIR="/home/beoboy/NATCOM"
LOG_FILE="/tmp/natcom_studio.log"
PORT=8080

echo "========================================"
echo "  NATCOM Studio — Launching..."
echo "========================================"

# Kill any previous instance
pkill -f "server.py" 2>/dev/null
sleep 1

# Start the server in background
cd "$NATCOM_DIR"
nohup python3 server.py > "$LOG_FILE" 2>&1 &
SERVER_PID=$!

echo "Server PID: $SERVER_PID"

# Wait for server to be ready
for i in {1..10}; do
    if curl -s "http://localhost:$PORT" > /dev/null 2>&1; then
        echo "Server is UP on http://localhost:$PORT"
        break
    fi
    sleep 0.5
done

# Open the browser automatically
if command -v xdg-open &>/dev/null; then
    xdg-open "http://localhost:$PORT"
elif command -v google-chrome &>/dev/null; then
    google-chrome "http://localhost:$PORT"
elif command -v firefox &>/dev/null; then
    firefox "http://localhost:$PORT"
fi

echo "NATCOM Studio is running. Logs: $LOG_FILE"
