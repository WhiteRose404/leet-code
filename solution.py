from math import inf;

class Solution:
    def candy(self, ratings) -> int:
        print("New test")
        candies = 0;
        len_rat = len(ratings);
        if(len_rat == 1): return 1;
        asec = ratings[0] < ratings[1];
        phase1 = [];
        bus = [ratings[0]];
        for i in range(1, len_rat):
            if((ratings[i-1]>=ratings[i] and asec) or (ratings[i-1]<=ratings[i] and not asec)):
                # handle when i == len - 1
                phase1.append(bus);
                bus = [];
                asec = not asec;
            bus.append(ratings[i]);
            
        phase1.append(bus);
        last_subarr = {
            'asec': False,
            'last': inf,
            'length': -1
        }
        for subarray in phase1:
            length = len(subarray);
            if(length == 0):
                # bad code: phase1 should not have empty subarrays
                continue;
            
            # print(subarray, length, last_subarr);
            #if(subarray[-1] < subarray[-2]):
            # there are 2 cases to be handled
            #   desc asec ----> [4321] [578] ----([4321] [56789])
            #   asec desc ----> [1234] [867] ----([124] [876])
            debug = candies;
            candies += length * (length + 1) // 2;
            if(last_subarr['length'] != -1):
                if(length == 1 and last_subarr['length'] == 1):
                    if(subarray[0] > last_subarr['last']): candies += 1;
                    elif(subarray[0] < last_subarr['last']): candies += 1;
                    print("handled");
                elif(last_subarr['asec']):
                    if(subarray[0] > last_subarr['last'] and last_subarr['length'] < length):
                        candies += (length - last_subarr['length']);
                    elif(subarray[0] < last_subarr['last'] and last_subarr['length'] <= length):
                        candies += (length - last_subarr['length'] + 1);
                elif(not last_subarr['asec'] and subarray[0] != last_subarr['last']):
                    candies += length;
            print("Subarray: ", subarray, "Candies: ", candies, "Gained: ", candies - debug)
            last_subarr['length'] = len(subarray);
            last_subarr['asec'] = False if last_subarr['length'] <= 1 else subarray[-2] < subarray[-1];
            last_subarr['last'] = subarray[-1];
        print("Candies: ", candies, "\n");
        return candies;


    def attempt(self, ratings) -> int:
        s = [1] * len(ratings);
        flag = True;
        while(flag):
            flag = False;
            for j in range(len(ratings)):
                if( j != len(ratings) - 1):
                    if(ratings[j] > ratings[j+1] and s[j] <= s[j+1]):
                        s[j] = s[j+1] + 1
                        flag = True
                if(j and ratings[j] > ratings[j-1] and s[j] <= s[j-1]):
                        s[j] = s[j-1] + 1
                        flag = True 
        return sum(s)


