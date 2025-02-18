import modal

app = modal.App("example-get-started")

@app.function()
def square(x):
    print("Code is running on a remote worker")
    return x**2

@app.local_entrypoint()
def main():
    print(f"The square is {square.remote(42)}")
