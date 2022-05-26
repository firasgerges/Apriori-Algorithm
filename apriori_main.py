import itertools
def is_number_allowed(num): # used to check if the min support and confidence are valid or not when entered by the user
	try:
		num=float(num);
	except ValueError:
		return False;
	if num < 0 or num >100:
		return False;
	return True;
def is_db_number_allowed(num): # used to check if the DbB number to use is valid or not when entered by the user
	try:
		num=int(num);
	except ValueError:
		return False;
	if num < 1 or num >5:
		return False;
	return True;
def support(items,transactions): # function to compute the support of the item set 'items' from the transactions list
	num_of_transactions=len(transactions);
	counter=0;
	for tran in transactions:
		if set(items).issubset(tran):
			counter=counter+1;
	support=(float(counter)/num_of_transactions)*100;
	return support;
def generate_sub_sets(items,cycle): #generate all subsets of the items list of lenght cycle
	return list(itertools.combinations(items,cycle));
def readItems():
	Items=[];
	ItemsFile=open('items.txt','r'); # reading the items for file called items.txt
	Items=ItemsFile.readlines();
	ItemsFile.close();
	for i in range(0,len(Items)): #cleaning input
		Items[i]=Items[i].strip('\n');
	return Items;
def readTransactions(db_current):
	fileDB="DB"+str(db_current);
	TransDB=open(fileDB+".txt",'r');#read lines of transaction DB, clean them and put them in a 2D array
	lines=TransDB.readlines();
	TransDB.close();
	transactions=[];# each row correspond to a transaction, each element in a row correspond to an item
	for i in range(0,len(lines)):
		transaction_inst = lines[i].strip('\n');
		print("Transaction "+str(i+1)+": "+transaction_inst);
		transactions.append(transaction_inst.split(','));
	return transactions;
	
def AprioriRun():
	#variables
	Min_Support=-1;Min_Confidence=-1;db_current=-1;
	print("---------------------------------------------------------------------");
	while not is_db_number_allowed(db_current):	#reading min support and confidence from user and DB number
		db_current=input("Please enter DB number to user (A number between 1 and 5) ");
	while not is_number_allowed(Min_Support):
		Min_Support=input("Please enter Min Support (A number between 0 and 100): ");
	while not is_number_allowed(Min_Confidence):
		Min_Confidence=input("Please enter Min Confidence (A number between 0 and 100) ");
	print("Proccessing Transcation DB: "+str(db_current));print("The Min Support is: "+str(Min_Support));print("The Min Confidence is: "+str(Min_Confidence));
	Min_Support=float(Min_Support);Min_Confidence=float(Min_Confidence);db_current=int(db_current);
	Items=readItems(); # list to store all the items
	transactions=readTransactions(db_current);	
	ItemSetsCycles=[];NotFrequentSets=[];
	ItemSets=Items.copy();
	ItemsInSet=1
	while ItemsInSet<=len(Items):#start with generating frequent ItemsInSet-itemset
		#get candidate itemsets of lenght ItemsInSet (to get from them the frequent)
		cycle_itemlist=generate_sub_sets(ItemSets,ItemsInSet)
		frequent=[];
		for itemlist in cycle_itemlist:
			itemlist=list(itemlist);
			to_ignore=False;
			for not_frequent in NotFrequentSets: # ignore all superset of non-frequent set
				if set(not_frequent).issubset(itemlist):
					to_ignore=True;break;
			if to_ignore:
				continue;
			if support(itemlist,transactions) >= Min_Support:#if item set is frequent, add it to frequent itemsets
				frequent.append(itemlist.copy());
			else:
				NotFrequentSets.append(itemlist.copy());
		if len(frequent)<1:
			break;
		ItemSetsCycles.append(frequent.copy());# ItemSetsCycles contains all the frequent item sets
		ItemsInSet=ItemsInSet+1; #increment the number if items in itemsets for next cycle
	AssociationRules=[];# Rules are stored in AssociationRules list. each rule is a list of four elements [0], [1],[3],[4]
	#[0] represent the left items in the association rule, [1] is for the right ones.-- [0]=>[1]
	#[3] and [4] are the support and confidence of each the association rule respectively
	for i in range(1,len(ItemSetsCycles)):#Getting the candidate association rules from ItemSetsCycles but ignoring the item sets of one item each .
		for itemlist in ItemSetsCycles[i]:			
			rule_support = support(itemlist,transactions);#compute support of rules from this itemlist
			for i in range(1,len(itemlist)):
				subsets=generate_sub_sets(itemlist,i);#generate all subsets of the itemList,
				for leftSide in subsets:#and the candidate rules are every susbset (at the left), and the remaining items (at the right)
					leftSide=list(leftSide);
					rightSide=itemlist.copy();
					for item in leftSide:
						rightSide.remove(item);
					rule_confidence=(rule_support/support(leftSide,transactions))*100 #get confidence of rule
					#if confidence greater than or equal to min confidence, add the  candidate rule to the association rules list
					if rule_confidence >= Min_Confidence:
						AssociationRules.append([leftSide,rightSide,rule_support,rule_confidence]);
	print("Association Rules: (Left=>Right[Support, Confidence])")		
	for rule in AssociationRules:
		print(','.join(rule[0])+" => "+ ','.join(rule[1]) + " [ "+str("{:.1f}".format(rule[2]))+"% , "+str("{:.1f}".format(rule[3]))+"% ]");
	print("---------------------------------------------------------------------------------------------------------------------------------");


if __name__== "__main__":
	Rerun='y'
	while Rerun=='y' or Rerun=='Y':
		AprioriRun();
		Rerun=input("Do You want to Re-run the programme: ('y' for yes)");
