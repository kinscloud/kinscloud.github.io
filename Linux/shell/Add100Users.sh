#/bin/bash

#批量创建100个用户并设备密码
USER_FILE=./user.info
for USER in user{1..100}; then
	if ! id $USER &> /dev/null; then
		PASS = $(echo $RANDOM | md5sum | cut -c 1-8)
		useradd $USER
		echo $PASS | passwd --stdin $USER
		echo "$USER $PASS" >>  $USER_FILE
		echo "$USER User create sucessful."
	else
		echo "$USER already exists!"
	fi
done