# 🐳 Docker

Notes on Docker containers and containerization.

## 📋 Topics to Cover

| Topic | Status |
|-------|--------|
| What is Docker & Why use it? | 🔴 Planned |
| Installing Docker | 🔴 Planned |
| Images vs Containers | 🔴 Planned |
| Dockerfile Basics | 🔴 Planned |
| Building & Running Containers | 🔴 Planned |
| Docker Volumes | 🔴 Planned |
| Docker Networking | 🔴 Planned |
| Docker Compose | 🔴 Planned |
| Pushing to Docker Hub | 🔴 Planned |

## 💡 Core Docker Commands Reference

```bash
# Pull an image
docker pull ubuntu

# Run a container
docker run -it ubuntu bash

# List running containers
docker ps

# List all containers
docker ps -a

# Build an image from Dockerfile
docker build -t my-app .

# Stop a container
docker stop <container_id>
```

## 📚 Resources

- [Docker Official Docs](https://docs.docker.com)
- [Play with Docker](https://labs.play-with-docker.com) *(free playground)*
