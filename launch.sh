#!/bin/bash

simulation_name=$1


if [ $simulation_name == "particules" ]
then
    python3 src/main_particules.py
elif [ $simulation_name == "wator" ]
then
    python3 src/main_water.py

elif [ $simulation_name == "avatar" ]
then
    python3 src/main_avatar.py
else
    >&2 echo "$simulation_name n'est pas une simulation valide"
fi
