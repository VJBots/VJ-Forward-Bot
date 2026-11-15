#!/usr/bin/env bash
set -uo pipefail

PORT="${PORT:-8000}"

gunicorn \
  --bind "0.0.0.0:${PORT}" \
  --workers 1 \
  --threads 2 \
  --timeout 120 \
  --access-logfile - \
  --error-logfile - \
  app:app &
GUNICORN_PID=$!

python3 main.py &
BOT_PID=$!

cleanup() {
  trap - INT TERM EXIT
  kill -TERM "${BOT_PID}" "${GUNICORN_PID}" 2>/dev/null || true
  wait "${BOT_PID}" "${GUNICORN_PID}" 2>/dev/null || true
}

trap cleanup INT TERM EXIT

wait -n "${GUNICORN_PID}" "${BOT_PID}"
EXIT_CODE=$?
exit "${EXIT_CODE}"
