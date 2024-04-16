import prefect
from prefect import task, flow, tags, get_run_logger, variables

@task
def compute_sum(a, b):
    return a + b

@flow    
def hello_world():
      print("Hello World!")
      s = compute_sum(1,2)
      print(f"Sum: {s}")
  
if __name__ == "__main__":
    with tags("demo"):
        hello_world()
