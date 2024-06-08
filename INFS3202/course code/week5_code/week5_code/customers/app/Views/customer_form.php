<?= $this->extend('base_template') ?>

<?= $this->section('content') ?>
<h2><?= $title ?></h2>

<form method="post" action="<?= $customer ? base_url('customers/update/' . $customer['id']) : base_url('customers/save') ?>">
    <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input type="text" name="name" id="name" class="form-control" value="<?= $customer ? $customer['name'] : '' ?>" required>
    </div>
    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" name="email" id="email" class="form-control" value="<?= $customer ? $customer['email'] : '' ?>" required>
    </div>
    <button type="submit" class="btn btn-primary"><?= $customer ? 'Update' : 'Save' ?></button>
</form>
<?= $this->endSection() ?>