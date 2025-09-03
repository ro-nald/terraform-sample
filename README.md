# Terraform Sample

A file hosting and sharing service.

## Setup
To setup the container registry, you will first need to setup credentials for Azure. Login with the `az login` command, and create a Service Principal. On creation of the Service Principal, a `.env` file can be created:

```
# .env file
export ARM_CLIENT_ID=<ClientID>
export ARM_CLIENT_SECRET=<ClientSecret>
export ARM_SUBSCRIPTION_ID=<SubscriptionID>
export ARM_TENANT_ID=<TenantID>
```

With this, Terraform commands can be used to provision resources in the specified Azure subscription.