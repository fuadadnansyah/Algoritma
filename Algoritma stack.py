# ===============================================
#      ALGORITMA STACK (Last In First Out)
# ===============================================

class Stack:
    def __init__(self):
        self.data = []   # tempat penyimpanan stack

    # PUSH → menambahkan data ke atas stack
    def push(self, value):
        self.data.append(value)
        print(f"Push: {value}")

    # POP → mengambil data paling atas
    def pop(self):
        if self.is_empty():
            print("Stack kosong, tidak bisa pop!")
            return None
        value = self.data.pop()
        print(f"Pop: {value}")
        return value

    # PEEK → melihat data paling atas
    def peek(self):
        if self.is_empty():
            print("Stack kosong, tidak ada yang di-peek!")
            return None
        return self.data[-1]

    # Mengecek apakah stack kosong
    def is_empty(self):
        return len(self.data) == 0

    # Menampilkan isi stack
    def display(self):
        print("Isi Stack:", self.data)


# =====================================================
#                  CONTOH PENGGUNAAN
# =====================================================

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Data paling atas (peek):", stack.peek())

stack.pop()
stack.pop()

stack.display()
