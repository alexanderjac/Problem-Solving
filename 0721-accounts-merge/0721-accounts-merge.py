class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        [["John","johnsmith@mail.com","john_newyork@mail.com", "xyz@mail.com"],
        ["John1","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]]    
        
        {email(key) -> name(value)}
        
        "johnsmith@mail.com" = set("john_newyork@mail.com","john00@mail.com")
        "john_newyork@mail.com" = set("johnsmith@mail.com")
        "john00@mail.com" = set("johnsmith@mail.com")
        "mary@mail.com" = set()
        "johnnybravo@mail.com" = set()
        
        
        ["john", "johnsmith@mail.com","john_newyork@mail.com" "john00@mail.com"]
        
        {"johnsmith@mail.com" : set()
        
        """
        emailToName = {}
        adjList = {}
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                emailToName[account[i]] = name
                if account[i] not  in adjList:
                    adjList[account[i]] = set()
                if i ==1:
                    continue
                adjList[account[i]].add(account[i-1])
                adjList[account[i-1]].add(account[i])

#         for account in accounts:
#             # print(account)
#             for i in range(1, len(account)):
                
#                 for j in range(1, len(account)):
                    # if i ==j:
                    #     continue
                    # if account[i] in adjList:
                    #     print(account[i],account[j])
                    #     adjList[account[i]].add(account[j])
                    # else:
                    #     adjList[account[i]] = set()
                    #     adjList[account[i]].add(account[j])
        visited = set()
        result = []
        # print(adjList)
        for email in adjList.keys():
            sub = []
            if email not in visited:
                name = emailToName[email]
                
                # sub.append(name)
                # sub.append(email)
                self.dfs(sub, email, visited, adjList)
                sub.sort()
                sub =[name] +sub
                result.append(sub)
        return result
        
    def dfs(self, sub ,email,  visited, adj):
        visited.add(email)
        sub.append(email)
        setvalue = adj[email]
        for eml in setvalue:
            if eml not in visited:
                self.dfs(sub ,eml,  visited, adj)
            
 
          
            
                        
                
        
        