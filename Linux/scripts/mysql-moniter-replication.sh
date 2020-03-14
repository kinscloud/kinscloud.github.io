#!/bin/bash
mysql -uroot -p1qaz@WSX123 -e 'show slave status\G' | grep -E \
"Slave_IO_Running|Slave_SQL_Running" | awk '{print $2}' | grep -c Yes