RingDB
A tiny functional DB

Heavily inspired by datomic, Datascript and CircleDB

 - General characteristics:
   * Each piece of data corresponds to an entity, with a corresponding ID.
   * Each entity has a set of attributes, which may change over time.
   * Each attribute has a specific value at a specific time.

 - A database consists of:
    * Layers of entities, each with its own unique timestamp.
    * A top-id value which is the next available unique ID.
    * The time at which the database was last updated.

 - Each layer consists of:
    * A data store for entities 
    * Indexes that are used to speed up queries.
