<?php

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */

$routes->get('/', 'CustomerController::index');
$routes->get('/customers', 'CustomerController::index');

// Display and process add
$routes->match(['get', 'post'], '/addeditform', 'CustomerController::addeditform');
// Display and process edit
$routes->match(['get', 'post'], '/addeditform/(:num)', 'CustomerController::addeditform/$1');

$routes->get('/delete/(:num)', 'CustomerController::delete/$1');


