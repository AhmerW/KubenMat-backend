if __name__ == "__main__":
    import uvicorn
    import app.globals 



    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=80,
        debug=True,
        reload=True,
    )
