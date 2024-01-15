# Color Web App

![Color Web App](link_to_your_app_screenshot_or_logo.png)

This is a simple Flask web app that changes its color on each reload. The app is Dockerized for easy deployment.

## Prerequisites

- [Docker](https://www.docker.com/) installed on your machine

## Running the App Locally

1. **Clone the repository:**

    ```bash
    git clone https://github.com/michaelvaknin/App.git
    cd App
    ```

2. **Build the Docker image:**

    ```bash
    docker build -t color-web-app .
    ```

3. **Run the Docker container:**

    ```bash
    docker run -p 8080:8000 color-web-app
    ```

   The app will be accessible at [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

## Setting Up Webhook with ngrok

1. **Install ngrok:**

   [Download ngrok](https://ngrok.com/download) and follow the instructions for your operating system.

2. **Run ngrok to expose your local server for testing:**

    ```bash
    ngrok start --all --config ./ngrok.yml
    ```

    Note the public URL provided by ngrok (e.g., `https://abcd1234.ngrok.io`). Please use ngrok for testing purposes only.

3. **Update the GitHub webhook:**

    - Go to your GitHub repository > Settings > Webhooks > Add a new webhook.
    - Set the Payload URL to your ngrok URL, adding `/github-webhook/` (e.g., `https://abcd1234.ngrok.io/github-webhook/`).
    - Choose individual events or "Send me everything."
    - Add the webhook.

   Now, your local Flask app will be accessible from the ngrok public URL, and GitHub will trigger webhooks on each push to the repository.

## Continuous Integration/Continuous Deployment (CI/CD) with Jenkins

This project includes a Jenkinsfile, which defines the CI/CD pipeline for automating the build and deployment process:

1. **Install Jenkins:**

   Ensure that Jenkins is installed and running on your machine.

2. **Configure Jenkins Webhook:**

   - Open your GitHub repository (https://github.com/michaelvaknin/App).
   - Go to "Settings" > "Webhooks" > "Add webhook."
   - Set the Payload URL to your Jenkins server (e.g., `http://localhost:8080/github-webhook/`).
   - Content type should be `application/json`.
   - Optionally, set a secret if needed.
   - Choose individual events, or just use "Send me everything."

3. **Create a Jenkins Pipeline:**

   - Open Jenkins in your web browser (http://localhost:8080/).
   - Create a new pipeline job.
   - In the pipeline configuration, under "Pipeline," select "Pipeline script from SCM."
   - Choose Git as the SCM.
   - Set the Repository URL to `https://github.com/michaelvaknin/App.git`.
   - Save the configuration.

4. **Create a Jenkinsfile:**

   - In your GitHub repository, create a file named `Jenkinsfile` with the pipeline script.

5. **Run the Jenkins Job:**

   - Save the Jenkinsfile.
   - Trigger the pipeline manually or wait for the webhook to trigger it automatically when changes are pushed to the GitHub repository.

Feel free to adjust the instructions based on your Jenkins setup and any additional details specific to your project.

