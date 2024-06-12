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
}
