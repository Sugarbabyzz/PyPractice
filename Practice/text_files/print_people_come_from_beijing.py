
import json

open_filename = 'test.txt'
out_filename = 'test_result.txt'
out_filename2 = 'test_result2.txt'
with open(open_filename) as file_object:
    for line in file_object:
        if "北京" in line:
            with open(out_filename, 'a') as f:
                f.write(line)


with open(open_filename) as file_object:
    for line in file_object:
        dict = eval(line)
        if dict['address'] == '北京':
            with open(out_filename2, 'a') as f:
                f.write(str(dict) + '\n')