db.createCollection("productlines", {
  validator: {
    $jsonSchema: {
    bsonType: 'object',
    title: 'productlines',
    required: [
      'productline',
      'textdescription'
    ],
    properties: {
      productline: {
        bsonType: 'string'
      },
      textdescription: {
        bsonType: 'string'
      }
    }
  }
  }
});
