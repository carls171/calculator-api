from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be valid numbers")
    return {"result": a + b}

@app.get("/subtract/{a}/{b}", status_code=200)
def sub(a: str, b: str):
    """
    Subtract one number from the other.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be valid numbers")
    return {"result": a - b}

@app.get("/multiply/{a}/{b}", status_code=200)
def multi(a: str, b: str):
    """
    Multiply two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be valid numbers")
    return {"result": a * b}



@app.get("/devide/{a}/{b}", status_code=200)
def dev(a: str, b: str):
    """
    Devide two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a and b must be valid numbers")

    if b == 0:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="The value of b can not be zero")
    
    return {"result": a / b}


@app.get("/avgerage/{a}/{b}/{c}", status_code=200)
def tri(a: str, b: str, c: str):
    """
    Find the average of three numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    - c: Third number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both a, b, and c must be valid numbers")
    
    return {"result": ((a+b+c)/3)}


@app.get("/areatri/{a}/{b}", status_code=200)
def areatri(a: str, b: str):
    """
    Find the area of a triangle.
    
    Parameters:
    - a: height number
    - b: base number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both base and height must be valid numbers")

    if (a <= 0) or (b <= 0):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Base and Height must be greater than zero")
    return {"result": (a * b)/2}

from math import sqrt
@app.get("/hypo/{a}/{b}", status_code=200)
def hypotenuse(a: str, b: str):
    """
    Find the hypotenuse of a right triangle.
    
    Parameters:
    - a: Side one number
    - b: Side two number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both sides must be valid numbers")

    if (a <=0) or (b <= 0):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Both sides must be greater than zero")
    return {"result": sqrt(a**2 + b**2)}