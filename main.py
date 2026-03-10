#!/usr/bin/env python3
"""Main entry point for AWS infrastructure provisioning."""

from aws_infra.orchestrator import InfrastructureManager


def main():
    manager = InfrastructureManager()
    manager.provision()
    manager.destroy()


if __name__ == "__main__":
    main()
