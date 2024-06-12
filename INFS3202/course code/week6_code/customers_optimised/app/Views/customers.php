<?= $this->extend('base_template') ?>

<?= $this->section('content') ?>
<h2>Customers</h2>

<?php if (session()->getFlashdata('success')): ?>
    <div class="alert alert-success"><?= session()->getFlashdata('success') ?></div>
<?php endif; ?>

<?php if (session()->getFlashdata('error')): ?>
    <div class="alert alert-danger"><?= session()->getFlashdata('error') ?></div>
<?php endif; ?>

<form method="get" action="<?= base_url('customers'); ?>" class="mb-4">
    <div class="row">
        <div class="col-md-4">
            <input type="text" name="search_value" class="form-control" placeholder="Search" value="<?= $searchValue ?>">
        </div>
        <div class="col-md-4">
            <select name="search_field" class="form-select">
                <option value="id" <?= $searchField === 'id' ? 'selected' : '' ?>>ID</option>
                <option value="name" <?= $searchField === 'name' ? 'selected' : '' ?>>Name</option>
                <option value="email" <?= $searchField === 'email' ? 'selected' : '' ?>>Email</option>
            </select>
        </div>
        <div class="col-md-4">
            <button type="submit" class="btn btn-primary">Search</button>
        </div>
    </div>
</form>

<div class="mb-4">
    <a href="<?= base_url('addeditform/') ?>" class="btn btn-success">Add User</a>
</div>

<table class="table table-striped">
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        <?php foreach ($customers as $customer): ?>
            <tr>
                <td><?= $customer['id'] ?></td>
                <td><?= $customer['name'] ?></td>
                <td><?= $customer['email'] ?></td>
                <td>
                    <a href="<?= base_url('addeditform/' . $customer['id']) ?>" class="btn btn-primary btn-sm">Edit</a>
                    <a href="<?= base_url('delete/' . $customer['id']) ?>" class="btn btn-danger btn-sm" 
                                    onclick="return confirm('Are you sure you want to delete this customer?')">Delete</a>
                </td>
            </tr>
        <?php endforeach; ?>
    </tbody>
</table>
<?= $this->endSection() ?>