print_style () {
	for (( i = 0; i < 20; i++ )); do
		printf "."
		sleep 0.1
	done
	echo ""
}

check_category () {
	# echo entered here
	if [[ "$1" -eq 0 ]] >/dev/null 2>/dev/null ; then
		echo "1"
		return
	fi
	numbers=`cat "$2" | egrep -o "^[0-9]+"`
	# echo "numbers are this"
	# echo "$numbers"
	# read a
	echo "$numbers" | egrep "^$1$" > /dev/null 2>/dev/null
	if [[ "$?" -eq 0 ]]; then
		echo "1"
		return
	fi
	echo "0"
}

home_page='.93c4f9293f239af6fe3db5c0d933c91e.html'
temp='.3d801aa532c1cec3ee82d87a99fdf63f.html'
complete_list='.c6c15056705a75f9fd8fa006aa9435e8'
readable='.500f1c435067a26384c6b38f464da461'
current='.43b5c9175984c071f30b873fdce0a000'
echo -ne "\033]0;Download wallpapers from best-wallpaper.net\007"
printf "\033c"
web='http://www.best-wallpaper.net'

man wget >/dev/null 2>/dev/null
if [[ "$?" -ne 0 ]]; then
	echo 'Command wget not found, first install wget to proceed...'
	exit 0
fi

echo 'Retrieving all the categories from the website, please be patient..!!'

print_style

wget -O "$home_page" "$web"
>$complete_list

for i in `cat $home_page | grep 'class="item_left"' | grep -P -v  "[0-9]+x[0-9]+" | egrep -o "href=\"[^\"]+" | cut -d "\"" -f2 | egrep "^\/"`
do
	wget -O "$temp" $web$i ; pages=`cat $temp | grep -A 1 '<div class="pg_pointer">' | sed "s/href/\n/g" | tail -2 | head -1 | egrep -o ">[0-9]+<" | egrep -o "[0-9]+"`; echo "$i=$pages" >> $complete_list
done



cat $complete_list > $current

count=1
printf "\033cEnter the number of the category that you want to download. (enter 0 for downloading all the categories)\n"
# echo 'Enter the number of the category that you want to download. (enter 0 for downloading all the categories)'
for i in `cat $complete_list`
do
	printf "$count.->"
	echo $i | cut -d "_" -f1 | sed "s/\///g"
	count=$(($count+1))
done > $readable
cat $readable
echo 'Press 0 for downloading all the categories of wallpapers (may take long time because of large number of wallpapers)'
flag=0

# echo Here
read category
# check_category $category $readable
flag=`check_category $category $readable`
# echo Here again $flag
# read a
while [[ "$flag" -eq 0 ]]; do
	echo "Input correct value."
	read category
	flag=`check_category $category $readable`
done

if [[ "$category" -eq 0 ]]; then
	echo "Downloading all the categories may take long time beacuse of large number of wallpapers, do you want to proceed (y/n)"
	read decision
	flag=0
	if [[ "$decision" == "y" || "$decision" == "Y"  ]]; then
		flag=1
	fi
fi

if [[ "$flag" -eq 0 ]]; then
	echo "Exiting the script"
	exit 0
fi

if [[ "$category" -ne 0 ]]; then
	# echo "Entered here"
	content=`cat $readable | egrep "^$category" | cut -d ">" -f2`
	# echo $content is this
	# read a
	# cat "$complete_list" | grep "$content" > "$current"
	awk "NR==$category" $complete_list | grep "$content" > "$current"
fi

echo "Going for the final showdown for the category $content in three seconds.."
for (( i = 1; i < 4; i++ )); do
	echo $i.
	sleep 1
done

# cat $current
# read a
for id in `cat $current`
do
	printf "\033c"
	# new=`echo $id | sed -e "s/.html.*//g" | sed -e "s/^\///g"`
	totalPage=`echo $id | rev | cut -d "=" -f 1 | rev`
	echo -ne "\033]0;$content; Total Pages-> $totalPage\007"
	current_dir=`pwd`
	directory=`echo $id | cut -d "_" -f1 | sed "s/\///g"`
	address=`echo $id | cut -d "=" -f1 | sed -e "s/\.html/\/page\//g"`
	address="$web""$address"
	pages=`echo $id | cut -d "=" -f2`
	mkdir -p $directory
	cd $directory

	page=1
	ls list > /dev/null 2>/dev/null

	if [[ "$?" -eq 0 ]]; then
		page=`cat list | tail -1 | egrep -o "[0-9]*$"`
	fi
	
	if [[ "$flag" -eq 1 ]]; then
		echo $pages > total.log
	fi

	flag=0
	# echo  $page
	# echo $pages
	for i in `seq $page $pages`
	do
		printf "\033cPage number $i\n"
		echo $i > page.log
		wget -O temp.html "$address""$i"
		for j in `cat temp.html | grep '<div class="pic_list_img">' | grep -o "href=\"[^\"]*" | cut -d "\"" -f2`
		do
			wget -O test1.html "$web""$j"
			new=`cat test1.html | grep -A 1 "16:9" | grep 'target="_blank"' | sed "s/href/\n/g" | tail -1  | cut -d "\"" -f2`
			wget --referer "$web""$j" -U "Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0" -O test2.html "$web""$new"
			final=`cat test2.html  | grep '<img src="/wallpaper/' | cut -d "\"" -f2`
			name=`echo $final | rev | cut -d "/" -f1 | rev`
			wget --referer "$web""$new" -U "Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0" -O $name "$web""$final"
			echo "$name $i" >> list
			flag=1
		done

	done
	cd $current_dir
done	
