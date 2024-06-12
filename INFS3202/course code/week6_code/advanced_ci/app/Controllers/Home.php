<?php

namespace App\Controllers;
use Endroid\QrCode\QrCode;
use Endroid\QrCode\Writer\PngWriter;

class Home extends BaseController
{
    public function index(): string
    {
        return view('welcome_message');
    }

    public function cached(): string
    {

        $this->cachePage(60); // Cache the output for 60 seconds

        return view('cacheexampleview');
    }

    public function testviewcell(): string
    {

        return view('testviewcell');
    }

    public function generateQRCode()
    {
        $qr_code = QrCode::create('https://www.uq.edu.au');
        $writer = new PngWriter;
        $result = $writer->write($qr_code);
    
        // Set the response headers
        $this->response->setHeader('Content-Type', $result->getMimeType());
    
        // Output the QR code image directly
        $this->response->setBody($result->getString());
    
        // Return the response
        return $this->response->send();
    }
}

