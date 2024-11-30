import numpy as np  

def calculate(numbers):  
    if len(numbers) != 9:  
        raise ValueError("List must contain nine numbers.")  
    
    # Convert the list to a 3x3 numpy array  
    matrix = np.array(numbers).reshape(3, 3)  
    
    calculations = {  
        'mean': [  
            matrix.mean(axis=0).tolist(),     # Mean of each column  
            matrix.mean(axis=1).tolist(),     # Mean of each row  
            matrix.mean().tolist()             # Mean of the flattened array  
        ],  
        'variance': [  
            matrix.var(axis=0).tolist(),      # Variance of each column  
            matrix.var(axis=1).tolist(),      # Variance of each row  
            matrix.var().tolist()              # Variance of the flattened array  
        ],  
        'standard deviation': [  
            matrix.std(axis=0).tolist(),      # Std deviation of each column  
            matrix.std(axis=1).tolist(),      # Std deviation of each row  
            matrix.std().tolist()              # Std deviation of the flattened array  
        ],  
        'max': [  
            matrix.max(axis=0).tolist(),      # Max of each column  
            matrix.max(axis=1).tolist(),      # Max of each row  
            matrix.max().tolist()              # Max of the flattened array  
        ],  
        'min': [  
            matrix.min(axis=0).tolist(),      # Min of each column  
            matrix.min(axis=1).tolist(),      # Min of each row  
            matrix.min().tolist()              # Min of the flattened array  
        ],  
        'sum': [  
            matrix.sum(axis=0).tolist(),      # Sum of each column  
            matrix.sum(axis=1).tolist(),      # Sum of each row  
            matrix.sum().tolist()              # Sum of the flattened array  
        ]  
    }  
    
    print(calculations)
    
calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])  
