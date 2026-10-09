class Expense:
    def __init__(self, category, amount, desc):
        self.category = category
        self.amount = amount
        self.desc = desc

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.root = TrieNode()

    def add_expense(self, category, amount, desc):
        # OOP - object creation
        exp = Expense(category, amount, desc)
        self.expenses.append(exp)
        self._add_to_trie(category)
        print(f"Added: {category} - ${amount}")

    def _add_to_trie(self, word):
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def get_top_expenses(self, n=3):
        # DSA - Heap concept using sort
        import heapq
        return heapq.nlargest(n, self.expenses, key=lambda x: x.amount)

    def search_category(self, prefix):
        # DSA - Trie search O(m)
        node = self.root
        for ch in prefix.lower():
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Demo
tracker = ExpenseTracker()
tracker.add_expense("Food", 50, "Lunch")
tracker.add_expense("Travel", 120, "Train to London")
tracker.add_expense("Food", 80, "Dinner")
print("Top expenses:", [(e.category, e.amount) for e in tracker.get_top_expenses()])
print("Search 'Fo':", tracker.search_category("Fo"))
