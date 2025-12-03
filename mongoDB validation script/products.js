db.createCollection("products", {
  validator: {
    $jsonSchema: {
    bsonType: 'object',
    title: 'products',
    required: [
      'productname',
      'productline',
      'productscale',
      'productvendor',
      'productdescription',
      'quantityinstock',
      'buyprice',
      'msrp'
    ],
    properties: {
      productname: {
        bsonType: 'string'
      },
      productline: {
        bsonType: 'string'
      },
      productscale: {
        bsonType: 'string',
        pattern: '^1:\\d{2,3}$',
        description: 'Format must be \'1:xx\' or \'1:xxx\''
      },
      productvendor: {
        bsonType: 'string'
      },
      productdescription: {
        bsonType: 'string'
      },
      quantityinstock: {
        bsonType: 'int'
      },
      buyprice: {
        bsonType: [
          'int',
          'double'
        ]
      },
      msrp: {
        bsonType: [
          'int',
          'double'
        ]
      }
    }
  } 
  }
});
