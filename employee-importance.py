"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        emp_id = {emp.id:i for i,emp in enumerate(employees)}

        def dfs(emp):
            nonlocal ans
            ans += emp.importance
            if not emp.subordinates:
                return
            
            for sub in emp.subordinates:
                dfs(employees[emp_id[sub]])

        dfs(employees[emp_id[id]])
        return ans