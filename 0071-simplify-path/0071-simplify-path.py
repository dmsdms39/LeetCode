import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        st = []
        result = '/'

        for comp in components:
            if comp == '' or comp == '.':
                continue

            if comp == '..':
                if st:
                    st.pop()
            else:
                st.append(comp)

        return result + '/'.join(st)


        