MAX_TICKS=20
NB_RUN=10
DATA_FILE="output.plot"

function launch_run(){
    size=$1
    total=0
    for i in $(seq 0 $NB_RUN)
    do
	python main.py --courbe True --grid_size_X $size --grid_size_Y $size
	nb_rebound=0
	for i in $(seq 0 $MAX_TICKS)
	do
	    nb_rebound=$(($nb_rebound + $(cat trace.csv | grep ";$i;" | wc -l)))
	done
	total=$(echo "scale=4;$total + $nb_rebound / $MAX_TICKS" | bc -l)
    done
    total=$(echo "scale=4;$total / $NB_RUN" | bc -l)
    echo "$size $total" >> output.plot
}

for size in $(seq 5 5 100)
do
    echo $size "======================================="
    launch_run $size
done

gnuplot <<EOF
set terminal png enhanced
set output 'courbe.png'
binwidth=5
bin(x,width)=width*floor(x/width)
set title "nombre rebond "
set ylabel "nb rebond"
set xlabel "taille de la grille"
set grid
plot "$DATA_FILE" using 1:2 with lines
EOF

rm $DATA_FILE
