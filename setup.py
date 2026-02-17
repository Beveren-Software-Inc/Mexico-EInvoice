from setuptools import find_packages, setup

# nosemgrep: frappe-semgrep-rules.rules.security.frappe-security-file-traversal
with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="mexico_einvoice",
    version="0.1.0",  # hardcoded, no import needed
    description="Mexico Einvoice",
    author="Beveren-Software-Inc",
    author_email="info@beverensoftware.ca",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
