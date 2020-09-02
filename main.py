while True:
    import random
    peter_list = ["The girl I love is realy sick right now","It has been a really busy week", "You might have a sister in law", "I'm at the gym, gimme 5", "Going to get tacos with the boys", "Can I have the Hulu password", "No comment","Nice nice","Just asking","sounds good","Thx", "Hey how's it going","oof","Not much just checking in","You dont deserve an answer","I am not apologizing"]
    peter_list = random.choice(peter_list)
    print("text peter")
    answer1=input()
    if "" in answer1:
        print (peter_list)
    

