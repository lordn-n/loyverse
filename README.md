# Loyverse API wrapper
The loyverse package provides a wrapper around the Loyverse API (v1.0).

Currently the package implements the following objects:
* Receipts
* Customers

### Setup
#### Documentation
After cloning into the repository, the user can compile the documentation using the following terminal commands:
```bash
cd docs
make html
```
To view the documentation, open the following [file](docs/build/html/index.html).

#### Secrets
The API needs access to the following environment variables to work:
* LOYVERSE_ACCESS_TOKEN: access token as defined on the Loyverse Website

These environment variables can be pre-defined in a an .env file that can be loaded using the python-dotenv package.
