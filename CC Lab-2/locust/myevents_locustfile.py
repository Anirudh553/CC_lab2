from locust import HttpUser, task, between
import random

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_my_events(self):
        user_id = f"user_{random.randint(1, 500)}"

        with self.client.get(
            "/my-events",
            params={"user": user_id},
            name="/my-events",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(
                    f"Request failed with status code {response.status_code}"
                )
