from math import inf;

class Solution:
    def candy(self, ratings) -> int:
        candies = 0;
        len_rat = len(ratings);
        if(len_rat == 1): return 1;
        asec = ratings[0] < ratings[1];
        phase1 = [];
        bus = [ratings[0]];
        for i in range(1, len_rat):
            if((ratings[i-1]>=ratings[i] and asec) or (ratings[i-1]<=ratings[i] and not asec)):
                # handle when i == len - 1
                if(len(bus) == 1 and ratings[i-1] != ratings[i]):
                    bus.append(ratings[i]);
                    asec = ratings[i-1] < ratings[i];
                    continue;
                phase1.append(bus);
                bus = [];
                asec = not asec;
            bus.append(ratings[i]);
        phase1.append(bus);
        last_subarr = {
            'asec': None,
            'last': inf,
            'length': -1
        };
        add_on = 0;
        for subarray in phase1:
            length = len(subarray);
            if(length == 0):
                # bad code: phase1 should not have empty subarrays
                continue;
            candies += length * (length + 1) // 2;
            current_subarr = {
                'length': len(subarray),
                'asec': None if len(subarray) <= 1 else subarray[-2] < subarray[-1],
                'last': subarray[-1]
            }
            if(last_subarr['length'] != -1):
                if(current_subarr['length'] == 1):
                    if(last_subarr['last'] < subarray[0] and not last_subarr['asec']):
                        candies += 1;
                if(last_subarr['asec'] and not current_subarr['asec']):
                    if(last_subarr['last'] > subarray[0]):
                        if(current_subarr['length'] >= last_subarr['length']):
                            candies += (current_subarr['length'] - last_subarr['length'] + 1) - add_on;
                add_on = 0;
                if(not last_subarr['asec'] and current_subarr['asec']):
                    if(last_subarr['last'] < subarray[0]):
                        candies += length - add_on; 
                        add_on = 1;
            last_subarr['length'] = len(subarray);
            last_subarr['asec'] = None if last_subarr['length'] <= 1 else subarray[-2] < subarray[-1];
            last_subarr['last'] = subarray[-1];
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


