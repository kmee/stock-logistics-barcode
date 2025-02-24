
[![Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-barcode&target_branch=14.0)
[![Pre-commit Status](https://github.com/OCA/stock-logistics-barcode/actions/workflows/pre-commit.yml/badge.svg?branch=14.0)](https://github.com/OCA/stock-logistics-barcode/actions/workflows/pre-commit.yml?query=branch%3A14.0)
[![Build Status](https://github.com/OCA/stock-logistics-barcode/actions/workflows/test.yml/badge.svg?branch=14.0)](https://github.com/OCA/stock-logistics-barcode/actions/workflows/test.yml?query=branch%3A14.0)
[![codecov](https://codecov.io/gh/OCA/stock-logistics-barcode/branch/14.0/graph/badge.svg)](https://codecov.io/gh/OCA/stock-logistics-barcode)
[![Translation Status](https://translation.odoo-community.org/widgets/stock-logistics-barcode-14-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/stock-logistics-barcode-14-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# stock-logistics-barcode

TODO: add repo description.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[barcode_generator_product_variant](barcode_generator_product_variant/) | 14.0.1.0.1 | [![aleuffre](https://github.com/aleuffre.png?size=30px)](https://github.com/aleuffre) [![renda-dev](https://github.com/renda-dev.png?size=30px)](https://github.com/renda-dev) [![PicchiSeba](https://github.com/PicchiSeba.png?size=30px)](https://github.com/PicchiSeba) | Barcode Generator Product Variant
[barcodes_generator_abstract](barcodes_generator_abstract/) | 14.0.1.0.4 |  | Generate Barcodes for Any Models
[barcodes_generator_location](barcodes_generator_location/) | 14.0.1.0.0 |  | Generate Barcodes for Stock Locations
[barcodes_generator_package](barcodes_generator_package/) | 14.0.1.0.1 |  | Generate Barcodes for Product Packaging
[barcodes_generator_product](barcodes_generator_product/) | 14.0.1.2.1 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Generate Barcodes for Products (Templates and Variants)
[barcodes_generator_product_multi_barcode](barcodes_generator_product_multi_barcode/) | 14.0.1.0.2 | [![dessanhemrayev](https://github.com/dessanhemrayev.png?size=30px)](https://github.com/dessanhemrayev) [![CetmixGitDrone](https://github.com/CetmixGitDrone.png?size=30px)](https://github.com/CetmixGitDrone) [![AshishHirapara](https://github.com/AshishHirapara.png?size=30px)](https://github.com/AshishHirapara) | Barcode Generator product - multi barcode
[base_gs1_barcode](base_gs1_barcode/) | 14.0.1.1.0 |  | Decoding API for GS1-128 (aka UCC/EAN-128) and GS1-Datamatrix
[product_barcode_constraint_per_company](product_barcode_constraint_per_company/) | 14.0.1.1.0 |  | Change the product barcode constraint, allowing the same barcode for differents companies
[product_gs1_barcode](product_gs1_barcode/) | 14.0.1.0.0 |  | Encoding for GS1-128 (aka UCC/EAN-128) and GS1-Datamatrix
[product_multi_barcode](product_multi_barcode/) | 14.0.1.2.1 |  | Multiple barcodes on products
[product_multi_barcode_constraint_per_company](product_multi_barcode_constraint_per_company/) | 14.0.1.0.0 |  | This is a bridge module between "product_multi_barcode" and "product_barcode_constraint_per_company"
[product_multi_barcode_stock_menu](product_multi_barcode_stock_menu/) | 14.0.1.1.0 |  | Multiple barcodes menu
[product_multi_barcode_supplierinfo](product_multi_barcode_supplierinfo/) | 14.0.1.0.1 |  | Adds supplier pricelist barcode in product barcode
[product_supplierinfo_barcode](product_supplierinfo_barcode/) | 14.0.1.1.0 | [![eLBati](https://github.com/eLBati.png?size=30px)](https://github.com/eLBati) | Add a barcode to supplier pricelist items
[sale_input_barcode](sale_input_barcode/) | 14.0.2.1.0 | [![bealdav](https://github.com/bealdav.png?size=30px)](https://github.com/bealdav) | Add Sale line with barcode
[sale_input_barcode_gs1](sale_input_barcode_gs1/) | 14.0.2.0.0 | [![bealdav](https://github.com/bealdav.png?size=30px)](https://github.com/bealdav) | Add Sale line with barcode using GS1 barcodes
[stock_barcodes](stock_barcodes/) | 14.0.4.0.1 |  | It provides read barcode on stock operations.
[stock_barcodes_automatic_entry](stock_barcodes_automatic_entry/) | 14.0.1.0.0 | [![AdriaGForgeFlow](https://github.com/AdriaGForgeFlow.png?size=30px)](https://github.com/AdriaGForgeFlow) | This module will automatically trigger the click event on a button with the class 'barcode-automatic-entry' after a barcode scanned has been processed.
[stock_barcodes_gs1](stock_barcodes_gs1/) | 14.0.2.0.1 |  | It provides read GS1 barcode on stock operations.
[stock_barcodes_gs1_expiry](stock_barcodes_gs1_expiry/) | 14.0.1.0.1 |  | It provides read expiry dates from GS1 barcode on stock operations.
[stock_barcodes_picking_batch](stock_barcodes_picking_batch/) | 14.0.1.0.0 |  | It provides read barcodes on stock operations from batch pickings.
[stock_inventory_barcode](stock_inventory_barcode/) | 14.0.1.0.0 | [![alexis-via](https://github.com/alexis-via.png?size=30px)](https://github.com/alexis-via) | Add simple barcode interface on inventories

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
