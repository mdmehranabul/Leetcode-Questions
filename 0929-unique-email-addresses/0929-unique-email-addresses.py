class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # hashset=set()

        # for id in emails:
        #     local,domain=id.split("@")
        #     local=local.split("+")[0]
        #     local=local.replace(".","")
        #     print(local,domain)

        #     hashset.add((local,domain))
        
        # return len(hashset)

        hashset=set()
        for id in emails:
            i=0
            local=""
            while id[i] not in ["@","+"]:
                if id[i] !=".":
                    local+=id[i]
                i+=1
            
            while id[i]!="@":
                i+=1
            domain=id[i+1:]
            hashset.add((local,domain))
        return len(hashset)


        