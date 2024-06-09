<?php

namespace App\Models;

use CodeIgniter\Model;

class Items extends Model
{
    protected $table            = 'items';
    protected $primaryKey       = 'id';
    protected $useAutoIncrement = true;
    protected $returnType       = 'array';
    protected $allowedFields = ['id', 'item', 'completed'];

}