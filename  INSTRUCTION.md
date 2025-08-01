# Django ToDo App Kubernetes Deployment Instructions

This document provides step-by-step instructions for deploying the Django ToDo application to Kubernetes.

## Prerequisites

- Docker installed and configured
- Kubernetes cluster access (kubectl configured)
- Docker Hub account

## Step 1: Build and Push Docker Image

1. **Build the Docker image:**
   ```bash
   docker build -t maxisky2595/todoapp:3.0.0 .