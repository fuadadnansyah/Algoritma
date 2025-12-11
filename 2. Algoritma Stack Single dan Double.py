# ============================================
#   Algoritma Stack Single dan Stack Double
#   By: Fuad Adnansyah
# ============================================

print("\n=== STACK SINGLE ===")

# Stack Single
stack_single = []

# Push
stack_single.append("Data 1")
stack_single.append("Data 2")
stack_single.append("Data 3")

# Pop
pop_single = stack_single.pop()

print("Isi Stack Single:", stack_single)
print("Data yang di-pop :", pop_single)


print("\n=== STACK DOUBLE ===")

# Stack Double dalam satu list
size = 10
stack_double = [None] * size
top1 = -1
top2 = size

# Push Stack 1
top1 += 1
stack_double[top1] = "A"

# Push Stack 2
top2 -= 1
stack_double[top2] = "B"

print("Isi Memori Stack Double:", stack_double)
print("Top1 berada di index:", top1)
print("Top2 berada di index:", top2)
