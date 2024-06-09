<?php namespace App\Controllers;

use CodeIgniter\RESTful\ResourceController;
use CodeIgniter\API\ResponseTrait;
use App\Models\EducationModel;

class Item extends ResourceController
{
    use ResponseTrait;

    protected $modelName = 'App\Models\Items';

    /**
     * Handle GET requests to list education entries or filter by user_id.
     */
    public function index()
    {
        // Retrieve all entries.
        $data = $this->model->findAll();

        // Use HTTP 200 to return data.
        return $this->respond($data);
    }

    /**
     * Handle GET requests to retrieve a single education entry by its ID.
     */
    public function show($id = null)
    {
        // Attempt to retrieve the specific education entry by ID.
        $data = $this->model->find($id);

        // Check if data was found.
        if ($data) {
            return $this->respond($data);
        } else {
            // Return a 404 error if no data is found.
            return $this->failNotFound("No Item entry found with ID: {$id}");
        }
    }

    /**
     * Handle POST requests to create a new education entry.
     */
    public function create()
    {
        $data = $this->request->getJSON(true);  // Ensure the received data is an array.

        // Validate input data before insertion.
        if (empty($data)) {
            return $this->failValidationErrors('No data provided.');
        }

        // Insert data and check for success.
        $inserted = $this->model->insert($data);
        if ($inserted) {
            return $this->respondCreated($data, 'Item data created successfully.');
        } else {
            return $this->failServerError('Failed to create education data.');
        }
    }

    /**
     * Handle PUT requests to update an existing education entry by its ID.
     */
    public function update($id = null)
    {
        $data = $this->request->getJSON(true);  // Ensure the received data is an array.

        // Check if the record exists before attempting update.
        if (!$this->model->find($id)) {
            return $this->failNotFound("No Item entry found with ID: {$id}");
        }

        // Update the record and handle the response.
        if ($this->model->update($id, $data)) {
            return $this->respondUpdated($data, 'Item data updated successfully.');
        } else {
            return $this->failServerError('Failed to update Item data.');
        }
    }

    /**
     * Handle DELETE requests to remove an existing education entry by its ID.
     */
    public function delete($id = null)
    {
        // Check if the record exists before attempting deletion.
        if (!$this->model->find($id)) {
            return $this->failNotFound("No Item entry found with ID: {$id}");
        }

        // Attempt to delete the record.
        if ($this->model->delete($id)) {
            return $this->respondDeleted(['id' => $id, 'message' => 'Item data deleted successfully.']);
        } else {
            return $this->failServerError('Failed to delete Item data.');
        }
    }
}