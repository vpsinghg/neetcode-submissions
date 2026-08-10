from collections import defaultdict, deque

class Solution:

    def __buildorder(self, comparisons:List[Tuple]) -> str:
        # 
        indegree = defaultdict(int)
        adjacency_list = defaultdict(list)
        for a, b in comparisons:
            indegree[b] += 1
            indegree[a] += 0
            adjacency_list[a].append(b)


        queue = deque(ch for ch in indegree if indegree[ch] ==0)
        result = ""
        while(queue):
            curr = queue.popleft()
            result += curr

            for node in adjacency_list[curr]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        print(result, len(indegree))
        return result if len(result) == len(indegree) else ""

    def foreignDictionary(self, words: List[str]) -> str:
        comparisons = set()
        character_set = set()

        # Every character must exist in the final answer
        for word in words:
            for ch in word:
                character_set.add(ch)

        # Compare adjacent words only
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            k = 0

            while (
                k < len(word1)
                and k < len(word2)
                and word1[k] == word2[k]
            ):
                k += 1

            # Invalid prefix:
            # "abc" cannot come before "ab"
            if k == len(word2) and k < len(word1):
                return ""

            # First different character gives the constraint
            if k < len(word1) and k < len(word2):
                comparisons.add(
                    (word1[k], word2[k])
                )
        if not comparisons:
            return "".join(character_set)
        ordered = self.__buildorder(list(comparisons))

        # Cycle / invalid ordering
        if ordered == "":
            return ""

        # Add characters that had no edges
        for ch in character_set:
            if ch not in ordered:
                ordered += ch

        return ordered        