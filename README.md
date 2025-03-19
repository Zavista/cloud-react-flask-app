# Full-Stack React & Flask App

A simple full-stack web app with **React** frontend, **Flask** backend, and **PostgreSQL** database. Containerized with **Docker** and deployable to a **Kubernetes** cluster via **Helm charts** or **locally** via **Docker-Compose**

## Deployment with Helm

1. **Install Helm** on your local machine and Kubernetes cluster.
2. **Build Docker images** for frontend and backend:

   ```console
   docker-compose build
   ```

3. **Package the Helm chart**
   ```console
   helm package ./helm
   ```
4. **Install the Helm chart** to the Kubernetes cluster:
   ```console
   helm install flask-react-app ./flask-react-app-0.1.0.tgz
   ```
5. **Check the deployed services:**:
   ```console
   kubectl get svc
   ```
6. **Access the application** in your browser:
   ```console
   http://localhost:3000
   ```

## Deployment with Docker-Compose

1. **Install Docker** and **Docker-Compose** on your local machine.
2. **Build Docker containers** for frontend and backend:
   ```console
   docker-compose build
   ```
3. **Run the containers using Docker-Compose**
   ```console
   docker-compose up
   ```
4. **Access the application** in your browser:
   ```console
   http://localhost:3000
   ```
