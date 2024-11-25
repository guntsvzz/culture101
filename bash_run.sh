#!/bin/bash

# Run a conversation between two Thai participants
echo "Running conversation between two Thai participants (Santi and Apsara):"
python3 conversation_simulation.py --p1 Santi --p2 Apsara
echo ""

# Run a conversation between two Chinese participants
echo "Running conversation between two Chinese participants (Wei and Lili):"
python3 conversation_simulation.py --p1 Wei --p2 Lili
echo ""

# Run a conversation between Thai and Vietnamese participants
echo "Running conversation between a Thai (Santi) and Vietnamese (Duc):"
python3 conversation_simulation.py --p1 Santi --p2 Duc
echo ""

# Run a conversation between Thai and German participants
echo "Running conversation between a Thai (Santi) and German (Max):"
python3 conversation_simulation.py --p1 Santi --p2 Max
echo ""

# Optional: Add more combinations if needed
