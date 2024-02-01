# ceiling.py by Raj Reddy for CS 4150 (1/24/24) coded in Python

def star_distance(x1, y1, x2, y2, d):
    # (x1-x2)2 + (y1-y2)2 ≤ d2
    if (((x1 - y1) ** 2) + ((x2 - y2) ** 2)) <= (d ** 2):
        return True
    else:
        return False
    

def main():
    
    d, k = map(int, input().split())
    
    for i in range (k):
        vals = list(map(int, input().split()))
    
    
        
    
    

# if __name__ == "__main__":
#     result = main()
#     print(result)