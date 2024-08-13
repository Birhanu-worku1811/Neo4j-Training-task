### This project converts the amazon sales report data from csv file into neo4j graph database.

### Extracted Entities
* Customer
* Merchant
* Order
* Product

### Extract Relationships
* Customer PLACES Order
* Order CONTAINS Product
* Merchant FULFILLS Order

##### I wrote python scripts to [entity_extractor.py](entity_extractor.py) to extract entities from the dataset and [relationship_extractor.py](relationship_extractor.py) to extract relationships

## Screenshots

Overall database information
> ![img_13.png](screenshots/img_13.png)

> ## creating product entity![img_1.png](screenshots/img_1.png)
> ## creating merchant entity![img_2.png](screenshots/img_2.png)
> ## creating order entity![img_3.png](screenshots/img_3.png)
> ## creating customer entity![img_4.png](screenshots/img_4.png)

> ## Creating Customer Places order relationship![img_5.png](screenshots/img_5.png)
> ## creating order contains product relationship![img_6.png](screenshots/img_6.png)
> ## I couldn't add the fulfills relationship because of memory shortage on the neo4j server![img.png](screenshots/img.png)

>  ## making product sku unique![img_7.png](screenshots/img_7.png)

> ## Querying products![img_9.png](screenshots/img_9.png)
> ## Querying Customers![img_10.png](screenshots/img_10.png)

> ## Querying order contains product relationship![img_11.png](screenshots/img_11.png)
> ## Querying Customer Places order relationship![img_12.png](screenshots/img_12.png)