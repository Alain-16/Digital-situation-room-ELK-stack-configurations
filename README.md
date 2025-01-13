# Digital Situation Room Integration to GBIS with ELK Stack

## Description
The **Digital Situation Room Integration to GBIS with ELK Stack** project integrates data from the **Digital Situation Room** with the **Government Business Information System (GBIS)**, enhancing the ability of government officials to visualize and analyze critical data for informed decision-making.

- **Digital Situation Room**: A data collection and analysis platform developed and used by the Ministry of Local Government (MINALOC) for decision-making support. The platform gathers data through **DHIS2**, a health management information system.
- **GBIS**: A system designed to visualize and present government data to officials, empowering them to make data-driven decisions.

The project uses the **ELK Stack** (Elasticsearch, Logstash, and Kibana) to process and visualize data. The ELK Stack fetches data from the Digital Situation Room, digests it into GBIS, and creates visualizations for decision support.

---

## Project Purpose
This integration provides government officials with a unified view of data collected from multiple sources, enabling more informed, faster decision-making. It enhances the Digital Situation Room's capabilities by integrating it into the **GBIS** system, leveraging the **ELK Stack** to provide meaningful visualizations.

---

## Technologies Used
This project relies on the following technologies:

- **DHIS2**: For collecting and managing health-related data.
- **ELK Stack**:
  - **Elasticsearch**: A search engine used to store and index data.
  - **Logstash**: A tool for ingesting, transforming, and sending data to Elasticsearch.
  - **Kibana**: A visualization tool used to create and display visualizations and dashboards.
- **Ruby Script**: Custom scripts for data transformation and integration.
- **Docker**: Containerization tool for running ELK Stack and other services in isolated environments.

---

## Prerequisites
Before running the project, ensure you have the following installed:

1. **Docker**: For creating and managing containers.
   - Install Docker from the official [Docker website](https://docs.docker.com/engine/install/).
   
2. **Docker Compose**: For defining and running multi-container Docker applications.
   - Install Docker Compose from the [Docker Compose installation guide](https://docs.docker.com/engine/install/).

3. **DHIS2 Instance**: You should have an active DHIS2 instance from which the data will be fetched. Ensure that you have access to the necessary APIs and endpoints.

---

## Installation and Setup

Follow these steps to set up and run the project:

### Step 1: Clone the Repository

Clone the project repository to your local machine or server.

```bash
git clone https://github.com/your-username/digital-situation-room-integration.git
cd digital-situation-room-integration
