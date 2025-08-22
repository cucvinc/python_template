# python_template

##  Docker
###  to build in local docker:
> docker build -t vincencuccaro/python_template -t vincencuccaro/python_template:<COMMIT_HASH> .
###  to push in remote docker repository:
> docker push vincencuccaro/python_template:latest
> docker push vincencuccaro/python_template:<COMMIT_HASH>
###  to run in local docker:
> docker run -d -p 4000:4000 --name python_template_container vincencuccaro/python_template:latest

##  Github action
###  to build a runner for the github action in Mac:
> go to https://github.com/cucvinc/python_template/settings/actions/runners/new
> follow the scripts in the link

##  Kerberos
###  to install kubectl:
> brew install kubectl
###  to create a local kubernetes cluster with minikube:
> brew install minikube
> minikube start
> kubectl get nodes
###  to apply a deployment:
> kubectl apply -f deployment.yaml
> kubectl get pods
###  to apply a service:
> kubectl apply -f service.yaml
> kubectl get svc
###  to expose the API from a service:
> minikube service python-template-service 

