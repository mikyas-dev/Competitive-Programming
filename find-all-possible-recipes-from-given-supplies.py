class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        adj = defaultdict(list)
        d = defaultdict(int)
        for i, recipe in enumerate(recipes):
            for ingred in ingredients[i]:
                adj[ingred].append(recipe)
                d[recipe] += 1
                if(ingred not in d):
                    d[ingred] = 0
        stack = deque()
        recipes = set(recipes)
        supplies = set(supplies)
        ans = []
        for i in d:
            if(d[i] == 0 and i in supplies):
                stack.append(i)
        while(stack):
            temp = stack.popleft()
            supplies.add(temp)
            if(temp in recipes):
                ans.append(temp)
            for child in adj[temp]:
                d[child] -= 1
                if(d[child] == 0):
                    stack.append(child)
        return ans