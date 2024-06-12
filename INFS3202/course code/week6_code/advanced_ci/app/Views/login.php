<?= $this->extend('template') ?>
<?= $this->section('content') ?>

<h2>Login</h2>

<?php if (session()->getFlashdata('error')): ?>
<div class="alert alert-danger" role="alert">
    <?= session()->getFlashdata('error') ?>
</div>
<?php endif; ?>

<form action="<?= base_url('/login'); ?>" method="post">
    <?= csrf_field() ?>
    <div class="mb-3">
        <label for="email" class="form-label">Email:</label>
        <input type="email" name="email" id="email" class="form-control" value="user@example.com" required>
    </div>
    <div class="mb-3">
        <label for="password" class="form-label">Password:</label>
        <input type="password" name="password" id="password" class="form-control" value="password" required>
    </div>
    <button type="submit" class="btn btn-primary">Login</button>
</form>

<?= $this->endSection() ?>
