import uvicorn

if __name__ == "__main__":
   print('running')
   uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=False)