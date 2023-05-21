import uvicorn
from fastapi import FastAPI
from app import app
from sr import sr

if __name__ == "__main__":
    try:
        # Create an instance of the FastAPI app
        api = FastAPI()

        # Mount the app and sr as sub-applications
        api.mount("/app", app)
        api.mount("/sr", sr)

        # Run the FastAPI server using uvicorn
        uvicorn.run(api, host="0.0.0.0", port=8095)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
