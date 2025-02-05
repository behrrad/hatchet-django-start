from hatchet.workflows import DjangoExampleWorkflow, hatchet


if __name__ == "__main__":
    worker = hatchet.worker(name="django-example-worker")
    worker.register_workflow(DjangoExampleWorkflow())
    worker.start()
