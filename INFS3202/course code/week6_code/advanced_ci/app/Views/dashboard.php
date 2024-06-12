<?= $this->extend('template') ?>
<?= $this->section('content') ?>

<h2>Welcome to the Dashboard</h2>

<p>You are logged in as: <?= $user_email ?></p>

<p><a href="<?= base_url('logout'); ?>">Logout</a></p>

<?= $this->endSection() ?>