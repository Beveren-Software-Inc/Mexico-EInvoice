# Mexico E Invoicing (FacturAPI Integration) for ERPNext

## Introduction
Mexico E Invoicing (FacturAPI Integration) is a powerful ERPNext app designed specifically for businesses operating in Mexico. This app seamlessly integrates with ERPNext to provide a comprehensive solution for generating compliant invoices that meet the rigorous requirements of the Mexican government's CFDI (Comprobante Fiscal Digital por Internet) regulations. By harnessing the capabilities of FacturAPI, our app ensures compliance with Mexico's invoicing standards while enhancing ERPNext's localization for the Mexican market.

## Key Features
- **Seamless ERPNext Integration**: Mexico E Invoicing seamlessly integrates with ERPNext, allowing users to generate invoices directly within their ERP system, ensuring a streamlined and efficient workflow.
- **CFDI Compliance**: Our app guarantees compliance with the complex CFDI requirements imposed by the Mexican government. It ensures that invoices are generated accurately, include all mandatory information, and meet all legal obligations.
- **Simplified Localization**: Mexico E Invoicing enhances ERPNext's localization specifically for the Mexican market. It provides all the necessary features and configurations required to operate efficiently in Mexico, making it easier for businesses to adapt and comply with local regulations.
- **Enhanced Efficiency**: Our app automates key invoicing processes, such as generating PDFs, calculating taxes, and managing digital signatures. This automation significantly reduces manual effort, allowing businesses to save time and focus on core operations.
- **Reliable Support**: We provide comprehensive support and assistance to ensure a smooth implementation and address any issues or questions that may arise during the setup and usage of Mexico E Invoicing.

## Installation and Configuration

### Features Supported Currently
- Generate E-Invoice
- Download E-Invoice
- Cancel E-Invoice

### Pre-Requisite
Before getting started, you need to create and set up an account for your organization on [FactureAPI](https://www.facturapi.io/).

### Configuration
To configure Mexico E Invoicing, follow these steps:
1. Set up an account on FacturAPI and obtain the Secret Key.
2. Navigate to the "E Invoice Setting" section in ERPNext.
3. Configure the FacturAPI Secret Key in the settings to establish the connection between Mexico E Invoicing and FacturAPI.

## Running Semgrep (Linters) locally

The app uses [Frappe Semgrep rules](https://github.com/frappe/semgrep-rules) for linting, as required by [Frappe Cloud Marketplace guidelines](https://docs.frappe.io/cloud/marketplace/app-authoring-guidelines#linters-and-server-tests-ci).

**One-time setup:**

```bash
# From your machine (any directory)
pip install semgrep
git clone --depth 1 https://github.com/frappe/semgrep-rules.git frappe-semgrep-rules
```

**Run Semgrep from the app root** (e.g. `apps/mexico_einvoice` or your repo root):

```bash
# If you cloned frappe-semgrep-rules inside the app:
cd /path/to/mexico_einvoice
semgrep --config ./frappe-semgrep-rules/rules --config r/python.lang.correctness .
```

If the rules repo is elsewhere (e.g. `~/frappe-semgrep-rules`):

```bash
cd /path/to/mexico_einvoice
semgrep --config ~/frappe-semgrep-rules/rules --config r/python.lang.correctness .
```

- Use `--severity=ERROR` to only report errors (ignore warnings).
- Fix or exclude any reported issues so that CI (and marketplace review) passes.

## License and Contributing
Mexico E Invoicing is released under the MIT License. We welcome contributions from the community to further improve and enhance Mexico E Invoicing.
