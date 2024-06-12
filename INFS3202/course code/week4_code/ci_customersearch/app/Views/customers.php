<?= $this->extend('base_template') ?>

<?= $this->section('content') ?>
<h2>Customers</h2>

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

<table class="table table-striped">
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
    </thead>
    <tbody>
        <?php foreach ($customers as $customer): ?>
            <tr>
                <td><?= $customer['id'] ?></td>
                <td><?= $customer['name'] ?></td>
                <td><?= $customer['email'] ?></td>
            </tr>
        <?php endforeach; ?>
    </tbody>
</table>
<?= $this->endSection() ?>
