#!/bin/bash

nohup gunicorn -b 0.0.0.0:5000 --daemon "app:create_app()" </dev/null >/home/pi/logs/light_controller/lc.log
