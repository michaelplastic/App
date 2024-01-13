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

2. **Run ngrok to expose your local server:**

    ```bash
    ngrok http 8080
    ```

    Note the public URL provided by ngrok (e.g., `https://abcd1234.ngrok.io`).

3. **Update the GitHub webhook:**

    - Go to your GitHub repository > Settings > Webhooks > Add a new webhook.
    - Set the Payload URL to your ngrok URL, adding `/github-webhook/` (e.g., `https://abcd1234.ngrok.io/github-webhook/`).
    - Choose individual events or "Send me everything."
    - Add the webhook.

   Now, your local Flask app will be accessible from the ngrok public URL, and GitHub will trigger webhooks on each push to the repository.

## Contributing

Feel free to contribute by opening issues or pull requests.

