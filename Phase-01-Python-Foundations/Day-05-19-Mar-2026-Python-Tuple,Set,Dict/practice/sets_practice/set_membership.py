# Membership and relation checks
fruits = {"apple", "banana", "cherry"}
print("'apple' in fruits?", "apple" in fruits)
print("'grape' not in fruits?", "grape" not in fruits)

a = {1, 2}
b = {1, 2, 3, 4}
c = {5, 6}

print("a subset of b:", a.issubset(b))
print("b superset of a:", b.issuperset(a))
print("a disjoint with c:", a.isdisjoint(c))

# frozenset is immutable set
frozen = frozenset({1, 2, 3})
print("frozenset:", frozen)
