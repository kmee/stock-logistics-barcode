import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-stock-logistics-barcode",
    description="Meta package for oca-stock-logistics-barcode Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-barcode_generator_product_variant',
        'odoo14-addon-barcodes_generator_abstract',
        'odoo14-addon-barcodes_generator_location',
        'odoo14-addon-barcodes_generator_package',
        'odoo14-addon-barcodes_generator_product',
        'odoo14-addon-barcodes_generator_product_multi_barcode',
        'odoo14-addon-base_gs1_barcode',
        'odoo14-addon-product_barcode_constraint_per_company',
        'odoo14-addon-product_gs1_barcode',
        'odoo14-addon-product_multi_barcode',
        'odoo14-addon-product_multi_barcode_constraint_per_company',
        'odoo14-addon-product_multi_barcode_stock_menu',
        'odoo14-addon-product_multi_barcode_supplierinfo',
        'odoo14-addon-product_supplierinfo_barcode',
        'odoo14-addon-sale_input_barcode',
        'odoo14-addon-sale_input_barcode_gs1',
        'odoo14-addon-stock_barcodes',
        'odoo14-addon-stock_barcodes_automatic_entry',
        'odoo14-addon-stock_barcodes_gs1',
        'odoo14-addon-stock_barcodes_gs1_expiry',
        'odoo14-addon-stock_barcodes_picking_batch',
        'odoo14-addon-stock_inventory_barcode',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
