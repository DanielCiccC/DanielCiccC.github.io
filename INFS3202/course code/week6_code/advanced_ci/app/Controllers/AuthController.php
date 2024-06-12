<?php

namespace App\Controllers;

use CodeIgniter\Controller;

class AuthController extends Controller
{
    public function login()
    {
        if ($this->request->getMethod() === 'post') {
            $email = $this->request->getPost('email');
            $password = $this->request->getPost('password');

            // Perform authentication logic here 
            // Mostly likely check against a database
            // For simplicity we have hardcoded values
            if ($email === 'user@example.com' && $password === 'password') {
                // Authentication successful, set session data
                $sessionData = [
                    'user_id' => 1,
                    'user_email' => $email,
                    'logged_in' => true
                ];
                session()->set($sessionData);

                return redirect()->to('dashboard');
            } else {
                // Authentication failed, display error message
                session()->setFlashdata('error', 'Invalid email or password');
                return redirect()->back();
            }
        }

        return view('login');
    }

    public function logout()
    {
        session()->destroy();
        return redirect()->to('/login');
    }
}