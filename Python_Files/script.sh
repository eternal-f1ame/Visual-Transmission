#!/bin/zsh
source ./bin/activate
python image_binary.py
python receive_values.py &
python send_value.py > /dev/null 2>&1
sleep 10
python decode.py
python binary_image.py