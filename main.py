from fastapi import FastAPI, status, HTTPException, Depends
from google.cloud import bigquery

app = FastAPI()

# Dependency method to provide a BigQuery client
# This will be used by the other endpoints where a database connection is necessary
def get_bq_client():
    # client automatically uses Cloud Run's service account credentials
    client = bigquery.Client()
    try:
        yield client
    finally:
        client.close()



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
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="a, b, and c must be valid numbers")
    
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


@app.get("/dbwritetest", status_code=200)
def dbwritetest(bq: bigquery.Client = Depends(get_bq_client)):
    """
    Writes a simple test row to a BigQuery table.

    Uses the `get_bq_client` dependency method to establish a connection to BigQuery.
    """
    # Define a Python list of objects that will become rows in the database table
    # In this instance, there is only a single object in the list
    row_to_insert = [
        {
            "endpoint": "/dbwritetest",
            "result": "Success",
            "status_code": 200
        }
    ]
    
    # Use the BigQuery interface to write our data to the table
    # If there are errors, store them in a list called `errors`
    # YOU MUST UPDATE YOUR PROJECT AND DATASET NAME BELOW BEFORE THIS WILL WORK!!!
    errors = bq.insert_rows_json("mgmt545project-carls171.calculator.api_logs", row_to_insert)

    # If there were any errors, raise an HTTPException to inform the user
    if errors:
        # Log the full error to your Cloud Run logs for debugging
        print(f"BigQuery Insert Errors: {errors}")
        
        # Raise an exception to the API user
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "Failed to log data to BigQuery",
                "errors": errors  # Optional: return specific BQ error details
            }
        )

    # If there were NOT any errors, send a friendly response message to the API caller
    return {"message": "Log entry created successfully"}