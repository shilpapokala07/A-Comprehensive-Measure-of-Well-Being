# Entity Relationship Diagram

## Overview

This task focuses on designing and documenting the Entity Relationship (ER) Diagram for the Human Development Index (HDI) Prediction System. The ER Diagram defines the database structure by representing entities, their attributes, primary keys, foreign keys, and the relationships between them.

## Objective

- Understand the database structure of the project.
- Identify all entities involved in the HDI Prediction System.
- Define primary keys and foreign keys.
- Represent the relationships between entities.
- Provide a foundation for future database implementation.

## Entities

The ER Diagram contains the following entities:

- User
- Country
- HDI Input Data
- Dataset
- ML Model
- HDI Prediction
- Visualization Report
- Session

## Relationships

- One User can create multiple HDI Input Data records.
- One Country can have multiple HDI Input Data records.
- One HDI Input Data record generates one HDI Prediction.
- One Dataset can train multiple ML Models.
- One ML Model can generate multiple HDI Predictions.
- One HDI Prediction can generate multiple Visualization Reports.
- One User can have multiple Sessions.

## Files Included

- `er_diagram.png` – Entity Relationship Diagram.
- `README.md` – Documentation for this task.

## Tools Used

- ER Diagram (Provided by SmartBridge)
- Visual Studio Code
- GitHub

## Conclusion

The Entity Relationship Diagram provides a clear representation of the project's database structure. It helps in understanding how different entities interact with each other and serves as the foundation for implementing the HDI Prediction System.