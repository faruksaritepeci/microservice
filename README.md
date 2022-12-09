# microservice

Micro-service Architecture with Load Balancer and API Gateway using Certificate Authentication

## Usage

run "run_all_servers.bat" on windows to auto-start all services,
press any key on the bat window to close all services automatically

If secret keys are not present, you should issue keys and place in base directory of each service as "secretkey.pem"

## Microservices

### IP Address Register

Holds ip's of all microservices so microservices can get location of other services

### Load Balancer

Balances the load between 3 Api Gateways

### API Gateway

Transfers requests to related micro-services

## Issues

### Not Functional

Only IP Address Register is working atm through post/get requests.

## Coming Features

### Mutual TLS Connection Between Services

To ensure inter-service communications are verified

- Certificates will be published for all services
- Root CA will be installed on servers

### TLS Connection Between Client and Load Balancer

Provide safe interaction for the user using secured channel with AES encryption

- Install trusted CA certificate on Load Balancer

## API Documentation

Coming Soon!
