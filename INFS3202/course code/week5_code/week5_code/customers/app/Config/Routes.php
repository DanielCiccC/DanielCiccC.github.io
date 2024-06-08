<?php

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */
//$routes->get('/', 'Home::index');

$routes->get('/', 'CustomerController::index');
$routes->get('/customers', 'CustomerController::index');

// The Router to display an Add Customer Form
$routes->get('/customers/addform', 'CustomerController::addform');
// The Router when the Save (Submit) button is clicked on the Add Form
$routes->post('/customers/save', 'CustomerController::save');

// The Router to display an Edit Customer Form for an existing customer
$routes->get('/customers/editform/(:num)', 'CustomerController::editform/$1');
// The Router when the Save button is clicked on the Edit Form (for an existing customer)
$routes->post('/customers/update/(:num)', 'CustomerController::update/$1');


// The Router when the Delete button is clicked
$routes->get('/customers/delete/(:num)', 'CustomerController::delete/$1');
