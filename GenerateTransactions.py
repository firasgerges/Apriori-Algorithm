import random;

Items=[];
ItemsFile=open('items.txt','r');
Items=ItemsFile.readlines();
ItemsFile.close();
for i in range(0,len(Items)):
	Items[i]=Items[i].strip('\n');
NumberOfDB=5;
NumItemProb=[1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,6,6,7,8,9,10];
while NumberOfDB != 0:
	DbFile=open('DB'+str(NumberOfDB)+'.txt','w');
	NumberOfTransactions=20;
	while NumberOfTransactions != 0:
		print(str(NumberOfDB)+"--"+str(NumberOfTransactions))
		NumberOfItem=random.choice(NumItemProb);
		Transaction=[];
		while NumberOfItem != 0:
			item=random.choice(Items);
			if item not in Transaction:
				Transaction.append(item);
				NumberOfItem=NumberOfItem-1;
		Transaction_line=','.join(Transaction);
		DbFile.write(Transaction_line+'\n');
		NumberOfTransactions=NumberOfTransactions-1;
	DbFile.close();
	NumberOfDB=NumberOfDB-1;