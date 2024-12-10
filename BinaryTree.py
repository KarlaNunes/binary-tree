from collections import deque

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

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, key):
    if node is None:
        return node

    # Localizar nó a ser removido
    if key < node.value:
        node.left = delete(node.left, key)
    elif key > node.value:
        node.right = delete(node.right, key)
    else:
        # Caso 1: Nó sem filhos
        if node.left is None and node.right is None:
            return None
        
        # Caso 2: Nó com um filho
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        # Caso 3: Nó com dois filhos
        else:
            min_node = find_min(node.right)  # Encontrar sucessor 
            node.value = min_node.value  # Substituir valor pelo sucessor
            node.right = delete(node.right, min_node.value)  # Remover sucessor 

    return node

def preorder(node):
    if node:
        print(node.value, end=" ")  
        preorder(node.left)
        preorder(node.right)
        
def inorder(node):
    if node:
        inorder(node.left) 
        print(node.value, end=" ")  
        inorder(node.right)
        
def postorder(node):
    if node:
        postorder(node.left)  
        postorder(node.right) 
        print(node.value, end=" ")

def level_order(root):
    if root is None:
        return 
    
    queue = deque()
    queue.append(root)
    
    while queue:  
        current_node = queue.popleft()
        print(current_node.value, end=" ") 
        
        # Enfileirar os filhos 
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)  
        print(" " * 4 * level + "->", node.value)  
        print_tree(node.left, level + 1)  
                
if __name__ == "__main__":
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        root = insert(root, value)
    
    print_tree(root)
    
    print("\nNúmero total de nós na árvore:", count_nodes(root))
    print("Número total de folhas na árvore:", count_leaves(root))
    
    print("\nEscolha o tipo de percurso:")
    print("1 - Pré-ordem (preorder)")
    print("2 - Simétrica (inorder)")
    print("3 - Pós-ordem (postorder)")
    print("4 - Em nível (level order)")
    
    option = int(input("Digite o número correspondente ao tipo de percurso: "))
    
    print("\nValores do percurso:")
    if option == 1:
        print("Pré-ordem:")
        preorder(root)
    elif option == 2:
        print("Simétrica:")
        inorder(root)
    elif option == 3:
        print("Pós-ordem:")
        postorder(root)
    elif option == 4:
        print("Em nível:")
        level_order(root)
    else:
        print("Opção inválida!")