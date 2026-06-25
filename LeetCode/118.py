class Solution(object):
    def generate(self, numRows):
        l = []
        if numRows == 0:
            return l
        l.append([1])
        for i in range (1,numRows):
            prev_r = l[i-1]
            curr_r = [1]

            for j in range (1,i):
                curr_r.append(prev_r[j-1]+ prev_r[j])
            curr_r.append(1)
            l.append(curr_r)
        return l
        
