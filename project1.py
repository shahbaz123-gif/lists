def square_odd_even_separator():
    """Create squares list and separate odd/even values"""
    
    try:
        # Get user input
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        
        # Validate range
        if start > end:
            print("Starting number should be less than or equal to ending number!")
            return
        
        # Create list of squares
        squares = [num**2 for num in range(start, end + 1)]
        
        # Separate odd and even squares
        odd_squares = [sq for sq in squares if sq % 2 != 0]
        even_squares = [sq for sq in squares if sq % 2 == 0]
        
        # Display results
        print(f"\nOriginal numbers range: {start} to {end}")
        print(f"Squares list: {squares}")
        print(f"Odd squares: {odd_squares}")
        print(f"Even squares: {even_squares}")
        
    except ValueError:
        print("Please enter valid integers!")

# Run the program
square_odd_even_separator()