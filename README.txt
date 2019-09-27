INSTRUCTIONS:
1. The script runs on  python3+.
2. Have the CSVFILE.csv containing the CIDR blocks in the same directory as the script
3. The script gives four outputs: Invalid blocks on display, valid, private and public on seperate yaml files


PREREQUISITES:
    Have Python3.6 installed

TESTING

1. Running the script with a wrong csv file:
        $ ./validate_ip.py
        Filename(a .csv file) $ test.csv

    Output
        No file 'test.csv' in the current path

2. Running the script with a non-csv file:
        $ ./validate_ip.py
        Filename(a .csv file) $ test.txt
    Output
        csv file required

3. For a successful run:
        $ ./validate_ip.py
        Filename(a .csv file) $ cidr.csv 
        CIDR column name $ IP

         Invalid block: 
        169.102.30.46/7
        169.102.30.44/66
        169.102.30.45/21
        169.102.30.46/7
        169.102.3044.47/67
        169.102.30.48/6
        169.102.30.49/789
        169.102.30.48/6
        fdfdf
        4
        All valid, private and public adresses output: "public.yaml", "private.yaml", "all_valid.yaml"

ls
all_valid.yaml private.yaml public.yaml validate_ip.py 