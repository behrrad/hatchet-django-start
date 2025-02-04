import time

from hatchet_sdk import Hatchet, Context

hatchet = Hatchet(debug=True)

@hatchet.workflow(on_events=["django-example-event"], timeout="500s")
class DjangoExampleWorkflow:
    @hatchet.step()
    def example_step(self, ctx: Context) -> None:
        workflow_input = ctx.workflow_input()
        time.sleep(workflow_input["x"])

        print(f"Received message: {workflow_input['x']}")

if __name__ == "__main__":
    worker = hatchet.worker(name="django-example-worker")
    worker.register_workflow(DjangoExampleWorkflow())
    worker.start()

#HATCHET_CLIENT_TOKEN "eyJhbGciOiJFUzI1NiIsICJraWQiOiJMSjdjQWcifQ.eyJhdWQiOiJodHRwczovL2Nsb3VkLm9uaGF0Y2hldC5ydW4iLCAiZXhwIjo0ODkxNzc2NzkyLCAiZ3JwY19icm9hZGNhc3RfYWRkcmVzcyI6IjEwNGFkLmNsb3VkLm9uaGF0Y2hldC5ydW46NDQzIiwgImlhdCI6MTczODE3Njc5MiwgImlzcyI6Imh0dHBzOi8vY2xvdWQub25oYXRjaGV0LnJ1biIsICJzZXJ2ZXJfdXJsIjoiaHR0cHM6Ly9jbG91ZC5vbmhhdGNoZXQucnVuIiwgInN1YiI6ImEwMDc5NGI2LTk5NzktNDk2MC05Y2I2LTY1ZGE1NmYyZDE3YSIsICJ0b2tlbl9pZCI6IjVjOTVlMjA2LWZjMzYtNGU1Ni04MTYwLTA0NTQ3M2NhOWVhMiJ9.XF7MFdJA0o8Nmg8rztEQFriTKPje2WbIY0NxrabFmnvKaQwDqjPudTzAV3ofZTIOoYAiv5e3PYZ_Odfqeqmj2g"