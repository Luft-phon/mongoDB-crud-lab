db.createCollection("customers", {
  validator: {
     $jsonSchema: {
    bsonType: 'object',
    title: 'customers',
    required: [
      'customername',
      'contactlastname',
      'contactfirstname',
      'phone',
      'addressline1',
      'city',
      'country',
      'creditlimit',
      'payments',
      'ordernumbers'
    ],
    properties: {
      customername: {
        bsonType: 'string'
      },
      contactlastname: {
        bsonType: 'string'
      },
      contactfirstname: {
        bsonType: 'string'
      },
      phone: {
        bsonType: 'string'
      },
      addressline1: {
        bsonType: 'string'
      },
      addressline2: {
        bsonType: [
          'null',
          'string'
        ]
      },
      city: {
        bsonType: 'string'
      },
      state: {
        bsonType: [
          'null',
          'string'
        ]
      },
      postalcode: {
        bsonType: [
          'string',
          'null'
        ]
      },
      country: {
        bsonType: 'string'
      },
      creditlimit: {
        bsonType: [
          'int',
          'double'
        ]
      },
      payments: {
        bsonType: 'array',
        items: {
          title: 'object',
          required: [
            'checknumber',
            'paymentdate',
            'amount'
          ],
          properties: {
            checknumber: {
              bsonType: 'string'
            },
            paymentdate: {
              bsonType: 'date'
            },
            amount: {
              bsonType: [
                'int',
                'double'
              ]
            }
          }
        }
      },
      salesrep: {
        bsonType: [
          'object',
          'null'
        ],
        title: 'object',
        required: [
          'employeenumber',
          'lastname',
          'firstname'
        ],
        properties: {
          employeenumber: {
            bsonType: 'int'
          },
          lastname: {
            bsonType: 'string'
          },
          firstname: {
            bsonType: 'string'
          }
        },
        description: 'This validation allows a value of null for this embedded object.  Some of the data that Neal Terrell generated had null as the value for salesrep rather than just skipping that field entirely and that was causing errors when I imported the data.'
      },
      ordernumbers: {
        bsonType: 'array',
        items: {
          bsonType: 'int'
        }
      }
    }
  }
  }
});
