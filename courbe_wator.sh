#!/bin/bash

#MAX_TICKS=20
#NB_RUN=10
#DATA_FILE="output.plot"
#EXE=src/main.py
#
#function launch_run(){
#    size=$1
#    total=0
#    for i in $(seq 0 $NB_RUN)
#    do
#	python $EXE --courbe True --grid_size_X $size --grid_size_Y $size
#	nb_rebound=0
#	for i in $(seq 0 $MAX_TICKS)
#	do
#	    nb_rebound=$(($nb_rebound + $(cat trace.csv | grep ";$i;" | wc -l)))
#	done
#	total=$(echo "scale=4;$total + $nb_rebound / $MAX_TICKS" | bc -l)
#    done
#    total=$(echo "scale=4;$total / $NB_RUN" | bc -l)
#    echo "$size $total" >> output.plot
#}
#
#for size in $(seq 5 5 100)
#do
#    echo $size "======================================="
#    launch_run $size
#done

DATA_FILE="trace.csv"

#gnuplot <<EOF
#set terminal png enhanced
#set output 'courbe.png'
#binwidth=5
#bin(x,width)=width*floor(x/width)
#set title "Evolution des poissons et requins"
#set ylabel "Densité de population"
#set xlabel "Temps"
#set grid
#plot "$DATA_FILE" using 1:2 with lines title "Poisson", \
#     "$DATA_FILE" using 1:3 with lines title "Requin"
#EOF

gnuplot <<EOF
set terminal png enhanced size 1500,500
set output 'courbe.png'
set multiplot layout 1,2 title "Evolution de population" font ",14"
#
set title "Evolution poisson et requin"
set ylabel "Densité de population"
set xlabel "Temps"
set grid
set ytics 5000
set xtics 300
plot "$DATA_FILE" using 1:2 with lines title "Poisson", \
     "$DATA_FILE" using 1:3 with lines title "Requin"
#
set title "Evolution poisson selon requin"
set ylabel "Requin"
set xlabel "Poisson"
set grid
set xtics 2000
unset key
plot "$DATA_FILE" using 2:3 with lines
#
unset multiplot
EOF
