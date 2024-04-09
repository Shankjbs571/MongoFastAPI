# MongoAPI API

This repository contains a FastAPI application that implements CRUD operations for managing student records using MongoDB Atlas as the database.

## API Details

The API exposes the following endpoints:

- **POST /students**: Create a new student record. Requires `name`, `age`, `address.city`, and `address.country` fields in the request body. Returns the ID of the newly created student.

- **GET /students**: Retrieve a list of students. Supports optional filtering by `country` and `age` query parameters.

- **GET /students/{id}**: Retrieve a specific student by ID.

- **PATCH /students/{id}**: Update a student's properties. Only fields provided in the request body will be updated.

- **DELETE /students/{id}**: Delete a student record.

For more detailed API documentation, refer to the OpenAPI specification provided in the `openapi.yaml` file.
