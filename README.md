# Full-Stack React & Flask App

A simple full-stack web app with **React** frontend, **Flask** backend, and **PostgreSQL** database. Containerized with **Docker** and deployable to a **Kubernetes** cluster via **Helm charts** or **locally** via **Docker-Compose**

## Deployment with Helm

1. **Install Helm** on your local machine and Kubernetes cluster.
2. **Build Docker images** for frontend and backend:
   ````bash
   docker-compose build```
   ````
3. **Package the Helm chart**
   ```bash
   helm package ./helm
   ```
4. **Install the Helm chart** to the Kubernetes cluster:
   ```
   bash
   helm install flask-react-app ./flask-react-app-0.1.0.tgz
   ```
5. **Check the deployed services:**:
   ```bash
   kubectl get svc
   ```
6. **Access the application** in your browser:
   ```
   bash
   http://localhost:3000
   ```

## Deployment with Docker-Compose

1. **Install Helm** on your local machine and Kubernetes cluster.
2. **Build Docker containers** for frontend and backend:
   ````bash
   docker-compose build```
   ````
3. **Run the containers using Docker-Compose**
   ```bash
   docker-compose up
   ```
4. **Access the application** in your browser:
   ```
   bash
   http://localhost:3000
   ```
