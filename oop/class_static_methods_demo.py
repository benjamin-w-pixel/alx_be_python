# class_static_methods_demo.py

class Calculator:
    """A calculator demonstrating class and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """Static method to add two numbers.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers.
        
        Args:
            cls: Reference to the class
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b