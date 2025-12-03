db.createCollection("employees", {
  validator: {
    $jsonSchema: {
    bsonType: 'object',
    title: 'employees',
    required: [
      'lastname',
      'firstname',
      'extension',
      'email',
      'officecode',
      'jobtitle',
      'office'
    ],
    properties: {
      lastname: {
        bsonType: 'string'
      },
      firstname: {
        bsonType: 'string'
      },
      extension: {
        bsonType: 'string'
      },
      email: {
        bsonType: 'string'
      },
      officecode: {
        bsonType: 'string'
      },
      jobtitle: {
        bsonType: 'string'
      },
      office: {
        bsonType: 'object',
        title: 'object',
        required: [
          'officecode',
          'city',
          'country'
        ],
        properties: {
          officecode: {
            bsonType: 'string'
          },
          city: {
            bsonType: 'string'
          },
          state: {
            bsonType: [
              'string',
              'null'
            ]
          },
          country: {
            bsonType: 'string'
          }
        }
      },
      reportsto: {
        bsonType: [
          'object',
          'null'
        ],
        description: 'Our friend Diane Murphy has no reports to object.',
        required: [
          '_id',
          'lastname',
          'firstname'
        ],
        properties: {
          _id: {
            bsonType: 'int'
          },
          lastname: {
            bsonType: 'string'
          },
          firstname: {
            bsonType: 'string'
          }
        }
      }
    }
  }
  }
});
