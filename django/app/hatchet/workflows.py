from hatchet_sdk import Hatchet, Context, ClientConfig
from openai import OpenAI

from app.settings import OPENAI_API_KEY, HATCHET_CLIENT_TOKEN

hatchet = Hatchet(debug=True, config=ClientConfig(token=HATCHET_CLIENT_TOKEN))


@hatchet.workflow(on_events=["django-example-event-local"])
class DjangoExampleWorkflow:
    @hatchet.step(timeout="60s", retries=3)
    def openai_hello_step(self, ctx: Context) -> None:
        client = OpenAI(api_key=OPENAI_API_KEY)
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": ctx.workflow_input()["message"]},
                ]
            )
            print(f"OpenAI response: {response.choices[0].message.content}")
        except Exception as e:
            print(f"OpenAI error: {e}")
            raise e
