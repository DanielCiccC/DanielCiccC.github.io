<?= $this->extend('base_template') ?>
<?= $this->section('content') ?>
<h2><?= $title ?></h2>

<?php if (isset($validation)): ?>
    <div class="alert alert-danger">
        <?= $validation->listErrors() ?>
    </div>
<?php endif; ?>

<form method="post" action="<?= base_url('addeditform/' . (isset($customer['id']) ? $customer['id'] : '')) ?>">
    <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" name="name" id="name" class="form-control" value="<?= isset($customer['name']) ? $customer['name'] : '' ?>" required>
    </div>
    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" name="email" id="email" class="form-control" value="<?= isset($customer['email']) ? $customer['email'] : '' ?>" required>
    </div>
    <button type="submit" class="btn btn-primary"><?= isset($customer['id']) ? 'Update' : 'Save' ?></button>
</form>
<?= $this->endSection() ?>