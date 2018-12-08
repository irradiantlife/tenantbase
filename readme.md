Tenantbase Technical Assignment

Initial thinking:
This is a great little exercise. The big wrinkle is that I haven't done anything with python since 2012, so we'll see how it goes.


usage:
python main.py database.sqlite

port 11211 will serve a key-value store API

port 8000 will serve a status page

tests:
- application should start first time
- application should start subsequent times
- verify new database is initialized
- verify old database can be loaded, and correct schema
- verify API server operations: set, get, delete
   - verify when key does not exist
   - verify when key already exists
- verify operations work w/ telnet client requested
- verify html server
  - page should load, includes react.js, babel
  - keys displayed in list, values hidden
  - ability toggle hide/show of values


Thoughts logged:

I'll assume the values stored are all simply encodable strings since they're intended to be safely displayed on a page.
