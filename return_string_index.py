# Enter your code here. Read input from STDIN. Print output to STDOUT

# take a string 'abchelloabcabcabchellohello' , print every index where a substring occurs . sub_str : 'abc' abc - 0 , abc 

# "hello" # "abc" , "he" , "bche "

import re

while True:
    test_string = 'abchelloabcabcabchellohello'
    print("Enter string to test: ")
    match_string = input()
    len_match_string = len(match_string)
    repl_str = ""

    for i in range(len_match_string):
        repl_str = repl_str + '1'

    while True:
        res = re.search(match_string, test_string)
        if res:
            print("Index is: {}".format(res.start()))
            test_string = re.sub(match_string, repl_str, test_string, count=1)
        else:
            break
