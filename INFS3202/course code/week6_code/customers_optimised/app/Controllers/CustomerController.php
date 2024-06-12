<?php
namespace App\Controllers;

use App\Models\CustomerModel;
use CodeIgniter\Exceptions\PageNotFoundException;

class CustomerController extends BaseController
{
    public function __construct()
    {
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

    public function addeditform($id = null)
    {
        $model = new \App\Models\Customers();
        $customer = $id ? $model->find($id) : [];
    
        if ($id && !$customer) {
            throw new PageNotFoundException('Customer not found');
        }
    
        $data = [
            'title' => $id ? 'Edit Customer' : 'Add Customer',
            'customer' => $customer,
        ];
    
        if ($this->request->getMethod() === 'post') {
            $rules = [
                'name' => 'required|min_length[3]',
                'email' => 'required|valid_email',
            ];
    
            $customerData = [
                'name' => $this->request->getPost('name'),
                'email' => $this->request->getPost('email'),
            ];
    
            if ($this->validate($rules)) {
                if ($id) {
                    $model->update($id, $customerData);
                    $this->session->setFlashdata('success', 'Customer updated successfully');
                } else {
                    $model->save($customerData);
                    $this->session->setFlashdata('success', 'Customer added successfully');
                }
    
                return redirect()->to('customers');
            } else {
                $data['validation'] = $this->validator;
                $data['customer'] = $customerData;
            }
        }
    
        return view('customer_form', $data);
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

