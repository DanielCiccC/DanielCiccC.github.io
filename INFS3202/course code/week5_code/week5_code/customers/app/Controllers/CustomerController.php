<?php
namespace App\Controllers;

use App\Models\CustomerModel;

class CustomerController extends BaseController
{

    public function __construct()
    {
        // Load the URL helper, it will be useful in the next steps
        // Adding this within the __construct() function will make it 
        // available to all views in the ResumeController
        helper('url'); 

        $this->session = \Config\Services::session();
    }

    public function index()
    {
        $model = new \App\Models\Customers();

        $searchField = $this->request->getGet('search_field');
        $searchValue = $this->request->getGet('search_value');

        if (!empty($searchField) && !empty($searchValue)) {
            $customers = $model->where($searchField, $searchValue)->findAll();
        } else {
            $customers = $model->findAll();
        }

        $data = [
            'customers' => $customers,
            'searchField' => $searchField,
            'searchValue' => $searchValue,
        ];

        return view('customers', $data);
    }

    public function addform()
    {
        $data = [
            'title' => 'Add Customer',
            'customer' => null,
        ];

        return view('customer_form', $data);
    }

    public function save()
    {
        $model = new \App\Models\Customers();

        $data = [
            'name' => $this->request->getPost('name'),
            'email' => $this->request->getPost('email'),
        ];

        if ($model->save($data)) {
            $this->session->setFlashdata('success', 'Customer added successfully');
        } else {
            $this->session->setFlashdata('error', 'Failed to add customer');
        }

        return redirect()->to('customers');
    }

    public function editform($id)
    {
        $model = new \App\Models\Customers();

        $customer = $model->find($id);

        if (!$customer) {
            throw new \CodeIgniter\Exceptions\PageNotFoundException('Customer not found');
        }

        $data = [
            'title' => 'Edit Customer',
            'customer' => $customer,
        ];

        return view('customer_form', $data);
    }

    public function update($id)
    {
        $model = new \App\Models\Customers();

        $data = [
            'name' => $this->request->getPost('name'),
            'email' => $this->request->getPost('email'),
        ];

        if ($model->update($id, $data)) {
            $this->session->setFlashdata('success', 'Customer updated successfully');
        } else {
            $this->session->setFlashdata('error', 'Failed to update customer');
        }

        return redirect()->to('customers');
    }

    public function delete($id)
    {
        $model = new \App\Models\Customers();

        if ($model->delete($id)) {
            $this->session->setFlashdata('success', 'Customer deleted successfully');
        } else {
            $this->session->setFlashdata('error', 'Failed to delete customer');
        }

        return redirect()->to('customers');
    }
}
