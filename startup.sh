#!/bin/bash
gunicorn --bind=0.0.0.0 --timeout 600 app:create_app