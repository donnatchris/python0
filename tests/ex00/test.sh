#!/bin/bash

cd "$(dirname "$0")" || exit 1

python3 ../../ex00/Hello.py | cat -e > actual_output.txt

if diff expected_output.txt actual_output.txt; then
	printf "Test réussi: la sortie du programme correspond à la sortie attendue."
else
	printf "Test échoué: la sortie du programme ne correspond pas à la sortie attendue."
fi

