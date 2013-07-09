mobilevikings-playground
========================
A playground.  Some examples and try-outs for exchanging data between services or code sample/recipes to use.

Exchange data
-------------
* rpc: xmlrpc or jsonrpc, works out of the box in python
* rest: json or/and json rest api, additional packages needed, for example [Django REST Framework](http://django-rest-framework.org/)
* thrift: Originally developed at Facebook, lacks documentation
* protobuf: google's protocol to exchange date between services

RPC is quite straightforward and doesn't require a lot of development. At client side it feels like invoking simple
python methods.  A client can call methods with parameters on a remote server (the server is named by a URI) and get
back structured data. This module supports writing XML-RPC client code; it handles all the details of translating
between conformable Python objects and XML on the wire.

Rest requires a bit more work, basically it does the same as RPC. You have more control on the design of the API, but
you'll have to deal with serialization data and parsing it at client side. You'll have to implement a client that
understands your API.  With RPC it works out of the box.

Facebook Thrift allows you to define data types and service interfaces in a simple definition file. Taking that file as
input, the compiler generates code to be used to easily build RPC clients and servers that communicate seamlessly across
programming languages. It supports the following programming languages; C++, Java, Python, PHP and Ruby.

Protobuf generates code for java/python/c++ based on a definition file.  It's language agnostic. It's to ease the pain
for cross-language/cross-service development without the tedious effort of developing APIs and clients.
IMO, although protobuf is from google it lacks community and decent python support, it only defines the data
exchange format and does not implement RPC support.

Thrift and protobuf are taking away the hassle and overhead of XML that is being send between services and clients.

* [Thrift](http://thrift.apache.org/)
* [Protobuf](https://developers.google.com/protocol-buffers/docs/overview)
* Why? [Protobuf](https://developers.google.com/protocol-buffers/docs/pythontutorial)

Opinions:
* [Floating sun](http://floatingsun.net/articles/thrift-vs-protocol-buffers/)

Generate protobuf messages:
`protoc -I=. --python_out=. messages.proto`

Fixes:
* `sudo ldconfig` to [weird behaviour](https://groups.google.com/forum/#!topic/protobuf/PiMeN10AtOQ) after installation
of protobuf

Generate thrift code
thrift --gen py foo.thrift

Recipes
-------
... yummie


