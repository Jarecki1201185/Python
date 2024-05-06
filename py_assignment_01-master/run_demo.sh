#!/usr/bin/env bash

echo === Square ===
python3 square.py 10 2

echo === Compare ===
python3 compare.py <<EOF
Tekst1
Tekst2
EOF

echo Result: $?

echo === Palindrom ===
python3 palindrom.py <<EOF
Ara
EOF

echo Result: $?

echo === Fibonacci ===
python3 fibonacci.py 10
