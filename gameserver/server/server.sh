#!/bin/bash
redis-server --daemonize yes
gunicorn -c gunicorn.config.py server:server --bind 0.0.0.0:8000

