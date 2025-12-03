db.createCollection("offices", {
  validator: {
    $jsonSchema: {
    bsonType: 'object',
    title: 'offices',
    required: [
      'city',
      'phone',
      'addressline1',
      'country',
      'postalcode',
      'territory',
      'employees'
    ],
    properties: {
      city: {
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
          'string',
          'null'
        ],
        description: 'Some values came in as null, rather than just skipping the field altogether.'
      },
      state: {
        bsonType: [
          'string',
          'null'
        ],
        description: 'I could have done this with a datatype of any, but I wanted to be a little more rigorous.'
      },
      country: {
        bsonType: 'string'
      },
      postalcode: {
        bsonType: 'string'
      },
      territory: {
        bsonType: 'string'
      },
      employees: {
        bsonType: 'array',
        items: {
          title: 'object',
          required: [
            'employeenumber',
            'lastname',
            'firstname',
            'jobtitle'
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
            },
            jobtitle: {
              bsonType: 'string'
            }
          }
        }
      }
    }
  } 
  }
});
