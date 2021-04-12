# Keyfile Creation 

usage example: python3 createKeyfile.py -n 10 -k keyfile.txt

Keyfile.txt contains a space-separated list of key names and their data types.
createKeyfile.py creates a random keyfile.txt. It takes as argument the number
of lines to be created. There are 4 possible data types. "string", "int", 
"float" and "KV". KV stands for key-value and it means a nested key-valur pair.

# Data Creation

usage example: python3 createData.py -k keyFile.txt -n 1000 -d 3 -l 4 -m 5

# KV Broker

usage example: python3 kvBroker.py -s serverFile.txt -i dataToIndex.txt -k 2

After executing kvBroker all data contained in the data file will be indexed
to the servers. If the K-replication cannot be performed because there aren't
at least working K servers an error message will be displayed. Then, the 
command prompt will start and the user will be able to execute command and
create requests. There are 4 possible commands. 'GET', 'DELETE', 'QUERY' and 
'clear'. 'clear' just clears the terminal screen.

example 1: GET key_55
example 1: DELETE key_56
example 1: QUERY key_55.home.address.street

Note that, at the command prompt keys are used without quotes. GET key_55 
instead of GET "key_55".

# KV Server

usage example: python3 kvServer.py -a ip_address -p port

