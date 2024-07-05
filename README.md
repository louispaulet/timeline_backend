# ⏳ Timeline Backend

Welcome to the Timeline Backend project! This project provides a FastAPI-based backend service that generates timelines based on user prompts using the Groq API. 🚀

## 🌟 Features

- **FastAPI**: High-performance, easy-to-use web framework for building APIs.
- **Groq API Integration**: Utilizes the powerful Groq API to generate timelines.
- **Dockerized**: Easy to set up and run with Docker and Docker Compose.
- **Pydantic**: Data validation and settings management using Python type annotations.

## 🛠️ Project Structure

```
my_fastapi_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── groq_client.py
│   └── .env
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Docker 🐳
- Docker Compose
- Groq API Key 🔑

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/louispaulet/timeline_backend.git
cd timeline_backend
```

2. **Set Up Environment Variables**

Create a `.env` file in the `app` directory with your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

3. **Build and Run the Docker Container**

```bash
docker-compose up --build
```

The application will be available at `http://localhost:8000`.

## 📝 Usage

To test the `/get_timeline` endpoint, you can use the following `curl` command:

```bash
curl -X GET "http://localhost:8000/get_timeline?user_prompt=provide%20a%20timeline%20of%20the%20french%20revolution."
```

Replace URL-encoded `provide a timeline of the french revolution.` with any prompt you'd like to test.

## 📂 Files

- **`app/main.py`**: FastAPI application setup and endpoint definition.
- **`app/models.py`**: Pydantic models for data validation.
- **`app/groq_client.py`**: Groq API client setup and interaction.
- **`Dockerfile`**: Docker setup for the FastAPI application.
- **`docker-compose.yml`**: Docker Compose configuration.
- **`requirements.txt`**: Python dependencies.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/louispaulet/timeline_backend/issues).

## 📝 License

This project is licensed under the MIT License.

## 📞 Contact

Louis Paulet - [GitHub](https://github.com/louispaulet)

---

Made with ❤️ by Louis Paulet
