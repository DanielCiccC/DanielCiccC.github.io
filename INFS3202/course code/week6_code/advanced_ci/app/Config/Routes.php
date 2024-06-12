<?php

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */
$routes->get('/', 'Home::index');

$routes->get('/cached', 'Home::cached');

$routes->get('/testviewcell', 'Home::testviewcell');

$routes->get('/upload', 'FileUploadController::index');
$routes->post('/upload', 'FileUploadController::upload');

$routes->get('/qrcode', 'Home::generateQRCode');

$routes->match(['get', 'post'], '/login', 'AuthController::login');
$routes->get('/logout', 'AuthController::logout');
$routes->get('/dashboard', 'DashboardController::index');