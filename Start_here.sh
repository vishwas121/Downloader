#!/bin/bash
mkdir Youtube
cd Youtube
if [ "$1" = NULL ]
then
	 python3 ../fun_script.py
else
	python3 ../fun_script.py "../${1}"
fi
cd ..
ls Youtube > input.txt
sed "s/\.webm\|\.mkv\|\.mp4/\.ogg/g" input.txt > input2.txt
awk -F"[-.]" -f script.awk input2.txt > output.txt
cd Youtube
x=1
y=$(grep -c "" < ../input.txt)
while [ $x -le $y ];
do
    line=$(head -${x} ../input.txt| tail -1)
    output=$(head -${x} ../output.txt| tail -1) 
    echo $output
    ffmpeg -i "$line" -vn -acodec copy "$output"
    x=$(($x + 1))
    # echo $x
done

rename "s/\.ogg/\.mp3/g" *
echo "Success"
