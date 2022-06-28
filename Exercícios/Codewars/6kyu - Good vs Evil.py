def good_vs_evil(good, evil):
    
    good_team = good.split()
    for i in range(0, len(good_team)):
        good_team[i] = int(good_team[i])
    
    evil_team = evil.split()
    for i in range(0, len(evil_team)):
        evil_team[i] = int(evil_team[i]) 
    
    
    good_team_sum = 1*good_team[0]+2*good_team[1]+3*good_team[2]+3*good_team[3]+4*good_team[4]+10*good_team[5]  
    evil_team_sum = 1*evil_team[0]+2*evil_team[1]+2*evil_team[2]+2*evil_team[3]+3*evil_team[4]+5*evil_team[5]+10*evil_team[6]
    
    if good_team_sum > evil_team_sum:
        battle_result = "Battle Result: Good triumphs over Evil"
    elif good_team_sum < evil_team_sum:
        battle_result = "Battle Result: Evil eradicates all trace of Good"
    else:
        battle_result = "Battle Result: No victor on this battle field"
    return battle_result