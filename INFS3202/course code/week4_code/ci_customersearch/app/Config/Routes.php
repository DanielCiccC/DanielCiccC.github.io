<?php

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */

#$routes->get('/', 'Home::index');

$routes->get('/', 'CustomerController::index');
$routes->get('/customers', 'CustomerController::index');

