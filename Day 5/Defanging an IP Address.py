class Solution:
    def defangIPaddr(self, address: str) -> str:
        newaddress = re.sub("[.]","[.]",address) # replaces all occurrences of "." with "[.]"
        return newaddress
