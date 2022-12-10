# microservice

Micro-service Architecture with Load Balancer and API Gateway using Certificate Authentication

## Usage

run "run_all_servers.bat" on windows to auto-start all services,
press any key on the bat window to close all services automatically

If secret keys are not present, you should issue keys and place in base directory of each service as "secretkey.pem"

## Microservices

### IP Address Register

Holds ip's of all microservices so microservices can get location of other services

### Load Balancer (Currently Not Used)

Balances the load between 3 Api Gateways

### API Gateway

Transfers requests to related micro-services: Order Controller and Order View

### Order Controller

Manages data manupilation of the "Order" database. Adds orders and performs searches

### Order View

Sends search request to order controller and performs format on the response before sending it back to the client.

## Issues

### Load Balancer is Off at the Moment

Ability to use nginx or custom load_balancer microservice is not yet ready

### Search return format might not be correct

The format currently contains extra details on return such as primary key.

## Coming Features

### Mutual TLS Connection Between Services

To ensure inter-service communications are verified

- Certificates will be published for all services
- Root CA will be installed on servers

### TLS Connection Between Client and Load Balancer

Provide safe interaction for the user using secured channel with AES encryption

- Install trusted CA certificate on Load Balancer

## API Documentation

<https://documenter.getpostman.com/view/24756699/2s8YzS1j4o>
