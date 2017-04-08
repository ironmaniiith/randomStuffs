#!/bin/bash
MAIN_DIR=`pwd`
URL='http://www.bhmpics.com/'
curl -s -L "$URL" > main.html
cat main.html | egrep -E "margin-left:0px;[^=]" | egrep -o "href=\"[^\"]*" | cut -d "\"" -f2 > categories.list
sed -E -i -e "s|^/||g" -e "s|\.html$||g" categories.list

cat categories.list | while read categoryName # Looping through all the categories
do
	mkdir -p "$categoryName" # ===
	cd "$categoryName" # ===
	indexURL="$URL""$categoryName"
	curl -s "$indexURL" > index.html
	cat index.html  | grep Next | sed "s/$categoryName/\n/g"  | tail -2  | head -1 | cut -d ">" -f2 | cut -d "<" -f1 > totalPages
	totalPages=`cat totalPages`
	for (( i = 1; i <= "$totalPages"; i++ )); do # Looping for all the pages
		echo "Current page $i" > currentPage.temp
		tempURL="$indexURL"/page/"$i"
		echo "Started downloading $tempURL"
		echo -ne "\033]0;$tempURL; Total Pages-> $totalPages\007"
		curl -s "$tempURL" > temp.html	
		cat temp.html | egrep "class.*?thumb" -A 2 | grep "href"  | sed -E "s|^.*\"/([^\"]*).*$|\1|g" | while read line
		do # Visiting each wallpaper's page present on temp.html
			finalURL="$URL""$line"
			wallPage="$URL"`curl -s "$finalURL" | grep -i "original" -A 2 |  egrep -i "href=.*?view"  | head -1 | sed -E "s|^.*?href=\"/([^\"]*).*?$|\1|g"`
			wall="$URL"`curl -s "$wallPage" | sed -n -E "s|^.*?href.*?(download[^\"]+).*|\1|p"  | sort | uniq | head -1` # Extracting the final wallpaper page from current page
			wget -q "$wall"
			echo "$wall"
			echo "$finalURL"="$wallPage"="$wall" >> completeList.list
		done
		printf "\033c"

		echo "Done downloading $tempURL"
	done
	cd "$MAIN_DIR"
	# sleep 5
done