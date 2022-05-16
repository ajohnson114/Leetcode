class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.defaultdict(int)
        
        for domain in cpdomains:
            count, domain = domain.split() #this line splits the list entries on spaces (which separates the count and domain name)
            count = int(count)
            frags = domain.split('.') #this splits the domain on its periods
            for i in range(len(frags)): 
                ans[".".join(frags[i:])] += count #this iterates on the periods and puts it in a dictionary with domains as key and count as value
            
        return["{} {}".format(ct,dom) for dom, ct in ans.items()] #this puts our dictionary into a syntax our answer wants
