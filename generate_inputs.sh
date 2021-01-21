#!/bin/bash

generate_input() {
  echo $1
  for i in `eval echo {1..$1}`
  do
    echo "Almafa" >> $2
    echo "Kortefa" >> $2
    echo "Szilvafa" >> $2
    echo "Barackfa" >> $2
    echo "Torkolyfa" >> $2
  done
  gzip $2
}

generate_input 100 500_lines.input
generate_input 1000 5000_lines.input
generate_input 10000 50000_lines.input
generate_input 100000 500000_lines.input

