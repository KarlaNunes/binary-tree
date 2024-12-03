class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    
    if key < node.value:
        node.left = insert(node.left, key)
    elif key > node.value:
        node.right = insert(node.right, key)
    else:
        print("Esse nó já existe na árvore!")
        
    return node

def search(node, key):
    if node is None or node.value == key:
        return node

    if key < node.value:
        return search(node.left, key)
    return search(node.right, key)

def count_nodes(node):
    if node is None:
        return 0
    return count_nodes(node.left) + count_nodes(node.right) + 1

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:  # Nó sem filhos
        return 1
    return count_leaves(node.left) + count_leaves(node.right)
    

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)  
        print(" " * 4 * level + "->", node.value)  
        print_tree(node.left, level + 1)  
                
if __name__ == "__main__":
    root = None 
    root_size = int(input("Quantos nós você quer na sua árvore? \n"))
    
    
    print("Digite os valores dos nós:")
    for _ in range(root_size):
        value = int(input(f"Nó {_ + 1}: "))
        root = insert(root, value)
    

    print("-------- Sua árvore: ---------")
    print_tree(root)
    
    print("Número total de nós na árvore:", count_nodes(root))
    print("Número total de folhas na árvore:", count_leaves(root))
    
    search_key = int(input("Qual valor você deseja buscar? \n"))
    found_node = search(root, search_key)
    if found_node:
        print(f"\nNó {search_key} encontrado!")
    else:
        print(f"\nNó {search_key} não encontrado.")