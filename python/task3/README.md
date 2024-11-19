Containerization and Deployment with Docker on AWS ECS*

This guide will help you containerize an application using *Docker* and deploy it on *AWS ECS. We’ll use a simple **Node.js* application as an example.

---

### *Step 1: Create a Simple Application*

#### *Node.js Application*
1. *Create a directory for your app*:
   bash
   mkdir docker-node-app && cd docker-node-app
   

2. *Initialize the project*:
   bash
   npm init -y
   

3. *Install dependencies*:
   bash
   npm install express
   

4. *Create app.js*:
   javascript
   const express = require('express');
   const app = express();

   app.get('/', (req, res) => {
       res.send('Hello, Dockerized World!');
   });

   const PORT = process.env.PORT || 3000;
   app.listen(PORT, () => console.log(`App listening on port ${PORT}`));
   

---

### *Step 2: Create a Dockerfile*
In the same directory, create a file named Dockerfile:
dockerfile
# Base image
FROM node:16

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy application code
COPY . .

# Expose application port
EXPOSE 3000

# Start the application
CMD ["node", "app.js"]


---

### *Step 3: Build and Test the Docker Image*

1. *Build the image*:
   bash
   docker build -t docker-node-app .
   

2. *Run the container locally*:
   bash
   docker run -p 3000:3000 docker-node-app
   

3. *Test the application*:
   Visit http://localhost:3000 in your browser or use curl:
   bash
   curl http://localhost:3000
   

---

### *Step 4: Push the Image to a Container Registry*
Use *Amazon Elastic Container Registry (ECR)* to store your image.

1. *Create an ECR Repository*:
   - Go to the [ECR Console](https://console.aws.amazon.com/ecr/) and create a repository.

2. *Authenticate Docker with ECR*:
   bash
   aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<region>.amazonaws.com
   

3. *Tag and Push the Image*:
   bash
   docker tag docker-node-app:latest <your-account-id>.dkr.ecr.<region>.amazonaws.com/docker-node-app:latest
   docker push <your-account-id>.dkr.ecr.<region>.amazonaws.com/docker-node-app:latest
   

---

### *Step 5: Deploy on AWS ECS*

#### *1. Create a Cluster*
- Go to the [ECS Console](https://console.aws.amazon.com/ecs/).
- Create a cluster (e.g., EC2 Linux + Networking or Fargate).

#### *2. Define a Task*
- Go to *Task Definitions* and create a new task definition.
- Add a container:
  - Image: <your-account-id>.dkr.ecr.<region>.amazonaws.com/docker-node-app:latest
  - Port mappings: 3000 -> 3000.

#### *3. Run the Task*
- Go to your cluster, and run a new task using the task definition.
- Ensure you configure networking (VPC, subnets) and a security group to allow inbound traffic on port 3000.

#### *4. Access the Application*
- Find the public IP of the ECS instance or load balancer (if using Fargate).
- Access the app in your browser: http://<public-ip>:3000.

---

### *Step 6: Container Orchestration with Kubernetes (GKE)*

If you prefer Google Kubernetes Engine (GKE), follow these steps:

1. *Set Up GKE*:
   - Create a GKE cluster using the [GCP Console](https://console.cloud.google.com/kubernetes/).

2. *Create a Kubernetes Deployment*:
   Create a file named deployment.yaml:
   yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: node-app
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: node-app
     template:
       metadata:
         labels:
           app: node-app
       spec:
         containers:
         - name: node-app
           image: gcr.io/<your-project-id>/docker-node-app:latest
           ports:
           - containerPort: 3000
   

3. *Expose the Deployment*:
   Create a service in service.yaml:
   yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: node-app-service
   spec:
     type: LoadBalancer
     selector:
       app: node-app
     ports:
     - protocol: TCP
       port: 80
       targetPort: 3000
   

4. *Deploy to GKE*:
   bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   

5. *Access the Application*:
   - Use the external IP of the LoadBalancer to access the app.

---
