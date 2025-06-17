#!/bin/bash
echo "Running NGSpice simulation..."
ngspice -b circuit.cir
python3 plot.py
