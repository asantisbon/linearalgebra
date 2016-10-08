#!/bin/bash

echo "PEP8 checks:"
echo ""
pep8 vector.py
pep8 test.py

echo ""
echo "Unit tests:"
echo ""
python test.py
