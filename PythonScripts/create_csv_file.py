import csv
# req_file="/home/jeremy/Documents/gitStuff/ultrapython3/PythonScripts/new_info.csv"

# fo=open(req_file,'r')
# csv_reader=csv.reader(fo,delimiter="|")
# for each_row in csv_reader:
#     print(each_row)

# fo.close()

req_file="/home/jeremy/Documents/gitStuff/ultrapython3/PythonScripts/demo.csv"
fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo,delimiter=",")
# csv_writer.writerow(['S_No',"Name",'Age'])
# csv_writer.writerow([1,"John",23])
# csv_writer.writerow([2,"Clinton",24])
my_data=[['S_No',"Name",'Age'],[1,"John",23],[2,"Clinton",24]]
csv_writer.writerows(my_data)
fo.close()














