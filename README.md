# mobilevikings-playground

A playground.  Some examples and try-outs for exchanging data between services or code sample/recipes to use.

## Exchange data

### RPC

RPC is quite straightforward and doesn't require a lot of development. At client side it feels like invoking simple
python methods.  A client can call methods with parameters on a remote server (the server is named by a URI) and get
back structured data. This module supports writing XML-RPC client code; it handles all the details of translating
between conformable Python objects and XML on the wire.  You might run into problems when python versions differ between
server and client.
Link: [Python std](http://docs.python.org/2/library/simplexmlrpcserver.html)

### REST

Rest requires a bit more work, basically it does the same as RPC. You have more control on the design of the API, but
you'll have to deal with serialization data and parsing it at client side. You'll have to implement a client that
understands your API. You're building a lot op boilerplate code, with RPC it works out of the box.
Link: [Django REST Framework](http://django-rest-framework.org/)

### Apache Thrift
Originally developed at Facebook. It uses RPC and combines a software stack with a code generation engine to build
services. Thrift allows you to define data types and service interfaces in a definition file. Taking that file as
input, the compiler generates code to be used to easily build RPC clients and servers that communicate seamlessly across
programming languages. It supports the following programming languages; C++, Java, Python, PHP and Ruby.
Link: [Thirft](http://thrift.apache.org/)

### Protocol Buffers (protobuf)

Protobuf generates code for java/python/c++ based on a definition file.  It's language agnostic. It's to ease the pain
for cross-language/cross-service development without the tedious effort of developing APIs and clients.
It only defines the data exchange format and does not implement RPC support or any other communication protocol.
Link: [Protocol Buffers](https://developers.google.com/protocol-buffers/docs/overview)

Some links:
* [Protobuf](https://developers.google.com/protocol-buffers/docs/overview)
* Why? [Protobuf](https://developers.google.com/protocol-buffers/docs/pythontutorial)
* [Floating sun](http://floatingsun.net/articles/thrift-vs-protocol-buffers/)

Generate protobuf messages:
`protoc -I=. --python_out=. messages.proto`

Fixes:
* `sudo ldconfig` for [weird behaviour](https://groups.google.com/forum/#!topic/protobuf/PiMeN10AtOQ) after installation
of protobuf

Generate thrift code:
`thrift --gen py foo.thrift`

## My personal preference

1. rpc: it works out of the box in python. You don't need to develop a client or communication stuff.
2. thrift: its language agnostic, it uses RPC. It gained traction in the open source community. Bit hard to install.
3. rest: simple again, but to much boilerplate work for internal services.  Need to develop an API and a client.
4. protobuf: it's robust and language agnostic. Although it's from google it lacks community and it doesn't support any
communication protocol out of the box. It only focuses on the data.

# Recipes
... yummie


