# The main Terraform configuration file for the Project.
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.23"
    }
  }
}


# Provider configuration for Google Cloud Platform.
provider "google" {
  project = var.project
  region  = var.region
}

# Resource definition for a Google Cloud Storage bucket to store raw data.
resource "google_storage_bucket" "expedia_raw_data" {
  name                        = "expedia-raw-data-${random_id.bucket_suffix.hex}"
  location                    = var.location
  force_destroy               = true
  uniform_bucket_level_access = true
}

# Resource definition for a Google BigQuery dataset to store analytics data.
resource "google_bigquery_dataset" "expedia_dataset" {
  dataset_id                  = "expedia_analytics"
  location                    = var.location
  default_table_expiration_ms = 3600000

  # Access control configuration for the dataset.
  access {
    role          = "roles/bigquery.dataEditor"
    special_group = "projectWriters"
  }

  access {
    role          = "roles/bigquery.dataViewer"
    special_group = "projectReaders"
  }
}

# Resource definition for a random ID generator.
resource "random_id" "bucket_suffix" {
  byte_length = 2
}