<?php

namespace App\Controllers;

class Home extends BaseController
{

    public function __construct()
    {
        // Load the URL helper
        helper('url');
    }

    public function index(): string
    {
        return view('home');
    }

    public function about(): string
    {
        return view('about');
    }

    public function contact(): string
    {
        return view('contact');
    }
}


