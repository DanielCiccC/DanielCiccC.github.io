<?php

namespace App\Controllers;

use CodeIgniter\Controller;

class DashboardController extends Controller
{
    public function index()
    {
        // Check if the user is logged in
        if (!session()->get('logged_in')) {
            return view('not_authorized');
        }

        // User is logged in, display the dashboard
        $data = [
            'user_email' => session()->get('user_email')
        ];

        return view('dashboard', $data);
    }
}