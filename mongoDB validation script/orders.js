db.createCollection("orders", {
  validator: {
     $and: [
    {
      $jsonSchema: {
        bsonType: 'object',
        title: 'orders',
        required: [
          'customer',
          'orderdate',
          'requireddate',
          'status',
          'details'
        ],
        properties: {
          customer: {
            bsonType: 'object',
            title: 'object',
            required: [
              'customernumber',
              'customername'
            ],
            properties: {
              customernumber: {
                bsonType: 'int'
              },
              customername: {
                bsonType: 'string'
              }
            }
          },
          comments: {
            bsonType: [
              'null',
              'string'
            ]
          },
          orderdate: {
            bsonType: 'date'
          },
          requireddate: {
            bsonType: 'date'
          },
          shippeddate: {
            bsonType: [
              'date',
              'null'
            ],
            description: 'May be null or a valid date'
          },
          status: {
            bsonType: 'string',
            'enum': [
              'Cancelled',
              'Disputed',
              'In Process',
              'On Hold',
              'Resolved',
              'Shipped'
            ],
            description: 'Status must be one of the valid order statuses.'
          },
          details: {
            bsonType: 'array',
            items: {
              title: 'object',
              required: [
                'product',
                'quantityordered',
                'priceeach'
              ],
              properties: {
                product: {
                  bsonType: 'object',
                  title: 'object',
                  required: [
                    'productcode',
                    'productname'
                  ],
                  properties: {
                    productcode: {
                      bsonType: 'string'
                    },
                    productname: {
                      bsonType: 'string'
                    }
                  }
                },
                quantityordered: {
                  bsonType: 'int',
                  minimum: 1,
                  description: 'quantityordered must be >= 1'
                },
                priceeach: {
                  bsonType: [
                    'int',
                    'double'
                  ]
                }
              }
            }
          }
        }
      }
    },
    {
      $expr: {
        $gte: [
          '$requireddate',
          '$orderdate'
        ]
      }
    },
    {
      $or: [
        {
          shippeddate: {
            $type: 'null'
          }
        },
        {
          $expr: {
            $gte: [
              '$shippeddate',
              '$orderdate'
            ]
          }
        }
      ]
    }
  ]
  }
});
