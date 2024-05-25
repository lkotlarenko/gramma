#!/bin/bash
nohup poetry run python gramma.py >/dev/null 2>&1 &
disown
exit
